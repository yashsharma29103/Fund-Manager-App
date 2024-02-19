from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.
class CustomUser(AbstractUser):
    Role = (
        ('Admin' , 'Admin'),
        ('Manager' , 'Manager'),
        ('Employee' , 'Employee'),
    )
    userRole = models.CharField(choices=Role, default='Employee')

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }




class FundGroup(models.Model):
    """Class for handling Groups"""
    group_id = models.IntegerField(primary_key=True, auto_created=True)
    group_name = models.CharField(max_length=30, null=False, blank=False)
    group_description = models.TextField(max_length=100, null=True, default='', blank=True)

    def __str__(self):
        return self.group_name



class FundTransaction(models.Model):
    """Class for handling Transaction data"""

    CategoryChoice = (
        ('Birthday', 'Birthday'),
        ('Fine', 'Fine'),
        ('Personal_achievement', 'Personal_achievement'),
        ('others', 'others'),
    )
    StatusPending = (
        ('Pending', 'Pending'),
        ('Settled', 'Settled'),
    )
    StatusApproved = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Revoked', 'Revoked'),
    )

    transaction_id = models.IntegerField(primary_key=True, auto_created=True)
    category = models.CharField(null=False, blank=False, choices=CategoryChoice, default="Birthday")
    amount = models.IntegerField(null=False, blank=False)
    trans_desc = models.TextField(max_length=100)
    status_pending = models.CharField(choices=StatusPending, default='Pending')
    request_raised_by = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, related_name='raised')
    request_raised_against = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, related_name='against')
    status_revoke_approve = models.CharField(choices=StatusApproved, default='Pending')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_id




class Group_User_Details(models.Model):

    Role = (
        ("Simple","Simple"),
        ("Admin","Admin"),
    )
    RequestStatus = (
        ('Requested','Requested'),
        ('Approved','Approved')
    )
    g_id = models.ForeignKey(to=FundGroup, on_delete=models.CASCADE, null=False, blank=False)
    u_id = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, null=False, blank=False)
    joinRequest = models.CharField(choices=RequestStatus, default='Requested', null=False, blank=False)
    roles = models.CharField(choices=Role, default='Simple', null=False, blank=False)

    class Meta:
        UniqueConstraint(fields=['g_id','u_id'], name="composite_primary_key")