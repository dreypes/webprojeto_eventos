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
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do evento'}),
            'data': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'local': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o local do evento'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Forneça detalhes sobre o evento'}),
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


from django import forms
from .models import Convite, Evento, Usuario

class ConviteForm(forms.ModelForm):
    class Meta:
        model = Convite
        fields = ['evento', 'convidado']

    evento = forms.ModelChoiceField(queryset=Evento.objects.all(), empty_label="Selecione um evento")
    convidado = forms.ModelChoiceField(queryset=Usuario.objects.all(), empty_label="Selecione um convidado")