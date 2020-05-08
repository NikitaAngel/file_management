from django import forms


class InputForm(forms.Form):
    inputFile = forms.FileField(
        label='Upload file to input folder',
    )
