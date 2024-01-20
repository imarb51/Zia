"""
Django settings for dristieye project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os, datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m!+*f$*vb4v+!kev2^us0^^rfmm3$$rg&2&$hr2q97^z^6b^yi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'django.contrib.sites',
    'rest_framework',
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

JWT_AUTH = {
    'JWT_SECRET_KEY': '1234',  # Change this to a strong and secret key
    'JWT_ALGORITHM': 'HS256',
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=1),  # Adjust expiration as needed
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),  # Adjust refresh token expiration as needed
}

SITE_ID = 1
ADMIN_SITE_HEADER = "NEW DRISHTIAI ADMIN"

# message error
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'main.backends.UsernameOrMobileModelBackend',
    # Add any other authentication backends if needed
]

ROOT_URLCONF = 'dristieye.urls'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'dristieye.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# MEDIA_URL = '/media/'  # The URL for serving media files
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_URL = 'doctor_login'
LOGOUT_URL = 'doctor_logout'
LOGIN_REDIRECT_URL = 'home'
AUTH_USER_MODEL = 'main.Doctor'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'info@bioscanai.com'
EMAIL_HOST_PASSWORD = 'jmabshvdqelldiwg'

# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'sajal89304@gmail.com'
# EMAIL_HOST_PASSWORD = 'lpgusqpwjmwlhbnl'

