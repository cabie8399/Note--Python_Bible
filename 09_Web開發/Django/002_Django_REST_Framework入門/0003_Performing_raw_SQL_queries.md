# Performing raw SQL queries

雖然 Django ORM 使用起來很棒，但有時某些情境或需求，ORM無法解決你的需求。此時Django有提供兩種方法，分別是 **Performing raw queries** 以及 **Executing custom SQL directly**。

使用時機差別在於:需要 queries 沒有完全 map 到 models 的資料，使用 **Executing custom SQL directly**。



## 1. 範例

假設我們想要使用Performing raw SQL queries，來時做一個API，是我們可以前端帶入user參數來查詢，若沒有帶任何user參數，則回傳全部。

- 確認資料庫有Pizza的資料
```sql
sqlite> SELECT * FROM github_user WHERE USER = "Pizza";
1|Pizza|Taipei|2020-02-21 20:21:58.042949|2020-02-21 20:21:58.042996
```


## 2. models.py

- 將透過 `Manager.raw()`這個方法
```py
from django.db import models

# Create your models here.

# 這裡我們設定Github User的Schema
class Github(models.Model):
    user = models.TextField()
    location = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True) #auto_now=Ture（在每次保存模型時將該字段設置為當前日期）
    created = models.DateTimeField(auto_now_add=True) #auto_now_add（僅設置模型首次創建時的日期）
    
    class Meta:
        db_table = "github_user"
        
        
        
        
        
def fun_raw_sql_query(**kwargs):
    user = kwargs.get('user')
    if user:
        result = Github.objects.raw('SELECT * FROM github_user WHERE user = %s', [user])
    else:
        result = Github.objects.raw('SELECT * FROM github_user')
    return result

```




## 3. views.py

- 因為版本問題，是使用```@action```，另外注意```detail=False```
- action參數
action装饰器可以接收两个参数：
    methods: 声明该action对应的请求方式，列表传递
    detail: 声明该action的路径是否与单一资源对应，及是否是xxx/<pk>/action方法名/ True 表示路径格式是xxx/<pk>/action方法名/ False 表示路径格式是xxx/action方法名/




```py
from django.shortcuts import render

from github_user.models import Github
from github_user.serializers import GithubSerializer

from rest_framework import viewsets


# Performing raw SQL queries時，用到的model
from github_user.models import Github
from github_user.models import fun_raw_sql_query
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


```



## 4. Postman

- http://192.168.1.108:8000/api/github_user/raw_sql_query/?user=Pizza

![](https://images2.imgbox.com/3b/32/XsiFmsvZ_o.png)

