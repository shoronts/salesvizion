import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'f!wh3q5%^*6&tjnbpm=f-s1d(lrj5&75@n!an#9%%6)^x44231'


# DEBUG = False
# ALLOWED_HOSTS = ['www.salesvizion.com','salesvizion.com', '50.62.81.235']


DEBUG = True
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # My Apps
    'salesviziontheme.apps.SalesvizionthemeConfig',
    'salesvizionusers.apps.SalesvizionusersConfig',
    'salesvizionquestions.apps.SalesvizionquestionsConfig',
    'salesvizionnews.apps.SalesvizionnewsConfig',
    #Text Editor
    'ckeditor',
    'ckeditor_uploader',
]

CKEDITOR_UPLOAD_PATH = "inTextPicture/"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'salesvizion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'salesvizion.wsgi.application'

# Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#             },
#         'NAME': 'salesvizion',
#         'USER': 'salesvizion',
#         'PASSWORD': 'WiuEtN!!@z34',
#         'HOST': '127.0.0.1',
#         'PORT': '3306'
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
        'NAME': 'mark',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

# Password validation

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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
# STATIC_ROOT = '/home/salesvizion/salesvizion/static'

MEDIA_URL = '/media/'
MEDIA_ROOT = [os.path.join(BASE_DIR, 'media')]

LOGIN_REDIRECT_URL = 'profile'
LOGIN_URL = 'login'


#Email options by Godaddy SMTP
EMAIL_HOST = 'a2nlvphout-v01.shr.prod.iad2.secureserver.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'webmaster@salesvizion.com'
EMAIL_HOST_PASSWORD = 'salesvizion1234'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


#Email options by gmail SMTP
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 465
# EMAIL_HOST_USER = 'lynbrookoptical8@gmail.com'
# EMAIL_HOST_PASSWORD = 'Shoron@007'
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False


# CKEditor Configuration Settings
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar': 'full',
        'width': 'auto',
        'height': 'auto',
        # 'toolbar_Custom': [
        #     ['Bold', 'Italic', 'Underline'],
        #     ['NumberedList', 'BulletedList'],
        # ],
    }
}

