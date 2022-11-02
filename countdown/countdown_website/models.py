from django.db import models


class Emails(models.Model):
    email = models.EmailField()
    reg_time = models.TextField()
    reg_name = models.TextField()
    reg_com = models.TextField()
    