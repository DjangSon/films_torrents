from django.db import models


class IpList(models.Model):
    ip_address = models.CharField(max_length=15)
    port = models.CharField(max_length=6)
    type = models.CharField(max_length=6)
    server_address = models.CharField(max_length=20, null=True)
    survive_flag = models.IntegerField(max_length=1, default=1)
    survive_date = models.DateTimeField(null=True)
    save_date = models.DateTimeField()
