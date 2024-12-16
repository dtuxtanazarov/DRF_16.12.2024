from rest_framework.serializers import ModelSerializer
from News.models import New


class New_serializer(ModelSerializer):
    class Meta:
        model = New
        fields = ['category','region','title','text','image','date','author']
