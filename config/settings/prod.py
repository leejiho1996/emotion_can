from .base import *

ALLOWED_HOSTS = ['3.39.16.254']
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [] 
# STATIC_ROOT가 설정된 경우 STATICFILES_DIRS에 동일한 디렉토리가 있으면 오류 발생