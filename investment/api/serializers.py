from rest_framework import serializers

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
    owner = OwnerSerializer()

    class Meta:
        model = Investments
        fields = "__all__"