# weather-newsletter

## Overview
This is a project written primarily in Django with a PostgreSQL database and a Boostrap framework. It consists of a single-page form where a user can enter their email address and choose a city from a drop-down list to sign up for daily weather alerts using the Weather Underground API (as well as the Giphy API). Users are also sent a welcome email upon signing up for the newsletter.

## Setup
1. Clone the repo to your local machine. Install the necessary requirements (including PostgreSQL).
2. Set the following environmental variables used by Django's settings.py file:
```bash
export WUNDERGROUND_KEY='ab1234567890'

export GMAIL_ACCT='sample@gmail.com'
export GMAIL_PW='password'

export PG_DB='postgres'
export PG_USER='postgres'
export PG_PASSWORD='password'
```

3. In root of the project, run `python manage.py migrate`
4. To start the server, in the root directory of the project run `python manage.py runserver`
5. To send out emails, run the corresponding admin command with `python manage.py send_email`

## Screenshots
![Alt text](https://github.com/bleonard33/weather-newsletter/blob/screenshots/screenshots/homepage.png "Signup Page")
![Alt text](https://github.com/bleonard33/weather-newsletter/blob/screenshots/screenshots/sample_email.png "Sample Email")
