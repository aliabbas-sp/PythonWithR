from django import forms
from runr.models import Rscript


class RscriptForm(forms.ModelForm):
    script = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                          'id': 'floatingTextarea',
                                                          'placeholder': 'input your R Script',
                                                          'style': 'height: 200px;'}), label="")

    df = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'form-control',
                                                         'name': 'df ',
                                                         'placeholder': 'df'}), label="")

    def __init__(self, *args, **kwargs):
        super(RscriptForm, self).__init__(*args, **kwargs)
        self.fields['df'].required = False
        self.fields['script'].required = False

    class Meta:
        model = Rscript
        fields = ('df', 'script')
