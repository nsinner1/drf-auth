# Intro to Django

## Authentication & Production Server & Postgresql and Back End Deployment

Lab: 33 and 34 - Authentication & Production Server & Postgresql and Back End Deployment

*Author: Natalie Sinner and Harry Potter*

----

## Description
LAB 33
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

LAB 34
Overview
It’s time to deploy!

First steps are to make sure your Application is able to run well in a remote environment.

Once you are confident that your Application is *deployable` then time to research deployment options.

Feature Tasks and Requirements
NOTE: You can use previous lab’s Application as a starting point or start from scratch.
Modify your application to store SECRET_KEY, ALLOWED_HOSTS, DEBUG and DATABASE information in .env file.
Add CORS capabilities to your app and whitelist allowed origins.
All the code changes will be in settings.py so check the demo code for CORS and Env related lines.
In a nutshell - make your own Application similar to the demo, and put it on the web.
Deployment Requirements
Research web hosting sites capable of working with Docker
NOTE no money is required for this lab but you may choose to create a trial account.
But you are responsible for making sure you don’t hit with charges when trial is complete.
Implementation Notes
You are not required to use Poetry since the requirements.txt is being supplied.
However if you run into issues with supplied requirements.txt then you are responsible for rebuilding.

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

Once server is running, copy and paste URL: http://127.0.0.1:8000/api/v1/books/ or http://0.0.0.0:8001/api/v1/books/ and/or http://35.161.156.9:8000/api/v1/books/

---

### Change Log
***[The change log will list any changes made to the code base. This includes any changes from TA/Instructor feedback]*** 
1.6: *Deployed to AWS* - 19 Sept 2020 
1.5: *Set up authentication* - 17 Sept 2020
1.4: *Set up Permissions & Postgresql* - 16 Sept 2020
1.3: *Set up Docker and new port* - 16 Sept 2020
1.2: *Set up server and verified links are correct between each page* - 16 Sept 2020  
1.1: *Set up scaffolding* - 16 Sept 2020  


------------------------------
For more information on Markdown: https://www.markdownguide.org/cheat-sheet