from django.db import models


class CyStat(models.Model):
    stat_dt = models.CharField(max_length=10)  # 日期
    cy_name = models.CharField(max_length=50)  # 国家名称
    confirm = models.IntegerField()  # 累计确诊
    dead = models.IntegerField()  # 累计死亡
    heal = models.IntegerField()  # 累计治愈
    today_confirm = models.IntegerField()  # 现有确诊
    today_new_confirm = models.IntegerField()  # 新增确诊


class ProvStat(models.Model):
    stat_dt = models.CharField(max_length=10)
    cy_name = models.CharField(max_length=50)
    prov_name = models.CharField(max_length=50)
    confirm = models.IntegerField()
    dead = models.IntegerField()
    heal = models.IntegerField()
    today_confirm = models.IntegerField()
    today_new_confirm = models.IntegerField()