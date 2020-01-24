from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/',views.company),
    path('company/insert/',views.insert),
    path('do_insert/',views.do_insert),
    path('company/detail/<int:stockid>/',views.detail),
    path('company/update/<int:stockid>/',views.update),
    path('do_update/',views.do_update),
    path('company/delete/<int:stockid>/',views.delete),
    path('do_delete/',views.do_delete),

]
