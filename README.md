# Jungle Devs - Backend Challenge #001

* Done by Thales A. Zirbel Hubner

## Overview

### APPs
- Each app has a viewset, an url specification, a serializer and a model. 
Instances can be created or read by any user but only deleted or edited by it's owner.
Deletion cascades.
The following apps have been implemented, their model is the one recommended by this challenge:
    * *User*: Used plain from what is offered by Django. No URL access;
    * *Topic*: the equivalent of a sub-reddit. 
    * *Post*: the equivalent of a *Reddit thread*, a *post* belongs to a *specific topic* and is *created by an user*.
    * *Comment*: the equivalent of a comment, a comment belongs to a *specific post* (which belongs to a *specific topic*) 
    and is *created by an user*.

 Topic, posts and comments have their models timestamped.
 
 ### URL
 
- The entities follow this URL pattern:
    - */topics/* - lists all available topics
    - */topics/{url_name}/* - details (as well as some posts) from a specific topic (identified by *urlname*)
    - */topics/{url_name}/posts/* - lists all posts from a specific topic
    - */topics/{url_name}/posts/{post_id}/* - lists details and some comments from a post
    - */topics/{url_name}/posts/{post_id}/comments/* - lists all comments from a post
    - */topics/{url_name}/posts/{post_id}/comments/{comment_id}/* - lists details from a comment


## Instructions to Run

- Create the virtual environment and activate it

        virtualenv -p python3 venv
        source venv/bin/activate
- Install the requirements `pip install -r requirements.txt`
- Start the dockers `docker-compose up` with the database and the localstack
- Run the server with `python manage.py runserver 8000`
- To use postman you might need to create a superuser with `python manage.py createsuperuser ` and then 
get the accounts authentication token with `python manage.py drf_create_token <user_name>`