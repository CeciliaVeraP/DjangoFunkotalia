from django import forms
from .models import Funko

class FunkoForm(forms.ModelForm):
    class Meta:
        model = Funko
        fields = "__all__"