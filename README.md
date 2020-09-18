# Intro to Django

## Django Permissions & Postgresql

Lab: 32 - Django Permissions & Postgresql

*Author: Natalie Sinner and Harry Potter*

----

## Description
Features - Django
Add JWT Authentication to your API.
Install needed libraries in project configuration and/or site settings.
Keep existing authentication so DRF Browsable API still usable.
That includes keeping the styling
Install needed libraries in project configuration and/or site settings.
Features - Docker
Create a boilerplate Dockerfile and docker-compose.yml so you don’t need to start from scratch each time.
Switch to using Gunicorn instead of Django’s built in development server.
mind the number of workers to avoid sluggishness
Warning You will run into styling issues when you switch over to Gunicorn.
On Django side you’ll need to properly handle static files.
Adjust docker-compose.yml so that data is persisted in a volume outside of container.

## Reference 
[StackOverFlow](https://stackoverflow.com/questions/40667519/why-is-django-throwing-error-disallowedhost-at)

---

### Getting Started
Clone this repository to your local machine.

```
$ git clone [https://github.com/nsinner1/drf-auth]
```

### To run the program from VS Code:
Select ```File``` -> ```Open``` -> ```drf-auth```

Next navigate to the location you cloned the Repository.

Double click on the ```drf-auth``` directory.

Then select and open ```drf-auth```

### To run in browser:
Locate directory in terminal

Activate virtual environment:

```
poetry init 
poetry shell
```
Once in virtual environment, run command:

```
python manage.py runserver
```

Once server is running, copy and paste URL: http://127.0.0.1:8000/api/v1/books/ or http://0.0.0.0:8001/api/v1/books/

---

### Change Log
***[The change log will list any changes made to the code base. This includes any changes from TA/Instructor feedback]*** 
1.5: *Set up authentication* - 17 Sept 2020
1.4: *Set up Permissions & Postgresql* - 16 Sept 2020
1.3: *Set up Docker and new port* - 16 Sept 2020
1.2: *Set up server and verified links are correct between each page* - 16 Sept 2020  
1.1: *Set up scaffolding* - 16 Sept 2020  


------------------------------
For more information on Markdown: https://www.markdownguide.org/cheat-sheet