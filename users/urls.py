from django.urls import path
from . import views
from .views import UserListView

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', views.profile, name='profile'),
    path('analytics/', views.log_pomodoro, name='analytics'),
    path('leaderboard/', views.leader, name='leaderboard'),
    path('trainer/', UserListView.as_view(), name='trainers'),
    path('search/', views.search, name='user-search'),
    path('badge/<int:id>/', views.create_badge, name='new-badge'),
    path('badge/', views.badge, name='badge'),
    path('<int:pk>/', views.user_detail_view, name='user-detail'),
]
