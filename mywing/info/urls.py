#

from django.urls import path
from mywing.info import views


urlpatterns = [
    path('news', views.ListNewsView.as_view()),
    path('boards', views.ListBoardView.as_view()),
]
