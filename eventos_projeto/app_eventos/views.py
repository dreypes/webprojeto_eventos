from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
#from django.contrib.auth.decorators import login_required
from .models import Evento, Usuario, Convite, Local
from .forms import EventoForm, UsuarioForm, ConviteForm, LocalForm

#chama a pagina index
def index(request):

    return render(request,'app_eventos/index.html')


# Cadastro de locais
#@login_required
def criar_local(request, id=None):
    local = get_object_or_404(Local, pk=id) if id else None
    lista_locais = Local.objects.all().order_by('-id')

    if request.method == "POST":
        form = LocalForm(request.POST, instance=local)
        if form.is_valid():
            form.save()
            messages.success(request, 'Local salvo com sucesso!')
            return redirect('listar_locais')
        else:
            messages.error(request, 'Erro ao salvar o local.')
    else:
        form = LocalForm(instance=local)

    return render(request, 'app/form_local.html', {'form': form, 'lista_locais': lista_locais, 'local': local})


#@login_required
def listar_locais(request):
    lista_locais = Local.objects.all().order_by('-id')
    return render(request, 'app/listar_locais.html', {'lista_locais': lista_locais})


# Cadastro de eventos
#@login_required
def criar_evento(request, id=None):
    evento = get_object_or_404(Evento, pk=id) if id else None
    lista_eventos = Evento.objects.filter(criador=request.user).order_by('-data')

    if request.method == "POST":
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.criador = request.user
            evento.save()
            messages.success(request, 'Evento salvo com sucesso!')
            return redirect('listar_eventos')
        else:
            messages.error(request, 'Erro ao salvar o evento.')
    else:
        form = EventoForm(instance=evento)

    return render(request, 'app/form_evento.html', {'form': form, 'lista_eventos': lista_eventos, 'evento': evento})


#@login_required
def listar_eventos(request):
    lista_eventos = Evento.objects.filter(criador=request.user).order_by('-data')
    return render(request, 'app/listar_eventos.html', {'lista_eventos': lista_eventos})


# Envio de convites
#@login_required
def enviar_convite(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id, criador=request.user)
    if request.method == "POST":
        form = ConviteForm(request.POST)
        if form.is_valid():
            convite = form.save(commit=False)
            convite.evento = evento
            convite.save()
            messages.success(request, 'Convite enviado com sucesso!')
            return redirect('listar_convites', evento_id=evento.id)
        else:
            messages.error(request, 'Erro ao enviar o convite.')
    else:
        form = ConviteForm()

    return render(request, 'app/form_convite.html', {'form': form, 'evento': evento})


# Controle de presença
def gerenciar_convite(request, convite_id):
    convite = get_object_or_404(Convite, id=convite_id, convidado=request.user)
    if request.method == "POST":
        resposta = request.POST.get('resposta')
        if resposta == 'aceitar':
            convite.status = 'Aceito'
            convite.save()
            messages.success(request, 'Convite aceito.')
        elif resposta == 'recusar':
            convite.status = 'Recusado'
            convite.save()
            messages.success(request, 'Convite recusado.')
        else:
            messages.error(request, 'Resposta inválida.')

        return redirect('listar_eventos_convidado')

    return render(request, 'app/gerenciar_convite.html', {'convite': convite})


# Listar eventos do usuário
#@login_required
def listar_eventos_convidado(request):
    convites = Convite.objects.filter(convidado=request.user, status='Aceito').select_related('evento')
    return render(request, 'app/listar_eventos_convidado.html', {'convites': convites})


# Garantir restrição de acesso
#@login_required
def visualizar_evento(request, evento_id):
    convite = get_object_or_404(Convite, evento_id=evento_id, convidado=request.user, status='Aceito')
    return render(request, 'app/detalhes_evento.html', {'evento': convite.evento})

#@login_required
def excluir_local(request, id):
    try:
        local = Local.objects.get(pk=id)
        local.delete()
        messages.success(request, 'Local excluído com sucesso.')
    except Local.DoesNotExist:
        messages.error(request, 'O local especificado não foi encontrado.')
    return redirect('listar_locais')  # Ajuste o nome da URL para onde deseja redirecionar

def gestao_eventos(request):
    return render(request, 'app_eventos/gestao_eventos.html')
