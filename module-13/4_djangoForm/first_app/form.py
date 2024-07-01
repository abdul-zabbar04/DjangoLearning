from django import forms

class contactForm(forms.Form):
    name= forms.CharField(label='Enter your Name: ')
    file= forms.FileField()



    # email= forms.EmailField(label='Enter your Email: ')
    # age= forms.IntegerField()
    # check= forms.BooleanField()
    # weight= forms.FloatField()
    # salary= forms.DecimalField()
    # birtday= forms.DateField()
    # CHOICES=[('s', 'small'), ('m', 'Medium'), ('l', 'large')]
    # size= forms.ChoiceField(choices=CHOICES)
    # # MEALS= [('chicken', 'chicken'), ('beef', 'beef'), ('mutton', 'mutton')]
    # MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    # # meals= forms.MultipleChoiceField(choices=MEALS)
    # pizza = forms.MultipleChoiceField(choices=MEAL)

# class formValidation(forms.Form):
#     name= forms.CharField()
#     email= forms.EmailField()

#     # def clean_name(self):
#     #     valname= self.cleaned_data['name']
#     #     if len(valname)< 6:
#     #         raise forms.ValidationError('Enter a name with at least 6 character')
#     #     return valname
#     # def clean_email(self):
#     #     valemail= self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError('Email must have .com')
#     #     return valemail
    
#     # all the validation check in one function is below: 

#     def clean(self):
#         cleaned_data= super().clean()
#         valname= self.cleaned_data['name']
#         valemail= self.cleaned_data['email']
#         if len(valname)< 6:
#             raise forms.ValidationError('Enter a name with at least 6 character')
#         if '.com' not in valemail:
#             raise forms.ValidationError('Email must have .com')
        


#  form validation using django built-in validators:

from django.core import validators

# user defined validator create:
def minLen5(value):
    if len(value)<5:
        raise forms.ValidationError('You must enter at least 5 character')
class formValidation(forms.Form):
    name= forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(6, message='Enter a name with at least 6 characters')])
    email= forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter a valid Email')])
    age= forms.IntegerField(widget=forms.NumberInput, validators=[validators.MaxValueValidator(30, message='You crossed 30 years'), validators.MinValueValidator(18, message='Your Age is too short') ])
    file= forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['png', 'jpg'], message='Only png and jpg file is allowed')])

    text= forms.CharField(widget=forms.TextInput, validators=[minLen5])

    birthday= forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

# password validation form:

class passwordValidation(forms.Form):
    password= forms.CharField(widget=forms.PasswordInput)
    confirm_password= forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data= super().clean()
        val_pass= self.cleaned_data['password']
        val_confirm_pass= self.cleaned_data['confirm_password']

        if val_pass != val_confirm_pass:
            raise forms.ValidationError('Doesn\'t match the password')
