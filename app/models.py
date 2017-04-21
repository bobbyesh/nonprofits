from django.db import models


class Organization(models.Model):
    business_name = models.CharField(max_length=256, blank=True)
    associated_name_type = models.CharField(max_length=256, blank=True)
    entity_type = models.CharField(max_length=256, blank=True)
    nonprofit_type = models.CharField(max_length=256, blank=True)
    zip_code = models.IntegerField(null=True)
    address = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=128, blank=True)
    registry_number = models.IntegerField(null=True)
    registry_date = models.DateTimeField(null=True)
    state = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.business_name