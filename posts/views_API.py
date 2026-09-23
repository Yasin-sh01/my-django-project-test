from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer

from .models import Post


class PostListApi(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serialaiser = PostSerializer(posts, many = True)
        return Response(serialaiser.data)

class CreatePostApi(APIView):
    def post(self, request):
        serialaiser = PostSerializer(data = request.data)
        if serialaiser.is_valid():
            serialaiser.save()
            return Response(serialaiser.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serialaiser.errors, status = status.HTTP_400_BAD_REQUEST)

class PostDetailApi(APIView):
    def get(self, request, pk):
        post = Post.objects.get(pk = pk)
        serialaiser = PostSerializer(post)
        return Response(serialaiser.data)