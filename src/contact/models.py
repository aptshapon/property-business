from django.db import models


class ContactDetails(models.Model):
    # location = 
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return str(self.id)
    