from .models import Post
from .serializers import BlogSerializer
from rest_framework import viewsets

from rest_framework import permissions

from .permissions import OnlyOwner

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
		
from django.db.models import Q

# Blog의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class BlogViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, OnlyOwner]

    queryset = Post.objects.all()
    serializer_class = BlogSerializer
   
    def get_queryset(self):
        search_text = self.request.query_params.get('search_text', '')
        start_date = self.request.query_params.get('start_date', '')
        end_date = self.request.query_params.get('end_date', '')

        qs = super().get_queryset()

        if search_text:
            # qs = qs.filter(title__icontains=search_text)
            qs = qs.filter( Q(title__icontains=search_text) | Q(body__icontains=search_text) )

        if start_date and end_date:
            qs = qs.filter(created_at__range=[start_date, end_date])

        return qs.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)





