
1. Clone the repo from the below link using command:
    - `git clone https://github.com/Prachi-13/employee_onboarding_checklist.git`

2. create virtual environment
    - `virutalenv env_name`

3. Active virutal environment
    - `Scripts/active` - for windows
    - `souce bin/activate` - for linux

4. install all depencdencies
    - `pip install -r requirements.txt`

5. change directory/move to src
    - `cd src`

6. run migrations and create a superuser
    - `python manage.py makemigrations`
    - `python manage.py migrate`
    - `python manage.py createsuperuser`

7. runserver
    - `python manage.py runserver`
