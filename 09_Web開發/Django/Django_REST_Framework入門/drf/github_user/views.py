from django.shortcuts import render

from github_user.models import Github
from github_user.serializers import GithubSerializer

from rest_framework import viewsets


# Create your views here.
# 只要這樣寫就擁有 CRUD 的全部功能
class GithubViewset(viewsets.ModelViewSet):
    queryset = Github.objects.all()
    serializer_class = GithubSerializer

