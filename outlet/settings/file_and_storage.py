import os

from outlet.env import BASE_DIR, env, env_to_enum

MEDIA_ROOT = os.path.join(BASE_DIR, env('MEDIA_ROOT'))
MEDIA_URL = '/'+env('MEDIA_ROOT')+'/'
STATIC_URL = 'static/'
