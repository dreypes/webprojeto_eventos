from django import forms
from .models import Evento, Usuario, Convite, Local


class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['nome', 'endereco']
        labels = {
            'nome': 'Nome do Local',
            'endereco': 'Endereço Completo',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do local'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Endereço completo'}),
        }


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'data', 'local', 'descricao']
        labels = {
            'nome': 'Nome do Evento',
            'data': 'Data e Hora do Evento',
            'local': 'Local do Evento',
            'descricao': 'Descrição do Evento',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do evento'}),
            'data': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'local': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição detalhada'}),
        }


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario', 'cpf']
        labels = {
            'usuario': 'Usuário',
            'cpf': 'CPF',
        }
        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ConviteForm(forms.ModelForm):
    class Meta:
        model = Convite
        fields = ['evento', 'convidado', 'status']
        labels = {
            'evento': 'Evento',
            'convidado': 'Convidado',
            'status': 'Status do Convite',
        }
        widgets = {
            'evento': forms.Select(attrs={'class': 'form-control'}),
            'convidado': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
