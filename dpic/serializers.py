from rest_framework import serializers
from .models import Instapic

class InstapicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instapic
        fields = ('pic_user_name', 'downdate')