# Executing custom SQL directly

有時候  `Manager.raw()`  是不夠的，像是你可能需要 queries 沒有完全 map 到 models 的資料，<br>
或是執行 UPDATE, INSERT, or DELETE。<br>
當我們使用這個方法時，是完全的繞過 model ，直接 access database。


## 1. 範例

簡單說明一下這段 code，前端可以帶入 id 和 song (json格式)來**查詢**資料。

```sql
sqlite> select * from github_user where id = 5;
5|dudu|Banciao|2020-02-26 05:24:41.550629|2020-02-26 05:24:41.550673


sqlite> select * from github_user where user = "dudu";
5|dudu|Banciao|2020-02-26 05:24:41.550629|2020-02-26 05:24:41.550673
```


## 2. models.py

```py
from django.db import models


# Executing custom SQL directly使用的model
from collections import namedtuple
from django.db import connection




# Create your models here.

# 這裡我們設定Github User的Schema
class Github(models.Model):
    user = models.TextField()
    location = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True) #auto_now=Ture（在每次保存模型時將該字段設置為當前日期）
    created = models.DateTimeField(auto_now_add=True) #auto_now_add（僅設置模型首次創建時的日期）
    
    class Meta:
        db_table = "github_user"
        
        
        
        
#  Performing raw queries        
def fun_raw_sql_query(**kwargs):
    user = kwargs.get('user')
    if user:
        result = Github.objects.raw('SELECT * FROM github_user WHERE user = %s', [user])
    else:
        result = Github.objects.raw('SELECT * FROM github_user')
    return result








# Executing custom SQL directly

def namedtuplefetchall(cursor):
    # Return all rows from a cursor as a namedtuplet
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def fun_sql_cursor_update(**kwargs):
    user = kwargs.get('user')
    #print("=========================================")
    #print("models.py ===>  user")
    #print("=========================================")
    #pk = kwargs.get('pk')

    '''
    Note that if you want to include literal percent signs in the query,
    you have to double them in the case you are passing parameters:
    '''
    with connection.cursor() as cursor:
        #cursor.execute("UPDATE music SET user = %s WHERE id = %s", [user, pk])
        #cursor.execute("SELECT * FROM github_user WHERE id = %s", [pk])
        
        cursor.execute("SELECT * FROM github_user WHERE user = %s", [user])
        # result = cursor.fetchone()
        result = namedtuplefetchall(cursor)
    result = [
        {
            'id': r.id,
            'user': r.user,
            'location': r.location,
            'last_modify_date': r.last_modify_date,
            'created': r.created,
        }
        for r in result
    ]

    return result

```


### <補充> 

補充一下上面英文註解的說明，假設今天我們使用 like 搜尋，也就是會包含  `%`  的符號，

這時候我們必須重複  `%`  這個符號，也就是  `%%`，請看以下的例子，

假如我想執行這個 sql
```
SELECT * FROM music WHERE song like 'song%'
```
在  `cursor.execute`  中，必須多加上一個  `%`
```
cursor.execute("SELECT * FROM music WHERE song like 'song%%'", [])
```




## 3. views.py

由於這個方法是沒有 map 到 model，所以我們沒辦法進行序列化，<br>
這邊將直接回傳一個 dict 字典


```py
from django.shortcuts import render

from github_user.models import Github
from github_user.serializers import GithubSerializer

from rest_framework import viewsets


# Performing raw SQL queries時，用到的model
from github_user.models import Github
from github_user.models import fun_raw_sql_query,fun_sql_cursor_update
from github_user.serializers import GithubSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status


# Create your views here.
# 只要這樣寫就擁有 CRUD 的全部功能
class GithubViewset(viewsets.ModelViewSet):
    queryset = Github.objects.all()
    serializer_class = GithubSerializer
    
    
    
    
    # /api/github_user/raw_sql_query/
    @action(detail=False,methods=['get'],url_path='raw_sql_query')
    def raw_sql_query(self, request):
        user = request.query_params.get('user', None)
        user_info = fun_raw_sql_query(user=user)
        serializer = GithubSerializer(user_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    
    
    
    # /api/github_user/sql_cursor/
    @action(detail=False,methods=['post'],url_path='sql_cursor')
    def sql_cursor(self, request):
        user = request.data.get('user')
        
        #print("=========================================")
        #print("views.py:   "+str(user))
        #print("=========================================")

        user2 = fun_sql_cursor_update(user=user)
        return Response(user2, status=status.HTTP_200_OK)

        
        #if user:
        #    user = fun_sql_cursor_update(user=user)
        #    return Response(user, status=status.HTTP_200_OK)
            

   
```





## 4. Postman

![](https://images2.imgbox.com/17/90/2lkd1X4c_o.png)

