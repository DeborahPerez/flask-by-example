# Flask by Example 
Replicated from https://realpython.com/flask-by-example-part-1-project-setup/
All requirements use up to date versions as of June 2019
 
## Blog Posts

This is the repo for the Real Python blog series, Flask by Example -

1. [Part One](https://realpython.com/blog/python/flask-by-example-part-1-project-setup/): Set up a local development environment and then deploy both a staging and a production environment on Heroku.
1. [Part Two](https://realpython.com/blog/python/flask-by-example-part-2-postgres-sqlalchemy-and-alembic): Set up a PostgreSQL database along with SQLAlchemy and Alembic to handle migrations.
1. [Part Three](https://realpython.com/blog/python/flask-by-example-part-3-text-processing-with-requests-beautifulsoup-nltk/): Add in the back-end logic to scrape and then process the word counts from a webpage using the requests, BeautifulSoup, and Natural Language Toolkit (NLTK) libraries.

Check out http://realpython.com

## Quick Start

### First Steps

```sh
$ pyvenv-3.5 env
$ source env/bin/activate
$ pip install -r requirements.txt
```

### Set up Migrations

```sh
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```

### Run

```sh
# the app
$ python app.py
```
