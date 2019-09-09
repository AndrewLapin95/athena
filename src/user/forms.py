from django import forms

from .models import Employee, EmergencyContact, Department, Designation

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

class EmergencyContactCreateForm(forms.ModelForm):
    """
    Form to create a new emergency contact for a given user
    """
    class Meta:
        model = EmergencyContact
        fields = [
            'name',
            'relationship',
            'birthday',
            'phone_number',
        ]
