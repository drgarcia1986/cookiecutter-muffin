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
(venv) $ muffin {{cookiecutter.repo_name}} create_db
```
### Start
User command `run` to start `{{cookiecutter.repo_name}}` server
```base
(venv) $ MUFFIN_CONFIG={{cookiecutter.repo_name}}.settings.production muffin {{cookiecutter.repo_name}} run --workers 6
```
Open up your favorite browser to http://localhost:5000/ to see the site running locally.

You can change `workers` numbers according to number os CPU cores.

To change default `port` use `bind` argument
```bash
(venv) $ MUFFIN_CONFIG={{cookiecutter.repo_name}}.settings.production muffin {{cookiecutter.repo_name}} run --bind 0.0.0.0:8000
```
