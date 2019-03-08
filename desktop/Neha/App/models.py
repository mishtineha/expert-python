from django.db import models

class User(models.Model):
    Name = models.CharField(max_length = 30)
    Email = models.CharField(max_length = 50)
    credit = models.CharField(max_length = 20)
    contact_no = models.CharField(max_length = 20)
    city = models.CharField(max_length = 20)
    def __str__(self):
        return self.Name+'    '+self.Email+'  '+self.credit
class Transfer(models.Model):
    from_user_name = models.CharField(max_length = 30)
    to_user_name = models.CharField(max_length = 50)
    transfer_credit = models.CharField(max_length = 20)
    created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.from_user_name+'    '+self.to_user_name+'  '+self.transfer_credit
    
    
    


# Create your models here.
