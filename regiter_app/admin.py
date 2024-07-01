from django.contrib import admin
from .models import UserInformation,ClassUser,RegionUser
# Register your models here.


admin.site.register(UserInformation)
admin.site.register(ClassUser)
admin.site.register(RegionUser)
