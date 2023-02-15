from rest_framework import status
from rest_framework.response import Response
from core.utils.messages.commonMessages import *
from core.utils.messages.userMessages import *
from core.models import User
from core.serializers import CreateUpdateUserSerializer , GetUserSerializer
from core.producer import publish
from .userBaseService import UserBaseService

class UserService(UserBaseService):
	""" Create, Update, Get, Delete and Get list of user."""

	def __init__(self):
		pass

	def get_all(self, request, format=None):
		"""Return all the existing users."""
		user = User.objects.all()
		serializer = GetUserSerializer(user, many=True)
		return ({"data": serializer.data, "code": status.HTTP_200_OK, "message": OK})

	def create(self, request, format=None):
		"""Create new user."""
		serializer = CreateUpdateUserSerializer(data=request.data)
		if serializer.is_valid ():
			serializer.save ()
			publish('user_created', serializer.data)
			return ({"data": serializer.data, "code": status.HTTP_201_CREATED, "message": USER_CREATED})
		return ({"data": serializer.errors, "code": status.HTTP_400_BAD_REQUEST, "message": BAD_REQUEST})

	def retrieve(self, request, pk, format=None):
		"""Get a user."""
		try:
			user = User.objects.get(id=pk)
			serializer = GetUserSerializer(user)
			return ({"data": serializer.data, "code": status.HTTP_200_OK, "message": OK})
		except:
			return ({"data": None, "code": status.HTTP_400_BAD_REQUEST, "message": RECORD_NOT_FOUND})

	def update(self, request, pk, format=None):
		"""Update user detail."""
		data = request.data
		try:
			user = User.objects.get(id=pk)
			serializer = CreateUpdateUserSerializer(user, data=data, partial=True)
			if serializer.is_valid ():
				serializer.save ()
				publish('user_updated', serializer.data)
				return ({"data": None, "code": status.HTTP_200_OK,"message":USER_DETAIL_UPDATED})
			else:
				return ({"data": serializer.errors, "code": status.HTTP_400_BAD_REQUEST,"message":BAD_REQUEST})
		except User.DoesNotExist:
			return({"data":None, "code":status.HTTP_204_NO_CONTENT, "message":RECORD_NOT_FOUND})

	def delete(self, request, pk, format=None):
		"""Delete user."""
		try:
			user = User.objects.get(id=pk)
			user.delete()
			publish('user_deleted', pk)
			return({"data":None, "code":status.HTTP_200_OK, "message":USER_DELETED})
		except User.DoesNotExist:
			return({"data":None, "code":status.HTTP_204_NO_CONTENT, "message":RECORD_NOT_FOUND})
