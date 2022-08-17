from rest_framework import serializers
from django.db import transaction
from drf_writable_nested.serializers import WritableNestedModelSerializer

from investment.models import Investments, Owner

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = "__all__"
        depth = 1

class InvestmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Investments
        fields = "__all__"

class InvestmentNestedSerializer(serializers.ModelSerializer):
    # owner_info = OwnerSerializer(many=True)

    class Meta:
        model = Investments
        fields = "__all__"
        read_only_fields = ('owner_info',)

