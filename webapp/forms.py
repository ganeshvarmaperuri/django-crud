from django import forms
from .models import *

class emp_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(emp_form, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label='Select'