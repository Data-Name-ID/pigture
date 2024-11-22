from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(BASE_DIR.parent / '.env')

env = environ.Env()
env.prefix = 'DJANGO_'

PORT = env.int('PORT', default=8000)

DEBUG = env.bool('DEBUG', default=True)
SECRET_KEY = env.str('SECRET_KEY', default='fake-key')

DEFAULT_HOSTS = ['localhost', '127.0.0.1']
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=DEFAULT_HOSTS)
INTERNAL_IPS = env.list('INTERNAL_IPS', default=ALLOWED_HOSTS)

CSRF_TRUSTED_ORIGINS = env.list(
    'CSRF_TRUSTED_ORIGINS',
    default=[f'http://{host}:{PORT}' for host in ALLOWED_HOSTS],
)

DOCKER = env.bool('DOCKER', default=False)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = (
    {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env.str('DB_NAME'),
            'USER': env.str('DB_USER'),
            'PASSWORD': env.str('DB_PASSWORD'),
            'HOST': env.str('DB_HOST'),
            'PORT': env.int('DB_PORT'),
        },
    }
    if DOCKER
    else {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        },
    }
)


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.MinimumLengthValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.CommonPasswordValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.NumericPasswordValidator'
        ),
    },
]

USE_I18N = True
LANGUAGE_CODE = 'ru-ru'

USE_TZ = True
TIME_ZONE = 'UTC'

STATIC_URL = 'static/'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


if DEBUG:
    INSTALLED_APPS = [
        *INSTALLED_APPS,
        'debug_toolbar',
    ]
    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        *MIDDLEWARE,
    ]

    DEBUG_TOOLBAR_CONFIG = (
        {
            'SHOW_TOOLBAR_CALLBACK': lambda _: DEBUG,
        }
        if DOCKER
        else {
            'IS_RUNNING_TESTS': False,
        }
    )
