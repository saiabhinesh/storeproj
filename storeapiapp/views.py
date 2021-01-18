from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import *
from .models import *
from rest_framework.pagination import LimitOffsetPagination
from .serializers import cartcreateserializer,productlistserializer,cartviewserializer
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

class mypagination(LimitOffsetPagination):
    default_limit=2
    max_limit=3
class productlist(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class=productlistserializer
    pagination_class=mypagination
    def get_queryset(self):
        return productstable.objects.all()
class cartcreate(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        ser = cartcreateserializer(data=request.data)
        if ser.is_valid():
            refinstanceset=productstable.objects.get(id=ser.data['cuserproducts'])
            s=carttable(
             	cuser=request.user.email,
                cuserproducts=refinstanceset,cqty=ser.data['cuserproducts'])
            s.save()
            return Response({'error':"false saved"})
        else:
            #ser.errors()
            return Response({'error':'True'})
class viewcart(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        userget=carttable.objects.filter(cuser=request.user.email)
        sercartview=cartviewserializer(userget,many=True)
        totalproducts=sercartview.data
        initialcartamount=0
        for eachproduct in totalproducts:
            initialcartamount=initialcartamount+eachproduct['eachproducttotal']
        totalproducts.append({'error':False,'cartvalue':initialcartamount})
        return Response(totalproducts)
    def patch(self,request):
        userget=carttable.objects.get(cuser=request.user.email,cuserproducts=request.data['cuserproducts'])
        sercartview=cartcreateserializer(userget,data=request.data,partial=True)
        if sercartview.is_valid():
            sercartview.save()
        return Response(sercartview.data)
