"""
Django settings for HealthHub project with comprehensive debugging.
"""

from pathlib import Path
import os
import sys
import traceback
from dotenv import load_dotenv

print("=" * 50)
print("DJANGO SETTINGS DEBUG - KOYEB DEPLOYMENT")
print("=" * 50)

try:
    print(f"Python version: {sys.version}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Python path: {sys.path[:3]}...")  # First 3 entries

    # Check if we can import Django
    import django
    print(f"Django version: {django.get_version()}")

    load_dotenv()
    print("✓ dotenv loaded")

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent
    print(f"BASE_DIR: {BASE_DIR}")
    print(f"BASE_DIR exists: {BASE_DIR.exists()}")
    print(f"Files in BASE_DIR: {list(BASE_DIR.iterdir())[:10]}")  # First 10 files

    # Check environment variables
    print("\nEnvironment Variables Check:")
    env_vars = ['SECRET_KEY', 'DEBUG', 'GEMINI_API_KEY', 'DATABASE_NAME',
                'DATABASE_USER', 'DATABASE_PASSWORD', 'DATABASE_HOST', 'DATABASE_PORT',
                'PORT']
    for var in env_vars:
        value = os.getenv(var)
        if var in ['SECRET_KEY', 'DATABASE_PASSWORD']:
            print(f"{var}: {'✓ SET' if value else '✗ MISSING'}")
        else:
            print(f"{var}: {value if value else '✗ MISSING'}")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-fallback-key-for-debugging")
    print(f"SECRET_KEY configured: {'✓' if SECRET_KEY else '✗'}")

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True  # Force True for debugging
    print(f"DEBUG: {DEBUG}")

    ALLOWED_HOSTS = ['*']
    print(f"ALLOWED_HOSTS: {ALLOWED_HOSTS}")

    LOGIN_URL = "authenticate:signin"

    # Application definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Comment out problematic apps for testing
        # 'django_browser_reload',

        'home',
        'authenticate',
        'workspace',
        'symptom_diagnoser',
        'reminders',
        'health_records',
    ]
    print(f"INSTALLED_APPS count: {len(INSTALLED_APPS)}")

    # Check if apps exist
    for app in ['home', 'authenticate', 'workspace', 'symptom_diagnoser', 'reminders', 'health_records']:
        app_path = BASE_DIR / app
        print(f"App {app} exists: {app_path.exists()}")

    # ASGI_APPLICATION = 'core.asgi.application'  # Comment out for now

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        "whitenoise.middleware.WhiteNoiseMiddleware",
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        # "django_browser_reload.middleware.BrowserReloadMiddleware",  # Comment out
    ]
    print(f"MIDDLEWARE count: {len(MIDDLEWARE)}")

    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    STATIC_ROOT = BASE_DIR / "staticfiles"
    STATIC_URL = '/static/'
    print(f"STATIC_ROOT: {STATIC_ROOT}")
    print(f"STATIC_ROOT exists: {STATIC_ROOT.exists()}")

    ROOT_URLCONF = 'HealthHub.urls'

    # Check if urls.py exists
    urls_file = BASE_DIR / 'HealthHub' / 'urls.py'
    print(f"URLs file exists: {urls_file.exists()}")

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    templates_dir = BASE_DIR / 'templates'
    print(f"Templates directory exists: {templates_dir.exists()}")

    WSGI_APPLICATION = 'HealthHub.wsgi.application'

    # Check if wsgi.py exists
    wsgi_file = BASE_DIR / 'HealthHub' / 'wsgi.py'
    print(f"WSGI file exists: {wsgi_file.exists()}")

    # Database configuration with detailed debugging
    print("\nDatabase Configuration:")
    db_name = os.getenv("DATABASE_NAME")
    db_user = os.getenv("DATABASE_USER")
    db_password = os.getenv("DATABASE_PASSWORD")
    db_host = os.getenv("DATABASE_HOST")
    db_port = os.getenv("DATABASE_PORT")

    if all([db_name, db_user, db_password, db_host, db_port]):
        print("Using PostgreSQL database")
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': db_name,
                'USER': db_user,
                'PASSWORD': db_password,
                'HOST': db_host,
                'PORT': db_port,
                'OPTIONS': {
                    'sslmode': 'require',
                },
            }
        }

        # Test database connection
        try:
            import psycopg2
            print("✓ psycopg2 imported successfully")
        except ImportError as e:
            print(f"✗ psycopg2 import error: {e}")

    else:
        print("Using SQLite database (fallback)")
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }

    # Password validation
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
    LANGUAGE_CODE = 'en-us'
    USE_I18N = True
    USE_TZ = True

    # Default primary key field type
    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    # Email configuration
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
    EMAIL_USE_SSL = False

    print("✓ All settings configured successfully")
    print("=" * 50)

except Exception as e:
    print(f"✗ ERROR in settings.py: {e}")
    print(f"Error type: {type(e).__name__}")
    print("Traceback:")
    traceback.print_exc()
    print("=" * 50)
    raise