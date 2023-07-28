from django import forms
from .models import Drop, Dropdown,Down,Dependent

class DropForm(forms.ModelForm):
    class Meta:
        model=Dependent
        fields=['name','birthdate','age','gender','number','mail','address','district','branch','account','credit','debit','cheque']
    def __init__(self, **kwargs):
        super(DropForm,self).__init__(**kwargs)
        self.fields["branch"].queryset=Dropdown.objects.none()

        if 'district' in self.data:
            try:
                district_id=int(self.data.get('district'))
                self.fields['branch'].queryset=Dropdown.objects.filter(district_id=district_id).order_by('name')
            except(ValueError,TypeError):
                pass
        elif self.instance.pk:
            self.fields['branch'].queryset=self.instance.district_set.order_by('name')


