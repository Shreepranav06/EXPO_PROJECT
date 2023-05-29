from django import forms
from .models import Email

class StudentForm(forms.Form):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        students = Email.objects.all()
        for student in students:
            self.fields[f"attendance_{Email.id}"] = forms.BooleanField(label=Email.student_name, required=True)

    def save(self):
        students = Email.objects.all()
        for student in students:
            attendance_value = self.cleaned_data[f"attendance_{Email.id}"]
            student.attendance = attendance_value
            student.save()