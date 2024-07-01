from django import forms
import datetime
class FormApi(forms.Form):
    name= forms.CharField(max_length=30, label='Enter Your Full Name:')
    contact_us= forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    data= forms.DateField(widget=forms.DateInput(attrs={'type':"date"}), initial=datetime.date.today)
    years= [2000, 2001, 2002, 2003, 2004]
    birthday= forms.DateField(widget=forms.SelectDateWidget(years=years))
    email= forms.EmailField(
        label='Enter your Email Address:'
    )
    check= forms.BooleanField(initial=True)
    courses= [('c', 'C'), ('c++', 'C++'), ('dsa','DSA'), ('mysql','MySQL'), ('python','Python'), ('oop', 'OOP'), ('django', 'Django')]
    choice= forms.ChoiceField(choices=courses)
    radios= [(1, 'A'), (2, 'B'), (3, 'C')]
    radio= forms.ChoiceField(choices=radios, widget=forms.RadioSelect)
    multiple_choice= forms.MultipleChoiceField(choices=courses)
    