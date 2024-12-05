from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
#from django.contrib.auth.decorators import login_required
from .models import Evento, Usuario, Convite, Local
from .forms import EventoForm, UsuarioForm, ConviteForm, LocalForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import ConviteForm

#chama a pagina index
def index(request):

    return render(request,'app_eventos/index.html')

# Criar usuários
def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            # Passa os dados atualizados para o template
            usuarios = Usuario.objects.all()  # Atualiza a lista de usuários
            form = UsuarioForm()  # Cria um novo formulário vazio
            return render(request, 'app_eventos/usuario.html', {
                'form': form,
                'lista_usuarios': usuarios,
                'mensagem': 'Usuário criado com sucesso!',
            })
    else:
        form = UsuarioForm()

    # Caso não seja POST, renderiza normalmente a página com a lista de usuários
    usuarios = Usuario.objects.all()
    return render(request, 'app_eventos/usuario.html', {'form': form, 'lista_usuarios': usuarios})


# Listar usuários
#def listar_usuarios(request):
 ##  return render(request, 'app_eventos/usuario.html', {'lista_usuarios': usuarios})
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    form = UsuarioForm()  # Add this line to show the form
    return render(request, 'app_eventos/usuario.html', {'lista_usuarios': usuarios, 'form': form})



# Editar usuário
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário atualizado com sucesso!")
            return redirect('listar_usuarios')
        else:
            messages.error(request, "Erro ao atualizar o usuário. Verifique os dados fornecidos.")
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'app_eventos/usuario.html', {'form': form, 'usuario': usuario})


# Excluir usuário
def excluir_usuario(request, usuario_id):
    # Tenta encontrar o usuário pelo ID ou retorna um erro 404
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    # Exclui o usuário do banco de dados
    usuario.delete()
    
    # Recarrega a página com os dados atualizados
    usuarios = Usuario.objects.all()
    form = UsuarioForm()
    return render(request, 'app_eventos/usuario.html', {
        'form': form,
        'lista_usuarios': usuarios,
        'mensagem': 'Usuário excluído com sucesso!',
    })

#Criar convite
from django.shortcuts import render, redirect
from .models import Evento, Usuario, Convite
from .forms import ConviteForm

def criar_convite(request):
    if request.method == 'POST':
        form = ConviteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nome_da_url')  # Redireciona após salvar
    else:
        form = ConviteForm()

    return render(request, 'app_eventos/convite.html', {'form': form})

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
# Criar evento
def criar_evento(request):
    # Captura o ID do evento a ser editado (via GET)
    editar_id = request.GET.get('editar')
    evento = None

    if editar_id:
        evento = get_object_or_404(Evento, pk=editar_id)

    if request.method == "POST":
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento salvo com sucesso!')
            return redirect('listar_eventos')
        else:
            messages.error(request, 'Erro ao salvar o evento.')
    else:
        form = EventoForm(instance=evento)

    lista_eventos = Evento.objects.all().order_by('-data')
    return render(request, 'app_eventos/evento.html', {'form': form, 'lista_eventos': lista_eventos, 'evento': evento})


# Listar eventos
def listar_eventos(request):
    lista_eventos = Evento.objects.all().order_by('-data')  # Exibe todos os eventos
    return render(request, 'app_eventos/evento.html', {'lista_eventos': lista_eventos})

def editar_evento(request, evento_id):
    """
    View para editar um evento existente.
    """
    # Tenta encontrar o evento pelo ID ou retorna um erro 404
    evento = get_object_or_404(Evento, id=evento_id)
    
    if request.method == 'POST':
        # Atualiza o evento com os dados enviados no formulário
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()  # Salva as alterações no banco de dados
            return redirect('listar_eventos')  # Redireciona para a lista de eventos
    else:
        # Cria um formulário preenchido com os dados do evento
        form = EventoForm(instance=evento)
    
    # Renderiza o template de edição
    return render(request, 'app_eventos/editar_evento.html', {
        'form': form,
        'evento': evento
    })

# Excluir evento
def excluir_evento(request, evento_id):
    # Tenta encontrar o evento pelo ID ou retorna erro 404
    evento = get_object_or_404(Evento, id=evento_id)
    
    # Exclui o evento do banco de dados
    evento.delete()
    
    # Adiciona uma mensagem de sucesso
    messages.success(request, "Evento excluído com sucesso!")
    
    # Redireciona para a lista de eventos
    return redirect('listar_eventos')

def listar_eventos_convidado(request):
    """
    Lista os eventos para os quais o usuário atual foi convidado.
    """
    convites = Convite.objects.filter(convidado=request.user)
    eventos = [convite.evento for convite in convites]
    return render(request, 'app_eventos/eventos_convidado.html', {'eventos': eventos})
# Envio de convites
#@login_required
def listar_convites(request):
    """
    Exibe os convites e formulário para criação de novos convites.
    """
    eventos = Evento.objects.all()  # Listar eventos
    usuarios = User.objects.exclude(id=request.user.id)  # Excluir o usuário atual
    convites = Convite.objects.all()  # Listar todos os convites

    return render(request, 'app_eventos/convite.html', {
        'eventos': eventos,
        'usuarios': usuarios,
        'convites': convites,
    })

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ConviteForm

def criar_convite(request):
    """
    Cria um novo convite.
    """
    if request.method == 'POST':
        form = ConviteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Convite criado com sucesso!')
            return redirect('listar_convites')  # Redirecionar para a página de convites
        else:
            messages.error(request, 'Erro ao criar o convite.')
    else:
        form = ConviteForm()

    # Garantir que a função sempre retorne uma resposta HttpResponse
    return render(request, 'app_eventos/convite.html', {'form': form})

def alterar_status_convite(request, convite_id, novo_status):
    """
    Altera o status de um convite.
    """
    convite = get_object_or_404(Convite, id=convite_id)
    if novo_status in dict(Convite.STATUS_CONVITE).keys():
        convite.status = novo_status
        convite.save()

    return redirect('listar_convites')  # Redirecionar para a página de convites


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
