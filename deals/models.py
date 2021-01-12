from django.db import models


class Deal(models.Model):
    """Deal model"""
    product_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250, blank=True, default="unset")
    description = models.TextField(blank=True)
    store = models.CharField(max_length=250, blank=True)
    link = models.URLField()
    thumbnail_url = models.URLField(max_length=250, null=True, blank=True)
    original_price = models.FloatField(null=True, blank=True)
    discounted_price = models.FloatField(null=True, blank=True)
    coupon = models.CharField(max_length=20, null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True)
    last_update = models.DateTimeField(auto_now=True, blank=True)
