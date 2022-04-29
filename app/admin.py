from django.contrib import admin
from .models import formregistration
from .models import userimage,reviews,Messages
#from .models import emplogin
# Register your models here.
admin.site.register(formregistration)
#admin.site.register(emplogin)
admin.site.register(userimage)
admin.site.register(reviews)

admin.site.register(Messages)