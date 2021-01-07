# DecisionsGame

The Decisions Game is a web app that prompts users to test their decisions.  Users have the ability to create and play different decisions games across many different areas.  Whether that be a nursing decisions game to see if a user can keep their patient alive or a criminology game to see if a user can live as an ex convict for 30 days, the decisions game is full of possibilities.  When creating a decisions game a user inputs: the length of the game (in days), amount of starting money (if applicable), and prompts for user decisions, and the decision options.

## External Requirements

In order to build this project you first have to install:

* [Python 3](https://www.python.org/downloads/)
* [Git](https://git-scm.com/)
* Django framework: install on command line
  - > git clone https://github.com/django/django.git
  - > python -m pip install -e django/
  - > python3 -m venv ~/.virtualenvs/djangodev
  - > ...\> %HOMEPATH%\.virtualenvs\djangodev\Scripts\activate.bat (windows users)
  - > . ~/.virtualenvs/djangodev/bin/activate (ios users)
  - > python -m pip install -e /path/to/your/local/clone/django/


## Setup

Database:
- Django by default uses SQLite 3.8.3 and later
- However, looking into PostgreSQL to see if we need that scalability

## Running

> python manage.py runserver

# Deployment

Webapps need a deployment section that explains how to get it deployed on the
Internet. These should be detailed enough so anyone can re-deploy if needed
. Note that you **do not put passwords in git**.

Mobile apps will also sometimes need some instructions on how to build a
"release" version, maybe how to sign it, and how to run that binary in an
emulator or in a physical phone.

deploy from local to git w jenkins?? look this up - moves code from one server to another
--> pip3 install gunicorn
--> $ pip3 install dj-database-url
--> sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
pip3 install psycopg2-binary
--> python3 manage.py check --deploy
-------**

--> $ brew install heroku/brew/heroku
--> $ heroku login
--> $ git clone https://github.com/SCCapstone/DecisionsGame.git
--> $ cd decisionsgame
--> $ heroku create
--> $ git push heroku main
--> $ heroku ps:scale web=1
--> $ heroku open

# Testing

Unit Testing coming in the future. More details will be add soon.

## Testing Technology

Django test suite (in the Django tests/ directory)
- > python -m pip install -r requirements/py3.txt
- > ./runtests.py #testnamehere
## Running Tests

TODO After Unit Tests are completed.

# Authors

Katherine Kopper  kkopper@email.sc.edu

Miller Banford  banford@email.sc.edu

Hannah Killian  hkillian@email.sc.edu

Andrew Jones  apj2@email.sc.edu

Chen QiWei  qiwei@email.sc.edu
