from rest_framework import serializers
from .models import User

class GetUserSerializer(serializers.ModelSerializer):
	"""This is for user list."""
	class Meta(object):
		model = User
		fields = "__all__"

class UpdateUserSerializer(serializers.ModelSerializer):
	"""This is to Update user."""
	class Meta(object):
		model = User
		fields = ['id', 'name', 'age', 'fever', 'body_pain', 'runny_nose', 'diff_breath']