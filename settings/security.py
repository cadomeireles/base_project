# Key for salting hashes and such
SECRET_KEY = '4h&hnf*mta9ks*3p*it6qvg8k9_uy1%re1o*au5!ar99cxaxus'

# Host names allowed
ALLOWED_HOSTS = []

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
