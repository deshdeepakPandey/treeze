from .models import transaction
from rest_framework import serializers


class transactionSerializer(serializers.ModelSerializer):
  date = serializers.SerializerMethodField("get_formated_date", allow_null=True)
  gross_amount = serializers.SerializerMethodField("get_gross_amount", allow_null=True)
  class Meta():
    model = transaction
    fields = "__all__"

  def get_gross_amount(self, obj):
    return f"${obj.gross_amount}"
  
  def get_formated_date(self, obj):
    return obj.date.strftime('%b %d %H:%M %p')


class TransactionSearchSerializer(serializers.ModelSerializer):
  searchField = serializers.CharField(write_only=True, required=True)

  class Meta:
    model = transaction
    fields = ('searchField',)
    extra_kwargs = {
      'searchField': {'required': True}
    }