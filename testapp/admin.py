from django.contrib import admin

from testapp.models import *

# Register your models here.
admin.site.register(Users),
admin.site.register(Resource),
admin.site.register(UserToken),