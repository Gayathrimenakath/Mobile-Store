from django.db import models

# Create your models here.


class Mobile(models.Model):
    # elements for handling text
    model_name = models.CharField(max_length=300)
    brand_name = models.CharField(max_length=300)

    # integer field for battery capacity
    battery_capacity = models.IntegerField()
    quantity = models.IntegerField()

    # float field for Mobile Features
    front_cam = models.FloatField()
    back_cam = models.FloatField()
    ram = models.FloatField()
    screen_size = models.FloatField()
    price = models.FloatField()

    # Date is set manually
    release_data = models.DateTimeField(auto_now=False, auto_now_add=False)

    # images are uploaded into /media/mobiles/
    img = models.ImageField()

