from django.forms import ModelForm, Form
from django import forms
from .models import Product


class ProductForm(ModelForm):
    title = forms.CharField(initial="Title",
                            widget=forms.TextInput(
                                attrs={"placeholder": "Your title"}
                                                   )
                            )
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                                "placeholder": "Your description",
                                                "class": "my_class_new",
                                                "id": "my-id-for-textarea",
                                                "rows": 10,
                                                "cols": 100}
                                    )
                                  )
    price = forms.DecimalField(initial=1999.99)

    class Meta:
        model = Product
        fields = [
                    'title',
                    'description',
                    'price'
                  ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not "CFE" in title:
            raise forms.ValidationError("Not found CFE")
        return title


class RawProductForm(Form):
    title = forms.CharField(initial="Title",
                            widget=forms.TextInput(
                                attrs={"placeholder": "Your title"}
                                                   )
                            )
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                                "placeholder": "Your description",
                                                "class": "my_class_new",
                                                "id": "my-id-for-textarea",
                                                "rows": 10,
                                                "cols": 100}
                                    )
                                  )
    price = forms.DecimalField(initial=1999.99)



