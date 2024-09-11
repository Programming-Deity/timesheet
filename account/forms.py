from crispy_forms.templatetags.crispy_forms_field import css_class
from django import forms
from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from sqlalchemy import column

alphanumeric_text = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50, validators=[alphanumeric_text], required=True)
    last_name = forms.CharField(label='Last Name', max_length=50, validators=[alphanumeric_text], required=True)
    username = forms.CharField(label='username', min_length=5, max_length=30, validators=[alphanumeric_text])
    employee_id = forms.CharField(label='Employee ID', max_length=8, validators=[
        RegexValidator(
            regex=r'^[0-9]{8}$',
            message='Employee ID must be exactly 8 digits.',
            code='invalid_employee_id'
        )
    ])
    email = forms.EmailField(label='Email', max_length=100, validators=[EmailValidator()], required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, validators=[validate_password], required=True)

    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, required=True)


    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 character long")
        return password

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Password do not match.')
        return password2

    # def __init__(self, *args, **kwargs):
    #     super(RegisterForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('First Name1', css_class='form-group col-md-6 mb-0'),
    #             Column('Last Name', css_class='form-group col-md-6 mb-0'),
    #             css_class='form-row'
    #         )
    #     )

























