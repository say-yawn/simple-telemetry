from django.db import models

class AliasCreated(models.Model):
    method = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class AddonInteraction(models.Model):
    interface = models.CharField(max_length=50)
    completed_at = models.DateTimeField(auto_now_add=True)

class AddonOnboarding(models.Model):
    step = models.PositiveSmallIntegerField()
    length = models.DecimalField(max_digits=10, decimal_places=10)