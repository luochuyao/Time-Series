from django.db import models

# Create your models here.
# global RR
#类名代表数据库表名，类里面的字段代表数据表中的字段name，数据类型有charfield（varchar）、DataField（datatime）
class Image(models.Model):
     headImg = models.FileField(upload_to='.')















