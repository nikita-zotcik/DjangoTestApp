**Django Test application**

To run app make the following steps:


 1. Go to main project folter
 2. Run   `pip install -r requirements.txt`
 3. Run  `python manage.py migrate`
 4. To check tests run `python manage.py test offices`
 5. To run backend app run ` python manage.py runserver`
 6. To run frontend run `cd frontend` from project root folder
 7. Run `npm install` from `frontend` frolder
 8. Run `npm start` to run frontend app 

*There are some extra tests and validations that frontend doesn't cover
For example we can create office without company and then select 
this office when create a new company. 
Extra validations are presented in API tests*
