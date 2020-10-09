from rest_framework import serializers

from .models import RouterModel

class RouterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RouterModel
        fields = ('r_name','r_ip','r_type')