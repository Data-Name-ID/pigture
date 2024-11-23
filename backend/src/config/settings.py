from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(BASE_DIR.parent.parent / ".env")
env = environ.Env()
env.prefix = "BACKEND_"

DEBUG = env.bool("DEBUG", default=True)
SECRET_KEY = env.str("SECRET_KEY", default="some_key")

DEFAULT_HOSTS = ["localhost", "127.0.0.1"]
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=DEFAULT_HOSTS)
INTERNAL_IPS = env.list("INTERNAL_IPS", default=ALLOWED_HOSTS)
CSRF_TRUSTED_ORIGINS = env.list("ALLOWED_ORIGINS")

if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CORS_ALLOWED_ORIGINS = CSRF_TRUSTED_ORIGINS

DOCKER = env.bool("DOCKER", default=False)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "rest_framework_simplejwt",
    "core.apps.CoreConfig",
    "images.apps.ImagesConfig",
    "marking.apps.MarkingConfig",
    "patients.apps.PatientsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = (
    {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env.str("DB_NAME"),
            "USER": env.str("DB_USER"),
            "PASSWORD": env.str("DB_PASSWORD"),
            "HOST": env.str("DB_HOST"),
            "PORT": env.int("DB_PORT"),
        },
    }
    if DOCKER
    else {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        },
    }
)


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation"
            ".UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.NumericPasswordValidator"
        ),
    },
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": (
        "rest_framework.pagination.PageNumberPagination"
    ),
    "PAGE_SIZE": 10,
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Our project",
    "DESCRIPTION": "Description",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
}

USE_I18N = True
LANGUAGE_CODE = "ru-ru"

USE_TZ = True
TIME_ZONE = "UTC"

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CELERY_BROKER_URL = (
    f"redis://{env('REDIS_HOST', default='localhost')}:"
    f"{env('REDIS_PORT', default='6379')}/"
    f"{env('REDIS_DB', default='0')}"
)
CELERY_RESULT_BACKEND = (
    f"redis://{env('REDIS_HOST', default='localhost')}:"
    f"{env('REDIS_PORT', default='6379')}/"
    f"{env('REDIS_DB', default='0')}"
)
CELERY_IMPORTS = ["images.tasks"]


if DEBUG:
    INSTALLED_APPS = [
        *INSTALLED_APPS,
        "debug_toolbar",
    ]
    MIDDLEWARE = [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        *MIDDLEWARE,
    ]

    DEBUG_TOOLBAR_CONFIG = (
        {
            "SHOW_TOOLBAR_CALLBACK": lambda _: DEBUG,
        }
        if DOCKER
        else {
            "IS_RUNNING_TESTS": False,
        }
    )
