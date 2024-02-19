from django.contrib import admin
from .models import CustomUser, FundGroup, FundTransaction, Group_User_Details

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(FundGroup)
admin.site.register(FundTransaction)
admin.site.register(Group_User_Details)