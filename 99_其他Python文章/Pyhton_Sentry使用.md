# Python Sentry 使用



## 使用方法

- [https://docs.sentry.io/platforms/python/django/](https://docs.sentry.io/platforms/python/django/)


Install  `sentry-sdk`:

```
$ pip install --upgrade 'sentry-sdk==0.14.2'

```

To configure the SDK, initialize it with the Django integration in your  `settings.py`  file:

```
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://32e8bb3xxxxxxxxxxxxxxxxxxxxxxxxxec628ceac2b@sentry.io/4xxxxxx969",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

```

You can easily verify your Sentry installation by creating a route that triggers an error:

```
from django.urls import path

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('sentry-debug/', trigger_error),
    # ...
]

```

Visiting this route will trigger an error that will be captured by Sentry.






## 使用步驟

- [https://docs.sentry.io/platforms/python/django/](https://docs.sentry.io/platforms/python/django/)

### 安裝

```bash
pip install raven
pip install --upgrade sentry-sdk==0.14.2
```


### 設定Django

- settings.py

```py
# Sentry
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_swagger',
    'raven.contrib.django.raven_compat', #加入raven
    'api1',
]




sentry_sdk.init(
    dsn="https://3xxxxxxxxxxxxxxxxxxxxxxxxxxxx628ceac2b@sentry.io/4xxxxxxxxxxxxxx",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
```

- urls.py

```py
def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view),
    path('', include(router.urls)),
    path('sentry-debug/', trigger_error) #加入urls去觸發trigger_error
]
```




### 在瀏覽器輸入

- [http://192.168.43.108:8000/sentry-debug/](http://192.168.43.108:8000/sentry-debug/)



### 然後上去自己的sentry

- 馬上可以看到有報錯


![](https://trello-attachments.s3.amazonaws.com/5e61ca539e20942c41c22c4a/5e61ca986670c26011a76758/2bb7ebc9c7c6da69946a5b74bda95c6e/image.png)
