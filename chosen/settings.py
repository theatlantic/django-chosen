import os.path
from django.conf import settings


CHOSEN_ROOT = os.path.normpath(os.path.dirname(__file__))
CHOSEN_MEDIA_ROOT = os.path.join(CHOSEN_ROOT, 'media')
CHOSEN_MEDIA_URL = getattr(settings, 'CHOSEN_MEDIA_URL', None)
