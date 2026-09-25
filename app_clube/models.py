from django.db import models


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

GESTAO_CHOICES = [
    ('ASSOCIATIVO', 'Associativo'),
    ('SAF', 'SAF'),
    ('PRIVADO', 'Privado'),
    ('HIBRIDO', 'Híbrido'),
]


class Clube(models.Model):
    nome            = models.CharField(max_length=100, verbose_name='Nome Oficial')
    nome_clube      = models.CharField(max_length=100, verbose_name='Nome do Clube')
    sigla           = models.CharField(max_length=5,   verbose_name='Sigla')
    gestao          = models.CharField(max_length=20, choices=GESTAO_CHOICES, default='ASSOCIATIVO', verbose_name='Modelo de Gestão')
    fundacao        = models.DateField(verbose_name='Data de Fundação')
    cidade          = models.CharField(max_length=100, verbose_name='Cidade')
    estado          = models.CharField(max_length=2, choices=ESTADO_CHOICES, verbose_name='Estado')
    estadio         = models.CharField(max_length=100, verbose_name='Estádio', blank=True)
    cor_primaria    = models.CharField(max_length=30, verbose_name='Cor Primária', blank=True)
    cor_secundaria  = models.CharField(max_length=30, verbose_name='Cor Secundária', blank=True)
    cor_terciaria   = models.CharField(max_length=30, verbose_name='Cor Terciária', blank=True)
    website         = models.URLField(verbose_name='Site', blank=True)
    escudo          = models.URLField(verbose_name='Link do Escudo', null=True, blank=True)
    descricao       = models.TextField(verbose_name='Descrição', blank=True)
    ativo           = models.BooleanField(default=True, verbose_name='Ativo')
    criado_em       = models.DateTimeField(auto_now_add=True)
    atualizado_em   = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = 'Clube'
        verbose_name_plural = 'Clubes'
        ordering            = ['nome']
        db_table            = 'Clube'

    def __str__(self):
        return f'{self.nome_clube} ({self.sigla})'
