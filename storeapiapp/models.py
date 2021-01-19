from django.db import models

class productstable(models.Model):
	pid=models.IntegerField()
	pname=models.CharField(max_length=100)
	pprice=models.IntegerField()
	pdescription=models.TextField()
	#created = models.DateTimeField(auto_now_add=True)
	#class Meta:
	#	ordering = ['created']
class carttable(models.Model):
	cuser=models.EmailField()
	cuserproducts=models.ForeignKey(productstable,on_delete=models.CASCADE)
	cqty=models.IntegerField()
class wishlisttable(models.Model):
	pass