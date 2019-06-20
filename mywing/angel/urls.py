#

from django.urls import path
from mywing.angel import views


urlpatterns = [
    path('<int:pk>', views.RetrieveAngelView.as_view()),
    path('me', views.retrieve_self_view),
    path('cas-login', views.CASLoginView.as_view()),
    path('logout', views.logout),
]
