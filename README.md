
INSTANTES - API - An interactive image sharing app 
==================================

* * *

ABOUT THE WEBSITE:
------------------

* * * 


[DEPLOYED API HEROKU LINK](https://instantes-drf-api.herokuapp.com/)

[DEPLOYED FRONTEND HEROKU LINK - LIVE SITE](https://instantes-react.herokuapp.com/)

[DEPLOYED BACKEND GITHUB REPOSITORY](https://github.com/stephaniecrocker91/djangorestframework-api)



_Instantes_ is a public online blog-styled media platford where users can create a profile and post their images along with a title and content. Users can also view other users profiles, comment, like and favourite them! This interactive platform is designed to provide a a rich online community as users interact with each others posts.

<img src="src/assets/amiresponsive.png" width="500px">
<img src="src/assets/home.png" width="500px">

* * * 


## DATABASE:

* * *

Prior to commencing to write my code out, I planned out the ERD.

<img src="src/assets/erd-map.png" width="1000px">

The User Model: Django default User Model. We will use user (PK) owner which will have a OneToOne relationship and on_delete=models.CASCADE.


User model --> Id(BigAuto), username(char), password (char)

Post model --> ID(BigAuto), Owner(FK), Title(char), content(text), image(imgage with default image in cloudinary)

Likes Model --> Id (BigAuto), Owner(FK), post(FK), created_at(DateTime)

Bookmarks Model --> Id (BigAuto), Owner(FK), post(FK), created_at(DateTime)

Comments Model --> id(BigAuto), Owner(FK), post(FK), created_at(DateTime), updated_at(DateTime), content(text)

Follower Model --> id(BigAuto), Owner(FK), created_at(DateTime), followed(FK)

Profile --> Id(BigAuto), Owner(OnetoOne), name(char), content(text), image(image), created_at(DateTime), updated_at(DateTime)


## TESTING:

I extensively tested manually to ensure that the API was working as intended for my projects purpose. For example...

* Manually verified each url path created to confirm they work and open without error.
* From my api, when searching for a post/profile that exist (using our posts/id or profile/id), the data is retrieved. 
*  When attempting to search for a post/profile that does not... "detail: not found." and we get a 404 not found.
* Verified that the CRUD functionality is available in each app: User, Post, Profile, Comments, Followers, Likes, Bookmarks.
* Creating a new item and checking new item URL path.
* Checked that editing a post works.
* Deleting the item works.
* Ensured search feature returns results.
* When logging into my superuser  administrator in my back-end deployed verison of the api: I can confirm all data entered from the front end is displaying!



## PEP8 testing:

This site was tested and is Pep8 compliant using [Black](https://black.vercel.app/?version=stable&state=_Td6WFoAAATm1rRGAgAhARYAAAB0L-Wj4ARsAnNdAD2IimZxl1N_WlkPinBFoXIfdFTaTVkGVeHShArYj9yPlDvwBA7LhGo8BvRQqDilPtgsfdKl-ha7EFp0Ma6lY_06IceKiVsJ3BpoICJM9wU1VJLD7l3qd5xTmo78LqThf9uibGWcWCD16LBOn0JK8rhhx_Gf2ClySDJtvm7zQJ1Z-Ipmv9D7I_zhjztfi2UTVsJp7917XToHBm2EoNZqyE8homtGskFIiif5EZthHQvvOj8S2gJx8_t_UpWp1ScpIsD_Xq83LX-B956I_EBIeNoGwZZPFC5zAIoMeiaC1jU-sdOHVucLJM_x-jkzMvK8Utdfvp9MMvKyTfb_BZoe0-FAc2ZVlXEpwYgJVAGdCXv3lQT4bpTXyBwDrDVrUeJDivSSwOvT8tlnuMrXoD1Sk2NZB5SHyNmZsfyAEqLALbUnhkX8hbt5U2yNQRDf1LQhuUIOii6k6H9wnDNRnBiQHUfzKfW1CLiThnuVFjlCxQhJ60u67n3EK38XxHkQdOocJXpBNO51E4-f9z2hj0EDTu_ScuqOiC9cI8qJ4grSZIOnnQLv9WPvmCzx5zib3JacesIxMVvZNQiljq_gL7udm1yeXQjENOrBWbfBEkv1P4izWeAysoJgZUhtZFwKFdoCGt2TXe3xQ-wVZFS5KoMPhGFDZGPKzpK15caQOnWobOHLKaL8eFA-qI44qZrMQ7sSLn04bYeenNR2Vxz7hvK0lJhkgKrpVfUnZrtF-e-ubeeUCThWus4jZbKlFBe2Kroz90Elij_UZBMFCcFo0CfIx5mGlrINrTJLhERszRMMDd39XsBDzpZIYV4TcG7HoMS_IF8aMAAAxI-5uTWXbUQAAY8F7QgAAP01Vc6xxGf7AgAAAAAEWVo=)

I set line legth to 79 and Python version to 3.10.

ALL PASSED!


## TECHNOLOGIES USED:

* * *

### MAIN LANGUAGE:

* * *

PYTHON

* * *

### Frameworks, Libraries, Programs:

* * * 

* Django
* Django RestFramework
* Cloudinary
* Heroku
* Pillow
* Django Rest Auth
* PostgreSQL

* * *


## BUGS, ISSUES & FIXES:

* * *

* Initially intalled django 4.1
pip3 install 'django<4'

Django 3.2 is the LTS (Long Term Support) version of Django and is therefore preferable to use over the newest Django 4




## DEPLOYMENT:

* * *


### CREATING THE PROJECT

1. Create GitHub repository.
2. Create project app on Heroku.
3. Add Postgres package to the Heroku app via Resources tab.
4. Installe the following packages using the pip install command:

'django<4'
dj3-cloudinary-storage
Pillow
djangorestframework
django-filter
dj-rest-auth
'dj-rest-auth[with_social]'
djangorestframework-simplejwt
dj_database_url psycopg2
gunicorn
django-cors-headers

5. Created the Django project with command:

django-admin startproject project_name .

6. In Heroku, Settings tab, add configvars:

Key: SECRET_KEY | Value: hidden
Key: CLOUDINARY_URL | Value: cloudinary://hidden
Key: DISABLE_COLLECTSTATIC | Value: 1
Key: ALLOWED_HOST | Value: api-app-name.herokuapp.com

7. Once the ReactApp is created, add configvars: (Check that the trailing slash \ at the end of both links has been removed.)

Key: CLIENT_ORIGIN | Value: Heroku app link
Key: CLIENT_ORIGIN_DEV | Value: Gitpod link

Pleas note: Gitpod occasionally updates the browser preview link. Should this occur, the CLIENT_ORIGIN_DEV value shall need to be updated.

8. Created env.py file and add variables. 

import os

os.environ['CLOUDINARY_URL'] = 'cloudinary://hidden'
os.environ['DEV'] = '1'
os.environ['SECRET_KEY'] = 'hidden'
os.environ['DATABASE_URL'] = 'postgres://hidden'

IN SETTINGS.PY

9. Add  to INSTALLED_APPS to support the newly installed packages:

'cloudinary_storage',
'django.contrib.staticfiles',
'cloudinary',
'rest_framework',
'django_filters',
'rest_framework.authtoken',
'dj_rest_auth',
'django.contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount',
'dj_rest_auth.registration',
'corsheaders',

10. Import the database, regular expression module and the env.py

import dj_database_url
import re
import os
if os.path.exists('env.py')
    import env

11. Below import statements, add variable for Cloudinary:

CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.ger('CLOUDINARY_URL')
}

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinartStorage'

12. Below INSTALLED_APPS, set site ID:

SITE_ID = 1
Below BASE_DIR, create the REST_FRAMEWORK, and include page pagination to improve app loading times, pagination count, and date/time format:
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}

13. Set the default renderer to JSON:

if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]

14. Undet this, add:

REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'

15. 
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'project_name.serializers.CurrentUserSerializer'
}

16. Updated DEBUG:

DEBUG = 'DEV' in os.environ

17. Updated the DATABASES variable:

DATABASES = {
    'default': ({
       'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    )
    )
}

18. Added the Heroku app to ALLOWED_HOSTS variable:

os.environ.get('ALLOWED_HOST'),
'localhost',

19. Below ALLOWED_HOST, add CORS_ALLOWED variable:

if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]

if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]

20. Add to top of MIDDLEWARE:

'corsheaders.middleware.CorsMiddleware',

21. Created a Procfile and add:
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn project_name.wsgi

22. Migrated the database:

python3 manage.py makemigrations
python3 manage.py migrate

23. Freeze requirements:

pip3 freeze --local > requirements.txt

24. Add, commit, push the changes to GitHub

25. Navigated back to heroku, and under the ‘Deploy’ tab, connect the GitHub repository.

26. Deployed the branch.

* * *

## CREDITS:

* * *

### CONTENT:

* * *

* I used the CI Moments walkthrough project as atemplate for my own API. Classes and functions have been credited.
* I made some moditications to the ERD. I added a Bookmakrs model, which will allow me to display favourite posts. I used the Likes Model as inspiration.

* * *
### MEDIA:

* * *

- Image for profiles: default image is the same as drf walkthrough project
- Image for default post: same as walkthrough project.

* * *

