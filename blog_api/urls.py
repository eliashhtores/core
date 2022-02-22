from django.urls import path
from .views import PostListAPIView, PostDetailAPIView

app_name = 'blog_api'

urlpatterns = [
    path('<int:pk>/', PostDetailAPIView.as_view(), name='detail'),

    path('', PostListAPIView.as_view(), name='list'),
]
