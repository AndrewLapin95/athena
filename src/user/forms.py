from django import forms

from .models import Employee

class EmployeeUpdateForm(forms.ModelForm):
    """
    Form to update employee's personal information
    """
    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'birthday',
            'gender',
            'address',
        ]
