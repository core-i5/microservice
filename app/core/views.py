from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from core.services.userService import UserService

user_service = UserService()

class CreateUserView(APIView):
    """create user."""
    def post(self, request, format=None):
        result = user_service.create(request, format=None)
        return Response(result, status=result["code"])

class GetUserListView(APIView):
    """create user List."""
    def get(self, request, format=None):
        result = user_service.get_all(request, format=None)
        return Response(result, status=result["code"])

class GetUserView(APIView):
    """Get User."""
    def get(self, request, pk, format=None):
        result = user_service.retrieve(request, pk, format=None)
        return Response(result, status=result["code"])

class UpdateUserView(APIView):
    """Update User."""
    def put(self, request, pk, format=None):
        result = user_service.update(request, pk, format=None)
        return Response(result, status=result["code"])

class DeleteUserView(APIView):
    """Delete User."""
    def delete(self, request, pk, format=None):
        result = user_service.delete(request, pk, format=None)
        return Response(result, status=result["code"])
