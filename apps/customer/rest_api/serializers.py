from rest_framework import serializers
from apps.administrator.views import User


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

