from django.db import models


class Organization(models.Model):
    business_name = models.CharField(max_length=256, blank=True, unique=True)
    associated_name_type = models.CharField(max_length=256, blank=True)
    entity_type = models.CharField(max_length=256, blank=True)
    nonprofit_type = models.CharField(max_length=256, blank=True)
    zip_code = models.IntegerField(null=True)
    address = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=128, blank=True)
    registry_number = models.IntegerField(null=True)
    registry_date = models.DateTimeField(null=True)
    state = models.CharField(max_length=256, blank=True)
    latitude = models.DecimalField(decimal_places=9, max_digits=15, null=True)
    longitude = models.DecimalField(decimal_places=9, max_digits=15, null=True)

    def __str__(self):
        return self.business_name

    def full_address(self):
        return '{}, {}, {}, {}'.format(self.address, self.city, self.state, self.zip_code)