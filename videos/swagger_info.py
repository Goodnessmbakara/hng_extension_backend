from django.conf import settings

SWAGGER_INFO = {
    'title': 'Hng Chrome Extension API',
    'description': 'This is an API for a chrome extension that facilitates saving of videos and sharing the videos',
    'version': '1.0',
}

if settings.DEBUG:
    SWAGGER_INFO['host'] = 'localhost:8000'
