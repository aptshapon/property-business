from django.db import models


# choices
property_type = (
    ('S', 'sale'),
    ('R', 'rent'),
)

class Property(models.Model):
    name = models.CharField(max_length=50)
    property_type = models.CharField(choices=property_type, max_length=10)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    price = models.PositiveIntegerField()
    area = models.PositiveIntegerField()
    beds_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property', null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Properties'

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'