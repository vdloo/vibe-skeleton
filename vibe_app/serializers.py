from rest_framework import serializers
from vibe_app.models import SomeModel


class SomeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomeModel
        fields = ('id', 'some_field')
