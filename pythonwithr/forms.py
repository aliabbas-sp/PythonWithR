from django import forms
from runr.models import Rscript


class RscriptForm(forms.ModelForm):
    Rscript_code = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control',
               'style': 'height: 200px;'
               }
    ), label="")

    class Meta:
        model = Rscript
        fields = "__all__"
