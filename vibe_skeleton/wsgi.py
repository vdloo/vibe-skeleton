"""
WSGI config for vibe-skeleton project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vibe_skeleton.settings')
application = get_wsgi_application()
