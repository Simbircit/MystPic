from . import views
from django.urls import path
from .views import ShowProfilePageView, CreateProfilePageView
urlpatterns = [
    path('', views.main_page, name='mystpic'),
    path('catalog/', views.catalog, name='catalog'),
    path('register/', views.register, name='register'),
    path('register/', views.register, name='register'),
    path('logout/', views.exit_page, name='logout'),
    # path('profile/', ShowProfilePageView.as_view(), name='profile'),
    path('profile/<int:pk>/', ShowProfilePageView.as_view(), name='profile'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_user_profile'),
    path('createmystery/', views.create_mystery, name='createmystery'),
    path('mystery/<mystery_id>/', views.mysteries, name='mystery'),
    path('catalog/<category_name>/', views.catalog2, name='catalog')
]
