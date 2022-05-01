from rest_framework import viewsets
from rest_framework import permissions

from tests.models import Test, UserResults
from .serializers import TestSerializer, ResultsSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticated]


class ResultsViewSet(viewsets.ModelViewSet):
    queryset = UserResults.objects.all()
    serializer_class = ResultsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserResults.objects.filter(user=self.request.user)
