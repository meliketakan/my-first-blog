from django import forms
from .models import Formsayfasi

class ListForm(forms.ModelForm):
    class Meta:
        model=Formsayfasi
        fields=["name","surname","email","message1", "message2"]
        widgets={
            "name":forms.TextInput(attrs={"placeholder":"Adınız ","size":40}),
            "surname":forms.TextInput(attrs={"placeholder":"Soyadınız ","size":40}),
            "email":forms.EmailInput(attrs={"placeholder":"E-posta ", "maxlength":100, "size":40}),
            "message1":forms.TextInput(attrs={"placeholder":"Konu", "size":40}),
            "message2":forms.Textarea(attrs={"placeholder":"Mesajınız", "rows":4,"cols":42})
        }