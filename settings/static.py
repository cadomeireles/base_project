from decouple import config


# URL to static files
STATIC_URL = config('STATIC_URL', default='/static/')
