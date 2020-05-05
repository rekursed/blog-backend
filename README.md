# Django REST Backend to be consumed by a React Frontend using next.js
##Installation
I am using [pipenv](https://github.com/pypa/pipenv) for package management.
```
# after checkout
cd project_directory
pipenv install
# Copy .env from example
cp .env.example .env
# .env file needs to be filled with right creds

#Migrate to datasource
./manage.py makemigrations
./manage.py migrate
#run server
./manage.py runserver
```