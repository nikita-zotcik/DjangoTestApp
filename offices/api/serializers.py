from django.core.exceptions import ValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework import serializers

from offices.models import Company, Office


class OfficeSerializer(serializers.ModelSerializer):
    headquarter_of = serializers.SerializerMethodField()

    class Meta:
        model = Office
        fields = "__all__"

    def validate(self, attrs):
        for key, value in attrs.items():
            if not key == 'company' and not value:
                raise DRFValidationError({key: "{} can't be empty".format(key)})
        return attrs

    def get_headquarter_of(self, instance):
        if instance.has_is_headquarter():
            return instance.is_headquarter.id

    def save(self, **kwargs):
        try:
            super(OfficeSerializer, self).save(**kwargs)
        except ValidationError as e:
            raise DRFValidationError({'company': e.messages[0]})


class NestedOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        exclude = ('company',)

    def validate(self, attrs):
        for key, value in attrs.items():
            if not value:
                raise DRFValidationError({key: "{} can't be empty".format(key)})
        return attrs


class CompanySerializer(serializers.ModelSerializer):
    headquarter = NestedOfficeSerializer(required=False, write_only=True, allow_null=True)
    headquarter_id = serializers.PrimaryKeyRelatedField(
        queryset=Office.objects.all(),
        required=False,
        write_only=True,
        allow_null=True)
    street = serializers.CharField(source='headquarter.street', max_length=256, read_only=True)
    postal_code = serializers.CharField(source='headquarter.postal_code', max_length=32, read_only=True)
    city = serializers.CharField(source='headquarter.city', max_length=256, read_only=True)

    class Meta:
        model = Company
        fields = "__all__"
        related_fields = ['headquarter']

    def create(self, validated_data):
        print(validated_data)
        office = validated_data.pop('headquarter_id', None)
        if office:
            validated_data['headquarter'] = office
            company = super(CompanySerializer, self).create(validated_data)
            return company
        else:
            headquarter = validated_data.pop('headquarter', None)
            office = self.create_office(headquarter)
            validated_data['headquarter'] = office
            company = super(CompanySerializer, self).create(validated_data)
            return company

    def update(self, instance, validated_data):
        office = validated_data.pop('headquarter_id', None)
        if office:
            validated_data['headquarter'] = office
            company = super(CompanySerializer, self).update(instance, validated_data)
            return company
        else:
            raw_headquarter = validated_data.pop('headquarter', None)
            if raw_headquarter:
                filtered_headquarter = {k: v for k, v in raw_headquarter.items() if v}
                office = self.update_existing_office(
                    filtered_headquarter, instance.headquarter.id)
                validated_data['headquarter'] = office
            company = super(CompanySerializer, self).update(instance,
                                                            validated_data)
        return company

    def create_office(self, office_data):
        return Office.objects.create(**office_data)

    def update_existing_office(self, office_data, office_id):
        Office.objects.filter(pk=office_id).update(**office_data)
        return Office.objects.get(pk=office_id)

    def save(self, **kwargs):
        try:
            super(CompanySerializer, self).save(**kwargs)
        except ValidationError as e:
            raise DRFValidationError({'headquarter': e.messages[0]})
