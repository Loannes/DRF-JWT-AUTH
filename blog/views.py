from .models import Post
from .serializers import BlogSerializer
from rest_framework import viewsets

from rest_framework import permissions

from .permissions import OnlyOwner

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

import pdb
		
# Blog의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class BlogViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, OnlyOwner]

    queryset = Post.objects.all()
    serializer_class = BlogSerializer
   
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)





