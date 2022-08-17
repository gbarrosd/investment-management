from rest_framework import viewsets
# from rest_framework.response import Response

from investment.api.serializers import OwnerSerializer, InvestmentSerializer, InvestmentNestedSerializer

from investment.models import Investments, Owner

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class InvestmentsViewSet(viewsets.ModelViewSet):
    queryset = Investments.objects.all()
    serializer_class = InvestmentSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = InvestmentNestedSerializer
        return super().retrieve(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        self.serializer_class = InvestmentNestedSerializer
        return super().list(request, *args, **kwargs)