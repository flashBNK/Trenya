from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.workout_list, name='workout_list'),
    path('<slug:goal_slug>/', views.workout_list,
         name='workout_list_by_goal'),
path('<int:id>/<slug:slug>', views.workout_detail,
         name='workout_detail')
]
