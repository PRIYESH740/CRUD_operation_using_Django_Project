from django import forms
from .models import Employee
from django.core.exceptions import ValidationError

class Employeeform(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['fullname','mobile','emp_code','position']
        labels={
            'fullname':'Full Name',
            'mobile':"Mobile No.",
            'emp_code':'EMP. Code',
        }
    def __init__(self,*args,**kwargs):
        super(Employeeform,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label="Select"
        self.fields['emp_code'].required=False

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        qs = Employee.objects.filter(mobile=mobile)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)  # exclude current record
        if qs.exists():
            raise ValidationError("Mobile number already exists.")
        return mobile

    def clean_emp_code(self):
        emp_code = self.cleaned_data.get('emp_code')
        qs = Employee.objects.filter(emp_code=emp_code)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)  # exclude current record
        if emp_code and qs.exists():
            raise ValidationError("EMP. Code already exists.")
        return emp_code
