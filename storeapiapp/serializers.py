from rest_framework import serializers
from .models import *
class productlistserializer(serializers.ModelSerializer):
	class Meta:
		model=productstable
		fields='__all__'
#in serializers
class cartcreateserializer(serializers.ModelSerializer):
	class Meta:
		model=carttable
		exclude=['cuser']
class cartviewserializer(serializers.ModelSerializer):
	cuserproducts=productlistserializer()
	eachproducttotal = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model=carttable
		fields='__all__'

	def get_eachproducttotal(self, obj):
		eachproductqty=obj.cqty
		eachproductprice=obj.cuserproducts.pprice
		totalofboth=eachproductqty*eachproductprice
		return totalofboth

#https://medium.com/better-programming/how-to-use-drf-serializers-effectively-dc58edc73998 check clear