from rest_framework import serializers
from app.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('idx', 'name', 'create_dt', 'update_dt')