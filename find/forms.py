from django import forms
from tutorprofile.models import TutorProfile

class FindForm(forms.ModelForm):
    class Meta:
        model = TutorProfile
        fields = [
            'subject',
            'city'
        ]



class ScheduleForm(forms.Form):
    form = forms.CharField()
