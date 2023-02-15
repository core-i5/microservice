from rest_framework import status
from rest_framework.response import Response
from core.utils.messages.commonMessages import *
from core.utils.messages.userMessages import *
from core.serializers import  GetUserSerializer, UpdateUserSerializer
from core.producer import publish
from core.models import User
from .userBaseService import UserBaseService
import requests
import pickle
from django.conf import settings
import os

class UserService(UserBaseService):
	""" Get list of user."""

	def __init__(self):
		pass

	def get_all(self, request, format=None):
		"""Return all the existing users."""
		user = User.objects.all()
		serializer = GetUserSerializer(user, many=True)
		return ({"data": serializer.data, "code": status.HTTP_200_OK, "message": OK})



	def update(self, request, pk, format=None):
		"""Update user detail."""
		try:
			user = User.objects.get(id=pk)
			file_path = os.path.join(settings.FILES_DIR, 'model.pkl')
			file=open(file_path,'rb')
			clf=pickle.load(file)
			file.close()
			fever = user.fever
			age = user.age
			bodypain = user.body_pain
			runnynose = user.runny_nose
			diffBreath = user.diff_breath
			inputFeatures=[fever,age,bodypain,runnynose,diffBreath]
			infprob=clf.predict([inputFeatures])[0]
			if infprob < 0:
				infprob=infprob * (-1)
			infprob=round(infprob*100,2)
			
			url="http://127.0.0.1:8000/app/user/update-user/"+str(pk)+"/"
			response = requests.put(url,json={"infection_prob" : infprob})
			if response.status_code == 200:
				publish('user_updated', pk)
			else:
				return ({"data": None, "code": status.HTTP_400_BAD_REQUEST,"message":BAD_REQUEST})
			return ({"data": None, "code": status.HTTP_200_OK, "message": OK})
		except:
			return({"data":None, "code":status.HTTP_204_NO_CONTENT, "message":RECORD_NOT_FOUND})
