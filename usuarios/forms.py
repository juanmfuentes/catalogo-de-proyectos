from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import User, Administrador, Alumno, Empresa, Proyecto, ProyectoAlumno
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):

    username = forms.CharField(
        initial=False,
        widget=forms.HiddenInput(attrs={"class": "form-control"})
    )
    password1 = forms.CharField(
        required=False, initial=False, widget=forms.HiddenInput
    )
    password2 = forms.CharField(
        required=False, initial=False, widget=forms.HiddenInput
    )
    es_administrador = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )
    es_alumno = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )
    es_empresa = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'es_administrador', 'es_alumno', 'es_empresa')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'
        self.fields['es_administrador'].label = ''
        self.fields['es_alumno'].label = ''
        self.fields['es_empresa'].label = ''
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'



class RolForm(forms.Form):
    ROL_CHOICES = [
        ('alumno', 'Alumno'),
        ('empresa', 'Empresa'),
    ]
    rol = forms.ChoiceField(
        label='Rol', choices=ROL_CHOICES, widget=forms.RadioSelect)


class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ()


class AlumnoForm(forms.ModelForm):
    SEXO_CHOICES = [
        ('', 'Seleccione una opción'),
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    ]

    sexo = forms.ChoiceField(choices=SEXO_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Alumno
        fields = ('matricula', 'nombre', 'apellido_paterno', 'apellido_materno', 'sexo', 'correo_personal',
                  'correo_institucional', 'telefono', 'is_active', 'programa_educativo')
        widgets = {
            'is_active': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['matricula'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['apellido_paterno'].widget.attrs.update({'class': 'form-control'})
        self.fields['apellido_materno'].widget.attrs.update({'class': 'form-control'})
        self.fields['sexo'].widget.attrs.update({'class': 'form-select'})
        self.fields['correo_personal'].widget.attrs.update({'class': 'form-control'})
        self.fields['correo_institucional'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefono'].widget.attrs.update({'class': 'form-control'})
        self.fields['programa_educativo'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_active'].widget.attrs.update({'class': 'form-control', 'type': 'hidden'})

        # Eliminar la opción "-------" del campo "programa_educativo"
        self.fields['programa_educativo'].empty_label = "Selecciona una opción"


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = (
            'razon_social', 'rfc', 'telefono_empresa', 'titular', 'cargo', 'nombre_enlace', 'telefono_enlace',
            'correo_enlace', 'correo', 'is_active', 'calle', 'numero', 'colonia', 'ciudad', 'codigo_postal', 'entidad'
        )
        widgets = {
            'is_active': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['razon_social'].widget.attrs.update({'class': 'form-control'})
        self.fields['rfc'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefono_empresa'].widget.attrs.update({'class': 'form-control'})
        self.fields['titular'].widget.attrs.update({'class': 'form-control'})
        self.fields['cargo'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombre_enlace'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefono_enlace'].widget.attrs.update({'class': 'form-control'})
        self.fields['correo_enlace'].widget.attrs.update({'class': 'form-control'})
        self.fields['correo'].widget.attrs.update({'class': 'form-control'})
        self.fields['calle'].widget.attrs.update({'class': 'form-control'})
        self.fields['numero'].widget.attrs.update({'class': 'form-control'})
        self.fields['colonia'].widget.attrs.update({'class': 'form-control'})
        self.fields['ciudad'].widget.attrs.update({'class': 'form-control'})
        self.fields['codigo_postal'].widget.attrs.update({'class': 'form-control'})
        self.fields['entidad'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_active'].widget.attrs.update({'class': 'form-control', 'type': 'hidden'})



class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['periodo', 'año', 'vacantes', 'modalidad', 'nombre', 'objetivo',
                  'justificacion', 'asesor', 'id_programa_educativo', 'id_proceso', 'id_empresa']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['periodo'].widget.attrs.update({'class': 'form-control'})
        self.fields['año'].widget.attrs.update({'class': 'form-control'})
        self.fields['vacantes'].widget.attrs.update({'class': 'form-control'})
        self.fields['modalidad'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['objetivo'].widget.attrs.update({'class': 'form-control'})
        self.fields['justificacion'].widget.attrs.update({'class': 'form-control'})
        self.fields['asesor'].widget.attrs.update({'class': 'form-control'})
        
        self.fields['id_programa_educativo'].widget.attrs.update({'class': 'form-control'})
        self.fields['id_proceso'].widget.attrs.update({'class': 'form-control'})
        self.fields['id_empresa'].widget.attrs.update({'class': 'form-control'})

        self.fields['id_programa_educativo'].empty_label = 'Selecciona una opción'
        self.fields['id_proceso'].empty_label = 'Selecciona una opción'
        self.fields['id_empresa'].empty_label = 'Selecciona una opción'

        self.fields['periodo'].empty_label = 'Selecciona una opción'
        self.fields['modalidad'].empty_label = 'Selecciona una opción'

        
class ProyectoSeleccionadoForm(forms.ModelForm):
    class Meta:
        model = ProyectoAlumno
        fields = ['alumno', 'proyecto']


class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Contraseña actual',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password1 = forms.CharField(
        label='Nueva contraseña',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label='Confirmar contraseña',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
