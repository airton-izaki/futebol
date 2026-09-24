from django.db import models


DIVISAO_CHOICES = [
    ('serie_a',   'Série A'),
    ('serie_b',   'Série B'),
    ('serie_c',   'Série C'),
    ('serie_d',   'Série D'),
    ('estadual',  'Estadual'),
    ('regional',  'Regional'),
    ('amador',    'Amador'),
]

ESTADO_CHOICES = [
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
    ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
    ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'),
    ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
]


class Clube(models.Model):
    nome            = models.CharField(max_length=100, verbose_name='Nome do Clube')
    sigla           = models.CharField(max_length=5,   verbose_name='Sigla')
    fundacao        = models.DateField(verbose_name='Data de Fundação')
    cidade          = models.CharField(max_length=100, verbose_name='Cidade')
    estado          = models.CharField(max_length=2, choices=ESTADO_CHOICES, verbose_name='Estado')
    estadio         = models.CharField(max_length=100, verbose_name='Estádio', blank=True)
    divisao         = models.CharField(max_length=20, choices=DIVISAO_CHOICES, verbose_name='Divisão')
    cor_primaria    = models.CharField(max_length=30, verbose_name='Cor Primária', blank=True)
    cor_secundaria  = models.CharField(max_length=30, verbose_name='Cor Secundária', blank=True)
    website         = models.URLField(verbose_name='Site', blank=True)
    escudo          = models.ImageField(upload_to='escudos/', verbose_name='Escudo', null=True, blank=True)
    descricao       = models.TextField(verbose_name='Descrição', blank=True)
    ativo           = models.BooleanField(default=True, verbose_name='Ativo')
    criado_em       = models.DateTimeField(auto_now_add=True)
    atualizado_em   = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = 'Clube'
        verbose_name_plural = 'Clubes'
        ordering            = ['nome']

    def __str__(self):
        return f'{self.nome} ({self.sigla})'
