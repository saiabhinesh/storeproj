from rest_framework import serializers
from .models import *
class productlistserializer(serializers.ModelSerializer):
	class Meta:
		model=productstable
		fields='__all__'
		lookup_field="pid"


class cartcreateserializer(serializers.ModelSerializer):
	cuserproducts = serializers.HyperlinkedIdentityField(
		view_name='productstable-detail',lookup_field='pid')
	class Meta:
		model=carttable
		exclude=['cuser']
##must change look up field in cart create taking id i.e., pk must change to pid
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