from pathlib import Path

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
DEBUG = True

# Definir o que será usado para login
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"
# Durante os testes, use o console (vai imprimir os e-mails no terminal)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.office365.com' 
# EMAIL_HOST = 'smtp-mail.outlook.com'  # Servidor SMTP do Hotmail/Outlook
EMAIL_PORT = 587  # Porta SMTP para envio de e-mail
EMAIL_USE_TLS = True  # Usar TLS (Transport Layer Security)
EMAIL_HOST_USER = 'philipe2015amancio@hotmail.com'  # Seu e-mail Hotmail
EMAIL_HOST_PASSWORD = 'tlhmoheqppyoqndn'  # Sua senha ou senha de aplicativo (se usar 2FA)
DEFAULT_FROM_EMAIL = 'philipe2015amancio@hotmail.com'  # E-mail do remetente





AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',  # Necessário para o dj-rest-auth
]

# Configuração do allauth para autenticação por e-mail
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # Permite login apenas com e-mail
ACCOUNT_EMAIL_REQUIRED = True  # O e-mail é obrigatório
ACCOUNT_USERNAME_REQUIRED = False  # Remove o campo de username se não for necessário




#Modelo de usuário
AUTH_USER_MODEL = 'profileAuth.Register'  # Substitua 'profileAuth' pelo nome do seu aplicativo


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = os.environ["DEBUG"]

ALLOWED_HOSTS = ['*']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ]
}


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #App para login/register
    'profileAuth.apps.AccountConfig',
    # 'profileAuth',
    'django.contrib.sites',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',#autenticcação por terceiros
    'django_extensions',
    'dj_rest_auth',

    'corsheaders',
    'rest_framework',

]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]

ROOT_URLCONF = 'server.urls'

APPEND_SLASH = False

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     }
 }

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'database',
#        'USER': 'user',
#        'PASSWORD': 'password',
#        'HOST': 'PostgresDB',
#        'PORT': 5432,
#    }
#}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
