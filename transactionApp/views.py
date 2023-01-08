from django.shortcuts import render
from .serializers import transactionSerializer
from .models import transaction
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from .constants import page_size
from .serializers import transactionSerializer, TransactionSearchSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db.models import Q

# Create your views here.
class transactionView(UpdateAPIView, PageNumberPagination):
  serializer_class = transactionSerializer
  http_method_names = ["get"]

  def get(self, request, *args, **kwargs):
    paginator = PageNumberPagination()
    paginator.page_size = page_size

    transaction_obj = transaction.objects.all()
    result_page = paginator.paginate_queryset(transaction_obj, request)
    transactionResult_obj = self.serializer_class(result_page, many=True)

    return paginator.get_paginated_response(transactionResult_obj.data)


class transactionSearchView(UpdateAPIView, PageNumberPagination):
  permission_classes = (AllowAny,)
  serializer_class = TransactionSearchSerializer
  http_method_names = ["post"]

  def post(self, request, *args, **kwargs):
    paginator = PageNumberPagination()
    paginator.page_size = page_size

    serch_Item = request.data.get('searchField')
    if serch_Item == "":
      transaction_obj = transaction.objects.all()
    else:
      query = Q()
      query = Q(date__icontains=serch_Item) | Q(gross_amount__icontains=serch_Item) | Q(status__icontains=serch_Item) | Q(customer__icontains=serch_Item) | Q(swifter_id__icontains=serch_Item) | Q(external_id__icontains=serch_Item) | Q(source__icontains=serch_Item)
      transaction_obj = transaction.objects.filter(query).all()
    
    result_page = paginator.paginate_queryset(transaction_obj, request)
    transactionResult_obj = transactionSerializer(result_page, many=True)

    return paginator.get_paginated_response(transactionResult_obj.data)

def index(request):
  return render(request, 'index.html')
