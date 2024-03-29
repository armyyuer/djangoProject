"""
Django settings for djangoProject project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lu^hd7ci)8!7*li(ogq%p86wy!o9clq+w56k!ykbwl4mjzw!i!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']

X_FRAME_OPTIONS = 'ALLOWALL'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'common.apps.CommonConfig',
    'django_crontab',  # 定时任务,需放置在应用之前
    'UserManage',
    'project',
    'orders',
    'Ser',
    'api',
    'dingding',
    'qr_code',
    'menu',
    'group',
    'workflow',
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

ROOT_URLCONF = 'djangoProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        # 'DIRS': [os.path.join(BASE_DIR, 'templates'.replace('\\', '/'))]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'UserManage.templatetags.my_tags',
                # 'menu.templatetags.menu_s',
            ],
            # # 写入libraries，格式为：<"过滤器名称": "位置">
            'libraries': {
                "my_tags": "UserManage.templatetags.my_tags",
                "menu_s": "menu.templatetags.menu_s",
            },
        },
    },
]

WSGI_APPLICATION = 'djangoProject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.mysql',
        #
        # 'NAME': os.environ.get('DJANGO_MYSQL_DATABASE') or 'gxnfc',  # 数据库名字
        # 'USER': os.environ.get('DJANGO_MYSQL_USER') or 'gxnfc',  # 数据库用户名
        # 'PASSWORD': os.environ.get('DJANGO_MYSQL_PASSWORD') or 'qweRasd@2022!@#',  # 数据库密码
        # 'HOST': os.environ.get('DJANGO_MYSQL_HOST') or '127.0.0.1',  # 数据库连接地址
        # 'PORT': int(
        #     os.environ.get('DJANGO_MYSQL_PORT') or 3306),  # 数据库端口
        # 'OPTIONS': {
        #     'charset': 'utf8mb4'},
        'NAME': 'gxnfc',  # 你的数据库名称
        'USER': 'gxnfc',  # 你的数据库用户名
        'PASSWORD': 'Bhxt@249',  # 你的数据库密码
        'HOST': '116.196.109.96',  # 你的数据库主机，留空默认为localhost
        'PORT': '3306',  # 你的数据库端口
    }

}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
# STATIC_URL = '/static/' # 别名
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 文件上传配置
UPLOAD_ROOT = os.path.join(BASE_DIR, 'upload')

# 解决中文乱码问题
CRONTAB_COMMAND_PREFIX = 'LANG_ALL=zh_cn.UTF-8'
# 存放log的路径
CRONJOBS_DIR = "/home/gxnfc/djangoProject/"
# Log文件名
CRONJOBS_FILE_NAME = "CRONJOBS.log"
# 添加定时任务(函数中的输出语句,是输出在.log文件中的)
CRONJOBS = (
    # 每分钟执行一次TestCrontab App中crontabFun的timedExecution函数，执行后将打印结果存储在log文件中
    #  '2>&1'每项工作执行后要做的事
    ('*/1 * * * *', 'api.ccgp.seedtxt', '>>' + CRONJOBS_DIR + CRONJOBS_FILE_NAME + ' 2>&1'),
    # 每分钟执行一次
    ('00 11 * * *', 'api.ccgp.seedtxt', '>>' + CRONJOBS_DIR + CRONJOBS_FILE_NAME + ' 2>&1'),
    # 每天11点执行
    ('0 */4 * * *', 'api.ccgp.seedtxt', '>>' + CRONJOBS_DIR + CRONJOBS_FILE_NAME + ' 2>&1'),
    # 每4小时执行一次
    # * * * * *
    # 分钟(0-59) 小时(0-23) 每个月的哪一天(1-31) 月份(1-12) 周几(0-6)

)

VERSION = '1.0'
