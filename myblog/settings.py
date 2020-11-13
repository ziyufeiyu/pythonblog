"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')qugj+^nh&4pk*ht_0&u3c-1*nw!1&zv6wbkrvbvx*f+0yz()i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'DjangoUeditor', # 编辑器
    'qiniustorage',
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

ROOT_URLCONF = 'myblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.views.global_variable',#添加此处
            ],
        },
    },
]

WSGI_APPLICATION = 'myblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    #'sql_lite3': {  # 原本的default
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3',
    #},
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'python_blog',
            'USER': 'user_nmghssc',
            'PASSWORD': '@wdsr0301',
            'HOST': '127.0.0.1',
            'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# 这个是设置静态文件夹目录的路径
STATICFILES_DIRS = (
    '/usr/local/lib/python3.6/site-packages/django/contrib/admin/static/',
)
#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#)

# 设置文件上传路径，图片上传、文件上传都会存放在此目录里
# MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, "static")

QINIU_ACCESS_KEY = 'M1zsoODbeIyUiWO4lLyrF03i6SK-iZpp_abNSn6I'
QINIU_SECRET_KEY = '0R3_4LMbUxnXwEPKHUggOSRIZy60GxgPKp9E2qpa'
QINIU_BUCKET_NAME = 'caoziangblog'
QINIU_BUCKET_DOMAIN = 'qiniublog.nmghssc.com/'
QINIU_SECURE_URL = False
PREFIX_URL = 'http://'
MEDIA_URL = PREFIX_URL + QINIU_BUCKET_DOMAIN
DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuStorage'

X_FRAME_OPTIONS = 'ALLOWALL'
