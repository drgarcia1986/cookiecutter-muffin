# {{cookiecutter.project_name}}
{{cookiecutter.description}}

## Up and Run
### Virtualenv
Create `virtualenv` with python 3
```bash
$ virtualenv --python python3 venv
```
Active the virtualenv
```bash
$ source venv/bin/active
```
### Requirements
Install `{{cookiecutter.repo_name}}` requirements
```base
(venv) $ pip install -r requirements.txt
```
### Database
Create all tables in configured database (`PEEWEE_CONNECTION` setting or `DATABASE_URL` environment) with `create_db` command
```base
(venv) $ MUFFIN_CONFIG={{cookiecutter.repo_name}}.settings.production muffin {{cookiecutter.repo_name}} create_db
```
### Start
User command `run` to start `{{cookiecutter.repo_name}}` server
```base
(venv) $ MUFFIN_CONFIG={{cookiecutter.repo_name}}.settings.production muffin {{cookiecutter.repo_name}} run --workers 6
```
Open up your favorite browser to http://localhost:5000/ to see the site running locally.

You can change `workers` numbers according to number of CPU cores.

To change default `port` use `bind` argument
```bash
(venv) $ MUFFIN_CONFIG={{cookiecutter.repo_name}}.settings.production muffin {{cookiecutter.repo_name}} run --bind 0.0.0.0:8000
```

### Deploy on Heroku
Follow these steps to deploy the {{cookiecutter.project_name}} to Heroku
* Create Heroku appplication
```bash
$ heroku apps:create {{cookiecutter.repo_name}}
```
* Set `MUFFIN_CONFIG` environment variable
```bash
$ heroku config:set MUFFIN_CONFIG={{cookiecutter.repo_name}}.settings.production
```
* Create a postgresql instance
```bash
$ heroku addons:create heroku-postgresql:hobby-dev
```
_the_ `DATABASE_URL` _environment variable will be set in this command_

* Add `psycopg2` lib to requirements file
```bash
$ echo 'psycopg2' >> requirements.txt
```
* Push {{cookiecutter.project_name}} to Heroku
```bash
$ git push heroku master
```
_don't forget to create a git repository in {{cookiecutter.project_name}} directory to working with Heroku_

* Run `create_db` command
```bash
$ heroku run muffin {{cookiecutter.repo_name}} create_db
```
And open up your browser to https://{{cookiecutter.repo_name}}.herokuapp.com/ to see the site running in heroku environment.
