from django.urls import path
from app import views
from rest_framework.authtoken import views as api_views

urlpatterns = [
    path('', views.BlogViews.as_view(), name='blog'),
    path('api-token-auth/', api_views.obtain_auth_token),

]
