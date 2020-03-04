from django.conf import settings


def my_envr(request):
    # return the value you want as a dictionary. you may add multiple values in there.
    return {
        # 'PRODUCTION_SERVER': settings.PRODUCTION_SERVER,
        'DB_MODE': settings.DB_MODE,
        'USING_LOCAL_DB': settings.USING_LOCAL_DB,
        'DB_NAME': settings.DB_NAME,
        'DB_HOST': settings.DB_HOST,
        'SITE_FULL_URL': settings.SITE_FULL_URL,
    }
