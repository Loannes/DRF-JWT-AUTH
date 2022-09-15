from rest_framework import permissions

from rest_framework import status
from datetime import datetime, timedelta
from rest_framework.exceptions import APIException

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # 읽기 권한 요청이 들어오면 허용
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # 요청자(request.user)가 객체(Blog)의 user와 동일한지 확인
        return obj.user == request.user



class OnlyOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # 요청자(request.user)가 객체(Blog)의 user와 동일한지 확인
        return obj.user == request.user





class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(detail=detail, code=code)

class example(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
		
        if request.method == 'GET':
            return True
        
        elif request.method != 'GET':
            return False    

        # 비로그인 유저이면서 그외 메소드일 경우 에러
        elif not user.is_authenticated and request.method in self.NEED_AUTH_METHODS:
            response ={
                    "detail": "서비스를 이용하기 위해 로그인 해주세요.",
                }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)
		
        # 로그인 유저이면서 가입일 3일 이내
        elif user.is_authenticated and user.join_date < (datetime.now() - timedelta(days=3)):
            return True
        
        # 관리자 계정
        elif user.is_admin:
            return True
        
        return False