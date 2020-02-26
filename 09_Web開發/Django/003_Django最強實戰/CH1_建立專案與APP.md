# CH1_建立專案與APP

## 大綱

> 1. 進入虛擬環境
> 2. 建立Django專案
> 3. 環境設定
> 4. 視圖(view)與URL

## 1. 進入虛擬環境

```bash
# 進入虛擬環境
source ~/anaconda3/bin/activate

# 退出
conda deactivate
```



## 2. 建立Django專案



### 2-1. 建立專案
```bash
(base) [cabie@centosclean chapter_01]$ django-admin startproject first_project
(base) [cabie@centosclean chapter_01]$ ls
first_project
(base) [cabie@centosclean chapter_01]$ cd first_project/
(base) [cabie@centosclean first_project]$ ls
first_project  manage.py
```

```bash
(base) [cabie@centosclean first_project]$ tree .
.
├── first_project
│   ├── asgi.py    
│   ├── __init__.py    #使得該目錄成為一個Python package
│   ├── settings.py    #本專案設定檔
│   ├── urls.py    # url配置檔
│   └── wsgi.py    #網頁伺服器和 Django介面設定檔
└── manage.py

1 directory, 6 files

```





### 2-2. 建立APP

APP相當於project的元件，而且可以當作其他專案的套件，每個project可以建立一個或多個APP


```bash
(base) [cabie@centosclean first_project]$ python manage.py startapp myapp
(base) [cabie@centosclean first_project]$ ls
first_project  manage.py  myapp

```

- 建立templates目錄、static目錄:這兩個要建立在傳案最上層，與所有APP平行。
```bash
(base) [cabie@centosclean first_project]$ pwd
/home/cabie/01_python/01_Django/002_django最強實戰/chapter_01/first_project
(base) [cabie@centosclean first_project]$ ls
first_project  manage.py  myapp  static  templates

```
templates目錄: 放置HTML檔
static目錄: 會使用到的圖形檔、CSS、javascript檔，除了以url方式儲存在網站上，也會以本機方式儲存在static目錄中。






### 2-3. 建立migration資料檔

-  Django通常要使用資料庫，會將建立資料表的結構與版本記錄下來，以利以後追蹤，若後面不佳APP，則會對所有APP進行makemigrations。
```bash
python manage.py makemigrations myapp
```




### 2-4. 模型與資料庫同步

- 利用migrate可以根據migration的紀錄，將模型同步到資料庫。
然後會產生一個db.sqlite3檔案，這個就是Django預設資料庫檔案。
```bash
(base) [cabie@centosclean first_project]$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK

```


### 2-5. 啟動Server

```bash
(base) [cabie@centosclean first_project]$ python manage.py runserver 0.0.0.0:8000
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 26, 2020 - 08:13:44
Django version 3.0.3, using settings 'first_project.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.

```

![](https://images2.imgbox.com/60/50/h2UBRBLx_o.png)

因為未將此ip加入ALLOWED_HOSTS，更改settings.py<br>

```
ALLOWED_HOSTS = ["192.168.1.108"]
或
ALLOWED_HOSTS = ["*"]
```

![](https://images2.imgbox.com/d7/ab/8BzYg4nr_o.png)








## 3. 環境設定


### 3-1. 除錯模式

部屬上線時，記得要改成False

```bash
DEBUG = True
```


### 3-2. 加入APP

```bash
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]

```

### 3-3. 設定Template路徑

- BASE_DIR為專案的最上層，本例為first_app
```bash
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR,'templates')], #加上templates路徑
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


```


### 3-4. 改語系及時區

```bash
#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hant'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Taipei'

```


### 3-5. 設定static靜態檔路徑


```bash
STATIC_URL = '/static/'

STATICFILES_DIRS = [ os.path.join(BASE_DIR,'static') ,]


```



## 4. 視圖(view)與URL

Django視透過urlpattern網址與函式對照的方式，主要有兩個步驟:
1. 設定 urls.py檔 urlpatterns串列中url網址和函式對照
2. 在views.py撰寫函式




### 4-1. 設定 urls.py

```py
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

```
當你打http://localhost:8000/admin時，將會執行admin.dite.urls函式，因為admin.dite.urls在django.contrib套件中的admin中，因此必須import進來。


- url語法
```
url(網址,函式),
```
- 範例: (^代表正規表達式開始，$代表正規表達式結束)-不知為何沒辦法跑
```bash
from django.contrib import admin
from django.urls import path

from myapp.views import sayhello


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', sayhello),
]

```



### 4-2. 設定 views.py


```py
from django.shortcuts import render

from django.http import HttpResponse #因為下面要使用HttpResponse


# Create your views here.
def sayhello(request): #規定一定要有request
    return HttpResponse("Hello Pizza !!!!")


```

![](https://images2.imgbox.com/2c/d1/UapZR8iD_o.png)




### 4-3. 改變url

```py
from django.contrib import admin
from django.urls import path

from myapp.views import sayhello


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'hello', sayhello),
]


```


![](https://images2.imgbox.com/34/bf/1e8tjvpb_o.png)






### 4-4. url傳遞參數

- urls.py : Django新版本url表示不一樣了
- [Django 2.0 以 path 函式設定 urlpatterns](http://blog.e-happy.com.tw/django2-0-%E4%BB%A5-path-%E5%87%BD%E5%BC%8F%E8%A8%AD%E5%AE%9A-urlpatterns/)

```js
傳遞參數型別：

-   **str**：字串，匹配任何非空字符串，但不含「/」字元，這是預設值。
-   **int**：匹配 0 及正整數，傳回一個 int 型別。
-   **slug**：匹配字母、數字以及 /、 組成的字串，是 url 在最後一部分的註釋文字。
-   **uuid**：匹配格式化的 uuid，為了防止衝突，規定必須使用「-」字元，所有字母必須小寫。如 075194d3-6885-417e-a8a8-6c931e272f00。它會傳回一個 UUID 物件。
-   **path**：匹配任何非空字符串，包含路徑分隔符號「/」。
```


```py
from django.contrib import admin
from django.urls import path

from myapp.views import sayhello,hello2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello2/<str:username>/', hello2),
]


```



- views.py
```py
from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def sayhello(request):
    return HttpResponse("Hello Pizza !!!")



def hello2(request,username):
    return HttpResponse("Hello "+ username)


```

![](https://images2.imgbox.com/c0/b5/9D4eyN4k_o.png)







### 4-5. 模板的使用


- HTML : 先在templates目錄下新增一個 hello3.html
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>第一個模板</title>
    </head>
    <body>
        <h1>歡迎光臨: {{username}}</h1>
        <h2>現在時間: {{now}}</h2>
    </body>
</html>
```

- urls.py
```py
from django.contrib import admin
from django.urls import path

from myapp.views import sayhello,hello2,hello3


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello2/<str:username>/', hello2),
    path('hello3/<str:username>/', hello3),
]

```


- views.py
```py
from django.shortcuts import render #利用render函式呼叫hello3.html

from django.http import HttpResponse

from datetime import datetime


# Create your views here.
def sayhello(request):
    return HttpResponse("Hello Pizza !!!")



def hello2(request,username):
    return HttpResponse("Hello "+ username)



def hello3(request,username):
    now = datetime.now()
	
    return render(request,"hello3.html",locals())
```
<解說> <br>
render第一個參數request:傳遞GET或POST送出的資料。<br>
第二個參數為模板名稱。<br>
第三個參數local()表示要傳遞所有區域變數。


![](https://images2.imgbox.com/25/cb/TX1FBIxW_o.png)






### 4-6. 加入static靜態檔案

通常會分別在static目錄下，在建立image、css、javasript子目錄。


- hello4.html :
```{% load static %}```:宣告使用靜態檔案

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>顯示圖片模版</title>
        {% load static %}
        <link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
    </head>
    
    
    <body>
        <img src="{% static 'images/a.png' %}" alt="Welcome" width="32" height="32" />
        
        <span class="info">歡迎光臨: {{username}} </span>
                     
        <h2>現在時間: {{now}}</h2>
    </body>
</html>

```




- urls.py
```py
from django.contrib import admin
from django.urls import path

from myapp.views import sayhello,hello2,hello3,hello4


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello2/<str:username>/', hello2),
    path('hello3/<str:username>/', hello3),
    path('hello4/<str:username>/', hello4),
]


```




- views.py
```py
from django.shortcuts import render

from django.http import HttpResponse

from datetime import datetime


# Create your views here.
def sayhello(request):
    return HttpResponse("Hello Pizza !!!")



def hello2(request,username):
    return HttpResponse("Hello "+ username)



def hello3(request,username):
    now = datetime.now()
    return render(request,"hello3.html",locals())



def hello4(request,username):
    now = datetime.now()
    return render(request,"hello4.html",locals())
```




- style.css
```css
.info{
    color:red;
    font-size: 1.5em;
}

```

```bash
(base) [cabie@centosclean images]$ pwd
/home/cabie/01_python/01_Django/002_django最強實戰/chapter_01/first_project/static/images

(base) [cabie@centosclean images]$ curl https://www.theladders.com/wp-content/uploads/Elon_Musk-800x450.jpg --output a.png
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 49112  100 49112    0     0  46907      0  0:00:01  0:00:01 --:--:-- 46907
(base) [cabie@centosclean images]$ ls
a.png

```




![](https://images2.imgbox.com/c2/73/IUBkHl6u_o.png)
