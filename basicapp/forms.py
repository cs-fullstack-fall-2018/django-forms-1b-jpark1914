from django import forms


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    confirmEmail = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    url = forms.URLField()

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        confirmEmail = cleaned_data.get('confirmEmail')
        if email != confirmEmail:
            print("Validation Failed")
            raise forms.ValidationError("These emails do not match")

        text = cleaned_data.get('text')
        text_num = len(text.split())
        if text_num < 3:
            print("Not enough words typed")
            raise forms.ValidationError("Not enough words typed")

        return cleaned_data