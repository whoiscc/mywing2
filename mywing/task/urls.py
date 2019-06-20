#

from django.urls import path
from mywing.task import views

urlpatterns = [
    path('acceptable', views.RecentUnacceptedTasksView.as_view()),
    path('<int:pk>', views.UpdateTaskView.as_view()),
    path('', views.CreateTaskView.as_view()),
    path('<int:pk>/accept', views.accept),
    path('<int:pk>/finish', views.finish),
    path('<int:pk>/complete', views.complete),
    path('<int:pk>/cancel', views.cancel),
]
