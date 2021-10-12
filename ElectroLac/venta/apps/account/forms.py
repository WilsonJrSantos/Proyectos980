from datetime import datetime
from django.forms import *
from apps.account.models import User

class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus']=True

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'firs_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres'
                }
            ),
            'last_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese su apellido'
                }
            ),
            'username': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres'
                }
            ),
            'email': TextInput(
                attrs={
                    'placeholder': 'Ingrese su correo electronico'
                }
            ),
            'password': TextInput(
                attrs={
                    'placeholder': 'Ingrese su password'
                }
            ),
        }
        exclude = ['']

    #def #save(self, commit=True):
