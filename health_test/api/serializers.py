from rest_framework import serializers

from tests.models import Test, UserResults


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'title', 'description')


class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResults
        fields = ('id', 'test', 'user', 'result')
