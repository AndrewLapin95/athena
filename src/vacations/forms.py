from django import forms

from .models import Holiday

class HolidayCreateForm(forms.ModelForm):
    """
    Form to create a new holiday
    """
    class Meta:
        model = Holiday
        fields = [
            'title',
            'holiday_date',
            'week_day',
        ]
