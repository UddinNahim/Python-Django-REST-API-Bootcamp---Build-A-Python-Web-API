# Python-Django-REST-API-Bootcamp---Build-A-Python-Web-API


src/taskful_api/settings.py
we added session based authentication.we just modified settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES':[
        #rest Framework authentication classes
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}



jwt ->

step - 1: pip install django-rest-framework-social-oauth2
step - 2: goto settings and write the install_apps =[
    'oauth2_provider',
    'social_django',
    'rest_framework_social_oauth2'
]