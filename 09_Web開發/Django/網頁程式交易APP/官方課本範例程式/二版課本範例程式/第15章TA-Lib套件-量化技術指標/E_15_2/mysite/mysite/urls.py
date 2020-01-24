
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('E_14_2_Py/',views.E_14_2_Py),
    path('E_15_2/',views.E_15_2),
    path('E_15_2_Py/',views.E_15_2_Py),

]
