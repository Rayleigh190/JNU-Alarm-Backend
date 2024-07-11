from django.db import models

class Shortcut(models.Model):
  name = models.CharField(max_length=10)
  ios_image_name = models.CharField(max_length=20)
  aos_image_name = models.CharField(max_length=20)
  color_code = models.CharField(max_length=6)
  link = models.URLField()
  is_available = models.BooleanField()
  is_webview = models.BooleanField()
  is_modal = models.BooleanField()

  def __str__(self):
    return self.name

class BannerAd(models.Model):
  name = models.CharField(max_length=50)
  image_url = models.URLField()
  direction_url = models.URLField(blank=True)
  is_available = models.BooleanField()
  expiry_date = models.DateField()