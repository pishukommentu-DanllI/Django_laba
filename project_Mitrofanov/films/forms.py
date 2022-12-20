from django import forms
from .models import Category


class Order_form(forms.Form):
    name = forms.CharField(max_length=50, label='Name')


    COICE_Category = [(i.id, i.name) for i in Category.objects.all()]


    Category = forms.MultipleChoiceField(choices=COICE_Category, label='Category')

    # date_made = models.DateTimeField(default=datetime.now, blank=True)

    date_show = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    acteru = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))

