from django.db import models
from django.contrib.auth.models import User


class Store(models.Model):
    '''
    店铺数据模型
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='static/images/store/', default='static/images/store/store.jpg')
    status = models.IntegerField(default=0)# 0正常 1关闭 2删除 其他~永久删除
    intro = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
