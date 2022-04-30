from pathlib import Path
import environ
from django.utils.translation import ugettext_lazy as _

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
TEMPLATE_DIR = BASE_DIR / 'templates'

environ.Env.read_env(BASE_DIR / '.env')

SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party Apps:
    'dynamic_preferences',
    'ckeditor',
    'ckeditor_uploader',
    'rosetta',
    'parler',

    # Project Apps:
    'page',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
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
        'DIRS': [TEMPLATE_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'dynamic_preferences.processors.global_preferences',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': env.db('DB_URL', default='sqlite:///db.sqlite3')
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

TIME_ZONE = env('TIME_ZONE', default='Europe/Istanbul')

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = (BASE_DIR / 'static',)

STATIC_ROOT = BASE_DIR / 'public/static'

MEDIA_ROOT = BASE_DIR / 'public/media'

MEDIA_URL = '/media/'

LOCALE_PATHS = (BASE_DIR / 'locale/',)

LANGUAGE_CODE = env('LANGUAGE_CODE', default="en-US")

LANGUAGES = (
    ('en', _('English')),
    ('tr', _('Turkish')),
    ('de', _('German')),
    ('it', _('Italian')),
    ('es', _('Spanish')),
    ('ru', _('Russian')),
    ('fr', _('French')),
)

LANGUAGE_SESSION_KEY = 'language'

ADMIN_URL = env('ADMIN_URL', default="admin/")

EMAIL_HOST = env("EMAIL_HOST", default="")
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")
EMAIL_PORT = env("EMAIL_PORT", default=587)
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default=EMAIL_HOST_USER)

CONTACT_FORM_RECEIVER = env.list('CONTACT_FORM_RECEIVER', default="")

RECAPTCHA_VALIDATION_ACTIVE = env("RECAPTCHA_VALIDATION_ACTIVE", default=False)
RECAPTCHA_SITE_KEY = env('RECAPTCHA_SITE_KEY', default="")
RECAPTCHA_SECRET_KEY = env('RECAPTCHA_SECRET_KEY', default="")

