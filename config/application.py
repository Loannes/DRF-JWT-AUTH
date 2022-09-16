# !!!!!!!!!!!!!!!!!!!!!!!!!
# 해당 파일은 .gitignore 에 추가하여 깃허브에 올리면 안된다
# 예시를 위해서 포함 시킴

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

APP_SECRET_KEY = 'django-insecure-+n*ow#-k*zzdwl)7^k)oefddyoy_op^aaf$je@95ofzgzvs@qo'

APP_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'default2': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '프로젝트명',
        'USER': 'root',
        'PASSWORD': 'mysql비밀번호',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}