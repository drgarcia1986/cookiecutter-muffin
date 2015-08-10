import os

STATIC_FOLDERS = (
    '{{cookiecutter.repo_name}}/common/static',
    '{{cookiecutter.repo_name}}/users/static',
)

# Muffin Plugins
PLUGINS = (
    'muffin_jinja2',
    'muffin_peewee',
    'muffin_session',
)


# Plugins configurations
SESSION_SECRET = 'SecretHere'
SESSION_LOGIN_URL = '/users/signin/'

JINJA2_TEMPLATE_FOLDERS = (
    '{{cookiecutter.repo_name}}/common/templates',
    '{{cookiecutter.repo_name}}/public/templates',
    '{{cookiecutter.repo_name}}/users/templates'
)

PEEWEE_CONNECTION = os.environ.get('DATABASE_URL', 'sqlite:///{{cookiecutter.repo_name}}.sqlite')
