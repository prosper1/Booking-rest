from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.FloatField()
    available = models.BooleanField(default=True)
    notes = models.TextField()
    item_pic = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.png', verbose_name='itempic')

    def __str__(self):
        return self.name + str(self.quantity)

class Booking(models.Model):
    user_firstname = models.CharField(max_length=30)
    user_lastname = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=30)
    user_cell = models.CharField(max_length=30)
    id_number = models.CharField(max_length=30)
    adults = models.IntegerField(default=1)
    children = models.IntegerField(default=0)

    date = models.DateField()
    time_created = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item ,related_name="item_to_book",on_delete=True)

    def __str__(self):
        return self.name + self.user_cell

class Restaurant(models.Model):
    meal_name = models.CharField(max_length=30)
    price = models.FloatField(default=0.0)
    category = models.CharField(max_length=30)
    display_pic = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.png', verbose_name='foodpic')

    def __str__(self):
        return self.meal_name + self.category

class Media(models.Model):
    display_pic = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.png', verbose_name='gallerypic')
    
    def __str__(self):
        return self.display_pic.name

