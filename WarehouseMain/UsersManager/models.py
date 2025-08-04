from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    ROLE_CHOICE=[
		('logistic_user_lvl1', 'Logistic User Level 1'),
        ('logistic_user_lvl2', 'Logistic User Level 2'),
        ('logistic_manager', 'Logistic Manager'),
        ('warehouse_user_lvl1', 'Warehouse User Level 1'),
        ('warehouse_user_lvl2', 'Warehouse User Level 2'),
        ('warehouse_manager', 'Warehouse Manager'),
        ('general_manager', 'General Manager'),
	]

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=30,choices=ROLE_CHOICE)
    id_number=models.IntegerField()
