# cookiecutter-muffin
A [cookiecutter](https://github.com/audreyr/cookiecutter) template for [Muffin](https://github.com/klen/muffin) Framework.

## Features
* Bootstrap stack:
	* [jQuery](https://jquery.com/) v1.11.3.
	* [Twitter Bootstrap](http://getbootstrap.com/) v3.3.5.
* Muffin Stack:
	* [Muffin](https://github.com/klen/muffin) v0.0.105
	* [Muffin-Jinja2](https://github.com/klen/muffin-jinja2) v0.0.11
	* [Muffin-Peewee](https://github.com/klen/muffin-peewee) v0.0.46
	* [Muffin-Session](https://github.com/klen/muffin-session) v0.0.8
* User `SignIn` and `SignUp` with session control.
* Custom middlewares and generic handlers.
* Procfile for deploying to [Heroku](https://www.heroku.com/).

## Usage
```
$ pip install cookiecutter
$ cookiecutter https://github.com/drgarcia1986/cookiecutter-muffin.git
```

## Roadmap
* Provisioning with Ansible.
* Containerization with Docker and docker-compose.
* Unit tests
* Another application (maybe a snippet list).
