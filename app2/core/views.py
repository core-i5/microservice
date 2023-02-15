from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from core.services.userService import UserService

user_service = UserService()

class GetUserListView(APIView):
    """create user List."""
    def get(self, request, format=None):
        result = user_service.get_all(request, format=None)
        return Response(result, status=result["code"])


class UpdateUserView(APIView):
    """Update User."""
    def put(self, request, pk, format=None):
        result = user_service.update(request, pk, format=None)
        return Response(result, status=result["code"])