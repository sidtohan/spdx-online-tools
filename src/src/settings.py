"""
Django settings for project src.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from secret import getGithubKey, getGithubSecret, getSecretKey, getOauthToolKitAppID, getOauthToolKitAppSecret

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_DIR = os.path.join(BASE_DIR,'app')
API_DIR = os.path.join(BASE_DIR,'api')
TEMPLATE_DIR = os.path.join(APP_DIR, 'templates')
STATIC_PATH = os.path.join(APP_DIR,'static')

LICENSE_REPO_NAME = "license-list-XML"
LICENSE_TEST_REPO_NAME = "TEST-LicenseList-XML"
DEV_REPO_URL = 'https://api.github.com/repos/spdx/{0}'.format(LICENSE_TEST_REPO_NAME)
PROD_REPO_URL = 'https://api.github.com/repos/spdx/{0}'.format(LICENSE_REPO_NAME)
REPO_URL = DEV_REPO_URL

NAMESPACE_REPO_NAME = "license-namespace"
NAMESPACE_TEST_REPO = "license-namespace-test"
NAMESPACE_DEV_REPO_URL = 'https://api.github.com/repos/spdx/{0}'.format(NAMESPACE_TEST_REPO)
NAMESPACE_PROD_REPO_URL = 'https://api.github.com/repos/spdx/{0}'.format(NAMESPACE_REPO_NAME)
NAMESPACE_REPO_URL = NAMESPACE_DEV_REPO_URL

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getSecretKey()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if not DEBUG:
    REPO_URL = PROD_REPO_URL
    NAMESPACE_REPO_URL = NAMESPACE_PROD_REPO_URL

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'api',
    'rest_framework',
    'social_django',
    'oauth2_provider',
    'rest_framework_social_oauth2',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['app/templates'], # to enable registration templates overriding
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.yahoo.YahooOpenId',
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'rest_framework_social_oauth2.backends.DjangoOAuth2',
]

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'app.utils.save_profile',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

SOCIAL_AUTH_GITHUB_KEY = getGithubKey()
SOCIAL_AUTH_GITHUB_SECRET = getGithubSecret()
SOCIAL_AUTH_GITHUB_SCOPE = ['public_repo', 'user:email']

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
	STATIC_PATH,
]

# Media files (Downloadable files)

MEDIA_ROOT = os.path.join(APP_DIR,'media')
MEDIA_URL = '/media/'

# Rest API framework

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        #'oauth2_provider.ext.rest_framework.OAuth2Authentication',  # django-oauth-toolkit < 1.0.0
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  # django-oauth-toolkit >= 1.0.0
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

# Absolute Path for tool.jar
# The online tool uses spdx-tools-2.1.6-SNAPSHOT-jar-with-dependencies.jar from the compiled target folder of java tools
# renamed (for now) as tool.jar in the main src directory of spdx-online tool

JAR_ABSOLUTE_PATH = os.path.join(BASE_DIR, "tool.jar")
# URL Path Variables

LOGIN_REDIRECT_URL = "/app/"
REGISTER_REDIRECT_UTL = "/app/login/"
LOGIN_URL = "/app/login/"
HOME_URL="/app/"

# oauthtoolkit app credentials
OAUTHTOOLKIT_APP_CLIENT_ID = getOauthToolKitAppID()
OAUTHTOOLKIT_APP_CLIENT_SECRET = getOauthToolKitAppSecret()
BACKEND = 'github'
DRFSO2_PROPRIETARY_BACKEND_NAME = 'Github'
DRFSO2_URL_NAMESPACE = 'github_social'

# Online tool usage without login
ANONYMOUS_LOGIN_ENABLED = True

# Password reset link expiration limit (in days)
PASSWORD_RESET_TIMEOUT_DAYS = 3

# this will output emails in the console.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# change to EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# after configuring the smtp correctly

# EMAIL_HOST = 'smtp.<smtp provider>.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'email@<smtp provider>.com'
# EMAIL_HOST_PASSWORD = 'password'
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'SPDX Team <noreply@spdx.com>'
