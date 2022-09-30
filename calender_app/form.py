from decimal import Clamped
from django import forms
from .models import Calender



# class CalenderForm(forms.ModelForm):
#     date = forms.DateTimeField(
#         input_formats=['%d/%m/%Y %H:%M'],
#         widget=forms.DateTimeInput(attrs={
#             'class': 'form-control datetimepicker-input',
#             'data-target': '#datetimepicker1'
#         })
#     )
    
    
  


class DateInput(forms.DateInput):
    input_type = 'date'

class CalenderForm(forms.Form):
    datefield = forms.DateField(widget=DateInput)