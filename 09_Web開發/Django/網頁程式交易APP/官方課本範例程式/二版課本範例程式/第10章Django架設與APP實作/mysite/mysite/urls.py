from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
	path('admin/', admin.site.urls),
	path('gogo/', views.pylinkweb),  #新增這一列
	path('fv/', views.deposits),   #新增這一列 
	path('result/', views.result),   #新增這一列     
]
