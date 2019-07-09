import axios from 'axios'
import {getAllCompanies} from '../redux/actions/index'
import store from '../redux/store/index'

export const fetchAllCompanies = (dispatch = store.dispatch) => {
    axios.get("http://localhost:8000/api/company/").then((response) => {
        dispatch(getAllCompanies(response.data))
    }).catch((error) => {
        console.log(error);
    })
};

export const fetchOfficesByCompany = (id) => {
    return axios.get(`http://localhost:8000/api/company/${id}/offices`)
};

export const setNewHeadquarter = (headquarter_id, company_id, company_name) => {
    const data = {
        name: company_name,
        headquarter_id: headquarter_id
    };
    return axios.patch(`http://localhost:8000/api/company/${company_id}/`, data)
};

export const addNewCompany = (formData) => {
    const data = {
        headquarter: {
            country: formData.country,
            street: formData.street,
            postal_code: formData.postalCode,
            city: formData.city,
            monthly_rent: formData.monthlyRent
        },
        headquarter_id: null,
        name: formData.name,
    };
    return axios.post(`http://localhost:8000/api/company/`, data)
};

export const addCompanyForOffice = (formData, company_id) => {
    const data = {
        country: formData.country,
        street: formData.street,
        postal_code: formData.postalCode,
        city: formData.city,
        monthly_rent: formData.monthlyRent,
    };
    return axios.post( `http://localhost:8000/api/company/${company_id}/offices/create`, data)
};