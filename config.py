import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    '''
    Flask and some of its extensions use the value of the secret
    key as a cryptographic key, useful to generate signatures or
    tokens. The Flask-WTF extension uses it to protect web forms
    against a nasty attack called Cross-Site Request Forgery or
    CSRF (pronounced "seasurf"). As its name implies, the secret
    key is supposed to be secret, as the strength of the tokens
    and signatures generated with it depends on no person outside
    of the trusted maintainers of the application knowing it.
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['krzysztof.filimonowicz@gmail.com']
    POSTS_PER_PAGE = 25
    LANGUAGES = ['en', 'pl']
    TRANSLATOR_KEY = os.environ.get('TRANSLATOR_KEY')
