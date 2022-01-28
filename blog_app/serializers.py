from rest_framework.serializers import ModelSerializer
from .models import Maqola

class MaqolaSerializer(ModelSerializer):
    class Meta:
        model = Maqola
        fields = '__all__'