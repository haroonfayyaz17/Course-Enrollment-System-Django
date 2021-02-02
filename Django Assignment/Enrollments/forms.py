
from Courses.models import Course
from django import forms  
from Enrollments.models import Enrollment
class EnrollmentForm(forms.ModelForm):
    # course = forms.ModelChoiceField(queryset=Course.objects.all(),
    #                                 to_field_name = 'title',
    #                                 empty_label="Select Course")  
    class Meta:  
        model = Enrollment  
        fields = "__all__"
