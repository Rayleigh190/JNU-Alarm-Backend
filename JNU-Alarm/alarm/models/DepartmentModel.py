from django.db import models

## 학과
class Department(models.Model):
  architecture = models.BooleanField(default=False)  # 건축학부
  software_engineering = models.BooleanField(default=False)  # 소프트웨어공학과
  electric_engineering = models.BooleanField(default=False)  # 전자공학과

## 건축학부
class Architecture(models.Model):
  num = models.PositiveIntegerField()
  title = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

## 소프트웨어공학과
class SoftwareEngineering(models.Model):
  num = models.PositiveIntegerField()
  title = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title