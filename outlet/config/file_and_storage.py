from pathlib import Path
import os
import environ

env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_ROOT = os.path.join(BASE_DIR, env.get_value('MEDIA_ROOT'))
MEDIA_URL = '/'+env.get_value('MEDIA_ROOT')+'/'
