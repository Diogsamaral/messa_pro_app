from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="O número de telefone deve estar no formato: '+999999999'."
    )
    contato = models.CharField(validators=[telefone_regex], max_length=16)
    empresa = models.CharField(max_length=110)
    ombro_ombro = models.CharField(max_length=10, null=True, blank=True)
    torax_busto = models.CharField(max_length=10, null=True, blank=True)
    cintura_alta = models.CharField(max_length=10, null=True, blank=True)
    cintura_baixa = models.CharField(max_length=10, null=True, blank=True)
    quadril = models.CharField(max_length=10, null=True, blank=True)
    altura_corpo = models.CharField(max_length=10, null=True, blank=True)
    comp_camisa = models.CharField(max_length=10, null=True, blank=True)
    comp_blazer = models.CharField(max_length=10, null=True, blank=True)
    comp_vestido = models.CharField(max_length=10, null=True, blank=True)
    comp_manga_curta = models.CharField(max_length=10, null=True, blank=True)
    comp_manga_longa = models.CharField(max_length=10, null=True, blank=True)
    larg_braco = models.CharField(max_length=10, null=True, blank=True)
    punho = models.CharField(max_length=10, null=True, blank=True)
    larg_perna = models.CharField(max_length=10, null=True, blank=True)
    comp_saia = models.CharField(max_length=10, null=True, blank=True)
    comp_calca = models.CharField(max_length=10, null=True, blank=True)
    tamanho_blazer = models.CharField(max_length=10, null=True, blank=True)
    tamanho_jaqueta = models.CharField(max_length=10, null=True, blank=True)
    tamanho_calca_social = models.CharField(max_length=10, null=True, blank=True)
    tamanho_calca_cigarrete = models.CharField(max_length=10, null=True, blank=True)
    tamanho_calca_jeans = models.CharField(max_length=10, null=True, blank=True)
    tamanho_saia = models.CharField(max_length=10, null=True, blank=True)
    tamanho_gilet = models.CharField(max_length=10, null=True, blank=True)
    tamanho_camisa_sem_manga = models.CharField(max_length=10, null=True, blank=True)
    tamanho_camisa_manga_curta = models.CharField(max_length=10, null=True, blank=True)
    tamanho_camisa_manga_longa = models.CharField(max_length=10, null=True, blank=True)
    tamanho_camisa_manga_3_4 = models.CharField(max_length=10, null=True, blank=True)
    tamanho_blusa = models.CharField(max_length=10, null=True, blank=True)
    tamanho_jaleco = models.CharField(max_length=10, null=True, blank=True)
    observacao = models.TextField(blank=True)


class Tecido(models.Model):
    artigo = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    fornecedor = models.CharField(max_length=100, blank=True)
    cliente = models.CharField(max_length=100, blank=True)
    metragem = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.artigo


class Aviamento(models.Model):
    artigo = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    fornecedor = models.CharField(max_length=100, blank=True)
    cliente = models.CharField(max_length=100, blank=True)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.artigo