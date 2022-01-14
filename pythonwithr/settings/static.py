from . settings import *

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_DIRS = [
    BASE_DIR / 'static/',
]
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
