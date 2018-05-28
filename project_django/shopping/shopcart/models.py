from django.db import models
from django.contrib.auth.models import User
import goods

# Create your models here.
class Shopcart(models.Model):
    '''
    购物车数据模型
    '''
    id = models.AutoField(primary_key=True)
    goods = models.ForeignKey(goods.models.Goods, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    subtoal = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)