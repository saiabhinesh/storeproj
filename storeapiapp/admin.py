from django.contrib import admin

# Register your models here.
from .models import productstable,carttable
admin.site.register([productstable,carttable])