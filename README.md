

DEBUGS
- Trusted origins when using Django 4
# Trusted origins when using Django4!
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000'
],
ALLOWED_HOSTS = [
    'localhost',
],
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8000',
]


Credits:

- Image for profiles: default image is the same as drf walkthrough project
- Used drf-api walkthrough project as guidance.. many snippets of code.