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
        class Meta:
            model = Product
            fields = [
                    'title',
                    'description',
                    'price',
                 ]


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
