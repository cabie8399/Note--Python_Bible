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
