from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
        title = forms.CharField(label="New Title", widget=forms.TextInput(
            attrs={"placeholder": "Your Title"}

        ))
        description = forms.CharField(required=True,
                                      widget=forms.Textarea(attrs={
                                          "class": "my-class-textarea",
                                          "id": "my-id-textarea",
                                          "rows": 5,
                                          "cols": 30,
                                          "placeholder": "Your description"
                                      }))
        price = forms.DecimalField(initial=199.99)
        email = forms.EmailField()

        class Meta:
            model = Product
            fields = [
                    'title',
                    'description',
                    'price',
                 ]

        def clean_title(self, *args, **kwargs):
            title = self.cleaned_data.get("title")
            if not "CFE" in title:
                raise forms.ValidationError("This is not a valid title")
            return title

        def clean_email(self, *args, **kwargs):
            email = self.cleaned_data.get("email")
            if not email.endswith("edu"):
                raise forms.ValidationError("This is not a valid email")
            return email



class RawProductForm(forms.Form):
    title = forms.CharField(label='Title', initial="New Title", required=True,
                            widget=forms.TextInput(attrs={
                                "placeholder": "Your Title"
                            }))
    description = forms.CharField(required=True, initial="description",
                                  widget=forms.Textarea(attrs={
                                      "class": "my-class-textarea",
                                      "id": "my-id-textarea",
                                      "rows": 5,
                                      "cols": 10,
                                      "placeholder": "Your description"
                                  }))
    price = forms.DecimalField(initial=10.00,required=True)
