from django.db import models


# Create your models here.
#실제로 데이터베이스에 반영이되는 클래스
#스프링, 엔티티 클래스와 동일함
# 클래스를 정의를 하면 자동으로 테이블을 생성해줌 ORM
class Burger(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)

    def __str__(self):
     return self.name
