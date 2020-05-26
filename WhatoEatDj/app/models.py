from django.db import models

# Create your models here.

class  Meishi(models.Model):
    id = models.AutoField(primary_key=True)  
    food_name = models.CharField(max_length=30) 
    food_author = models.CharField(max_length=8)
    food_money = models.FloatField() 
    food_star = models.CharField(max_length=10,default='normal') 

    def __str__(self): 
        return "<Meishi:{id=%s,food_name=%s,food_author=%s,food_money=%s,food_star=%s}>"\
               %(self.id,self.food_name,self.food_author,self.food_money,self.food_star)