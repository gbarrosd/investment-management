from rest_framework import permissions, viewsets, mixins
from rest_framework.response import Response

from investment.api.serializers import OwnerSerializer, InvestmentSerializer, InvestmentNestedSerializer

from investment.models import Investments, Owner

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class InvestmentsViewSet(viewsets.ModelViewSet):
    queryset = Investments.objects.all()
    serializer_class = InvestmentSerializer

    def get_custom_serializer(self, serializer_class, *args, **kwargs):
        # serializer_class = serializer_class
        kwargs.setdefault("context", self.get_serializer_context())
        return serializer_class(*args, **kwargs)


    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = InvestmentNestedSerializer
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print(serializer.data, 'identificador')
        return Response(serializer.data)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_custom_serializer(
            InvestmentNestedSerializer, queryset, many=True
        )
        return Response(serializer.data)


