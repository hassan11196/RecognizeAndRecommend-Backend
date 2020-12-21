# Recognize And Recommend
## Send Base64 of Face to 

`POST /recognition/recognize-face`
Request Body:
```
{
  "face":"data:image/png;base64,iVB.."
}
```
if it returns a username then user is registered.

else if it returns unknown. prompt user for a username and send a base64 Face along with username to the following endpoint

`POST localhost:8000/api/v1/users/`

Request Body:
``` 
{
  "username":"mustafa",
  "profile_photo":"data:image/png;base64,iVBOR..."
}
```
This endpoint returns a `auth_token`, save it. it will be used to authenticate the user with the server.

To Save a user face for training
send Base64 face along with `auth_token` in header.
Call this api in a loop and send 30 different Base64 Faces.

`POST localhost:8000/recognition/save-face`

Request Body:
```
{
  "face":"data:image/png;base64,iVB.."
}
```
Headers:
```
Authorization : Token auth_token
```

After you have saved a users face, hit this api to start training.

`POST localhost:8000/recognition/train-face`


# FACE RECOGNITION 2

#### To Get CSRFMIDDLEWARETOKEN
get: http://127.0.0.1:8000/facerecognition/get_csrf

#### To Train On Individual Image
post: http://127.0.0.1:8000/person/add_person/

multipart form data:  

csrfmiddlewaretoken = ""
name = ""
image = ""  //Image File

#### To Store Person Data Temporily for later training
post: http://127.0.0.1:8000/facerecognition/add_temp_person/

multipart form data:  

csrfmiddlewaretoken = ""
name = ""
image = ""  //Image File

#### To Train All Temporily Stored Images
get: http://127.0.0.1:8000/facerecognition/batch_train/

#### To Get Face Label
post: http://127.0.0.1:8000/facerecognition/get_label/

multipart form data:  

csrfmiddlewaretoken = ""
image = ""  //Image File



## Python - Django Rest Framework boilerplate

This is boilerplate for starting fresh new DRF projects. It's built using [cookiecutter-django-rest](https://github.com/agconti/cookiecutter-django-rest).

## Highlights

- Modern Python development with Python 3.6+
- Bleeding edge Django 3.0+
- Fully dockerized, local development via docker-compose.
- MySQL
- Full test coverage, continuous integration, and continuous deployment.
- Celery tasks

### Features built-in

- Token-based Auth system
- Social (FB + G+) signup/sigin
- API Throttling enabled
- Password reset endpoints
- User model with profile picture field using Easy Thumbnails
- Sentry setup
- Swagger API docs out-of-the-box
- CodeLinter (flake8) and CodeFormatter (yapf)
- Tests (with mocking and factories) with code-coverage support

## API Docs

API documentation is automatically generated using Swagger. You can view documention by visiting this [link](http://localhost:8000/swagger).

## Prerequisites

If you are familiar with Docker, then you just need [Docker](https://docs.docker.com/docker-for-mac/install/). If you don't want to use Docker, then you just need Python3 and MySQL installed.

## Local Development with Docker

Start the dev server for local development:

```bash
cp .env.dist .env
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

## Local Development without Docker

### Install

```bash
python3 -m venv env && source env/bin/activate                # activate venv
cp .env.dist .env                                             # create .env file and fill-in DB info
pip install -r requirements.txt                               # install py requirements
./manage.py migrate                                           # run migrations
./manage.py collectstatic --noinput                           # collect static files
redis-server                                                  # run redis locally for celery
celery -A src.config worker --beat --loglevel=debug
  --pidfile="./celerybeat.pid"
  --scheduler django_celery_beat.schedulers:DatabaseScheduler # run celery beat and worker
```

### Run dev server

This will run server on [http://localhost:8000](http://localhost:8000)

```bash
./manage.py runserver
```

### Create superuser

If you want, you can create initial super-user with next commad:

```bash
./manage.py createsuperuser
```

### Running Tests

To run all tests with code-coverate report, simple run:

```bash
./manage.py test
```

### MySQL - privileges issue

If you experience any problems with DB user privileges during migrations run query below:

`GRANT ALL PRIVILEGES ON [mydb].* TO '[user]'@'localhost';`

You're now ready to ROCK! ✨ 💅 🛳
