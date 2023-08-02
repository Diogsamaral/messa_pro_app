from django.shortcuts import render, redirect
from .models import Pessoa
from django.shortcuts import render, get_object_or_404


def buscar_pessoas(request):
    if 'query' in request.GET:
        query = request.GET['query']
        resultados = Pessoa.objects.filter(nome__icontains=query)
    else:
        resultados = None

    return render(request, 'buscar.html', {'resultados': resultados})

def home(request):
    return render(request, 'home.html')



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
            comp_calca=comp_calca
        )
        pessoa.save()

        return redirect('cadastro-pessoa')  # Redireciona para uma página de sucesso após o cadastro

    return render(request, 'cadastrar-pessoa.html')

    


def exibir_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    return render(request, 'exibir_pessoa.html', {'pessoa': pessoa})



def todas_pessoas(request):
    # Consulta o banco de dados e obtém todos os registros do modelo MeuModelo
    todos_os_registros = Pessoa.objects.all()
    
    # Passe os registros para o template usando um dicionário
    context = {
        'registros': todos_os_registros,
    }
    
    # Renderiza o template com os dados e retorna a resposta HTTP
    return render(request, 'todas-pessoas.html', context)

