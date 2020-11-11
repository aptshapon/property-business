from django import forms
from .models import Reservation, Property


class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'


# class PropertySearch(forms.ModelFrom):
#     class Meta:
#         model = Property
#         # fields = ['address', 'property_type']