from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer


class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.get_published_posts()
    serializer_class = PostSerializer


class PostDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
