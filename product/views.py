from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .fillters import ProductsFilter
from .models import Product
from .serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination


# Create your views here.


@api_view(['GET'])
def get_all_product(request):
    # products = Product.objects.all()
    filterset = ProductsFilter(request.GET , queryset=Product.objects.all().order_by('id'))
    count = filterset.qs.count()
    resPage = 5
    paginator = PageNumberPagination()
    paginator.page_size = resPage
    
    queryset = paginator.paginate_queryset(filterset.qs , request)
    serializer = ProductSerializer(queryset ,many=True)
    return Response({"Products":serializer.data,"per page":resPage,"count":count})


@api_view(['GET'])
def get_product_by_id(request,pk):
    
    products = get_object_or_404(Product,id=pk)
    serializer = ProductSerializer(products,many=False)
    return Response({"Product":serializer.data})