from django.shortcuts import render, redirect
from .models import Pessoa, Tecido, Aviamento
from django.shortcuts import render, get_object_or_404
from .forms import TecidoForm, AviamentoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, auth


def home(request):
    return render(request, 'home.html')


def registrar(request):
    if request.method == 'POST':
        primeiro_nome = request.POST['first_name']
        segundo_nome = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        senha = request.POST['password']
        confirmar_senha = request.POST['confirm_password']
        if senha==confirmar_senha:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username já existe')
                return redirect(registrar)
            
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email já registrado')
                return redirect(registrar)

            else:
                user = User.objects.create_user(username=username, password=senha, email=email, first_name=primeiro_nome, last_name=segundo_nome)
                user.set_password(senha) 
                user.save()
                print('Feito!')
                return redirect('login')

    else:
        print('Isso não é um metodo de post')
        return render(request, 'registrar.html')


@login_required
def buscar_pessoas(request):
    if 'query' in request.GET:
        query = request.GET['query']
        resultados = Pessoa.objects.filter(nome__icontains=query) | Pessoa.objects.filter(empresa__icontains=query)        
        aviamentos = Aviamento.objects.filter(artigo__icontains=query)
        tecidos = Tecido.objects.filter(artigo__icontains=query)
    else:
        resultados = None
        aviamentos = None
        tecidos = None

    return render(request, 'buscar.html', {'resultados': resultados, 'aviamentos': aviamentos, 'tecidos': tecidos})



@login_required
def cadastrar_pessoa(request):
    if request.method == 'POST':
        # Obtenha os dados do formulário
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        contato = request.POST.get('contato')
        empresa = request.POST.get('empresa')
        ombro_ombro = request.POST.get('ombro_ombro')
        torax_busto = request.POST.get('torax_busto')
        cintura_alta = request.POST.get('cintura_alta')
        cintura_baixa = request.POST.get('cintura_baixa')
        quadril = request.POST.get('quadril')
        altura_corpo = request.POST.get('altura_corpo')
        comp_camisa = request.POST.get('comp_camisa')
        comp_blazer = request.POST.get('comp_blazer')
        comp_vestido = request.POST.get('comp_vestido')
        comp_manga_curta = request.POST.get('comp_manga_curta')
        comp_manga_longa = request.POST.get('comp_manga_longa')
        larg_braco = request.POST.get('larg_braco')
        punho = request.POST.get('punho')
        larg_perna = request.POST.get('larg_perna')
        comp_saia = request.POST.get('comp_saia')
        comp_calca = request.POST.get('comp_calca')
        tamanho_blazer = request.POST.get('tamanho_blazer')
        tamanho_jaqueta = request.POST.get('tamanho_jaqueta')
        tamanho_calca_social = request.POST.get('tamanho_calca_social')
        tamanho_calca_cigarrete = request.POST.get('tamanho_calca_cigarrete')
        tamanho_calca_jeans = request.POST.get('tamanho_calca_jeans')
        tamanho_saia = request.POST.get('tamanho_saia')
        tamanho_gilet = request.POST.get('tamanho_gilet')
        tamanho_camisa_sem_manga = request.POST.get('tamanho_camisa_sem_manga')
        tamanho_camisa_manga_curta = request.POST.get('tamanho_camisa_manga_curta')
        tamanho_camisa_manga_longa = request.POST.get('tamanho_camisa_manga_longa')
        tamanho_camisa_manga_3_4 = request.POST.get('tamanho_camisa_manga_3_4')
        tamanho_blusa = request.POST.get('tamanho_blusa')
        tamanho_jaleco = request.POST.get('tamanho_jaleco')
        observacao = request.POST.get('observacao')

        # Salve os dados no banco de dados
        pessoa = Pessoa(
            nome=nome,
            email=email,
            contato=contato,
            empresa=empresa,
            ombro_ombro=ombro_ombro,
            torax_busto=torax_busto,
            cintura_alta=cintura_alta,
            cintura_baixa=cintura_baixa,
            quadril=quadril,
            altura_corpo=altura_corpo,
            comp_camisa=comp_camisa,
            comp_blazer=comp_blazer,
            comp_vestido=comp_vestido,
            comp_manga_curta=comp_manga_curta,
            comp_manga_longa=comp_manga_longa,
            larg_braco=larg_braco,
            punho=punho,
            larg_perna=larg_perna,
            comp_saia=comp_saia,
            comp_calca=comp_calca,
            tamanho_blazer=tamanho_blazer,
            tamanho_jaqueta=tamanho_jaqueta,
            tamanho_calca_social=tamanho_calca_social,
            tamanho_calca_cigarrete=tamanho_calca_cigarrete,
            tamanho_calca_jeans=tamanho_calca_jeans,
            tamanho_saia=tamanho_saia,
            tamanho_gilet=tamanho_gilet,
            tamanho_camisa_sem_manga=tamanho_camisa_sem_manga,
            tamanho_camisa_manga_curta=tamanho_camisa_manga_curta,
            tamanho_camisa_manga_longa=tamanho_camisa_manga_longa,
            tamanho_camisa_manga_3_4=tamanho_camisa_manga_3_4,
            tamanho_blusa=tamanho_blusa,
            tamanho_jaleco=tamanho_jaleco,
            observacao=observacao
        )
        pessoa.save()

        return redirect('cadastro-pessoa')  # Redireciona para uma página de sucesso após o cadastro

    return render(request, 'cadastrar-pessoa.html')

    

@login_required
def exibir_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    return render(request, 'exibir_pessoa.html', {'pessoa': pessoa})


@login_required
def todas_pessoas(request):
    # Consulta o banco de dados e obtém todos os registros do modelo MeuModelo
    todos_os_registros = Pessoa.objects.all()
    
    # Passe os registros para o template usando um dicionário
    context = {
        'registros': todos_os_registros,
    }
    
    # Renderiza o template com os dados e retorna a resposta HTTP
    return render(request, 'todas-pessoas.html', context)


@login_required
def novo_tecido(request):
    if request.method == 'POST':
        form = TecidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('novo_tecido'))  # Redireciona para a URL nomeada 'novo_tecido'
    else:
        form = TecidoForm()
    return render(request, 'novo_tecido.html', {'form': form})

@login_required
def novo_aviamento(request):
    if request.method == 'POST':
        form = AviamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('novo_aviamento'))  # Redireciona para a URL nomeada 'novo_tecido'
    else:
        form = AviamentoForm()
    return render(request, 'novo_aviamento.html', {'form': form})