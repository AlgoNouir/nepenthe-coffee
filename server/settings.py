# ----------------------------------------------------------------------------------+
#                                                                                   |
#                                      IMPORTS                                      |
#                                                                                   |
# ----------------------------------------------------------------------------------+


from pathlib import Path
import os
import datetime



# ----------------------------------------------------------------------------------+
#                                                                                   |
#                                     ADMIN PANEL                                   |
#                                                                                   |
# ----------------------------------------------------------------------------------+

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Library Admin",
    "site_header": "Library",
    "site_brand": "FORTEENALL",
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "custom_css": "main.css",
    "copyright": "black castle forteenall",
}

# ----------------------------------------------------------------------------------+
#                                                                                   |
#                                      SECURITY                                     |
#                                                                                   |
# ----------------------------------------------------------------------------------+


BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "n_3(l0)3r4rc_rtl8e7_)0oymuara7p9&p^z*y2v*8$n+psdxj"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=5),
}


# ----------------------------------------------------------------------------------+
#                                                                                   |
#                                        CORS                                       |
#                                                                                   |
# ----------------------------------------------------------------------------------+


ALLOWED_HOSTS = ["*"]


# cors
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]


# ----------------------------------------------------------------------------------+
#                                                                                   |
#                                   INSTALLED APPS                                  |
#                                                                                   |
# ----------------------------------------------------------------------------------+


DEPENDENCIES = [
    "rest_framework",
    "corsheaders",
]

MAIN_APPS = [
    'models.order.apps.OrderConfig',
    'models.orderCount.apps.OrdercountConfig',
    'models.menu.apps.MenuConfig',
    'models.person.apps.PersonConfig',
    'core',]


INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    *DEPENDENCIES,
    *MAIN_APPS,
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


# ----------------------------------------------------------------------------------+
#                                                                                   |
#                                     DEFINITION                                    |
#                                                                                   |
# ----------------------------------------------------------------------------------+


ROOT_URLCONF = "server.urls"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

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

WSGI_APPLICATION = "server.wsgi.application"


# ----------------------------------------------------------------------------------+
#                                                                                   |
#                                  DATABASE & FILES                                 |
#                                                                                   |
# ----------------------------------------------------------------------------------+


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "data/db.sqlite3",
    }
}

STATIC_URL = "static/"
STATICFILES_DIRS = ((os.path.join(BASE_DIR, "static")),)
# AUTH_USER_MODEL


# ----------------------------------------------------------------------------------+
#                                                                                   |
#                               INTERNATIONALIZATION                                |
#                                                                                   |
# ----------------------------------------------------------------------------------+


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True
