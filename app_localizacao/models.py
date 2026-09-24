from django.db import models

# ────────────────────────────────────────────────────────────────────────
# Unidade da Federalção 
# ────────────────────────────────────────────────────────────────────────
class RegiaoEnum(models.TextChoices):
    NORTE = 'N', 'Norte'
    NORDESTE = 'NE', 'Nordeste'
    CENTRO_OESTE = 'CO', 'Centro-Oeste'
    SUDESTE = 'SE', 'Sudeste'
    SUL = 'S', 'Sul'

class Estado(models.Model):    
    codigo_ibge = models.IntegerField(              
        primary_key = True,
        help_text   = "Código de 2 dígitos do IBGE (ex: 35 para SP, 53 para DF)"
    )
    uf = models.CharField(
        verbose_name = "UF",
        max_length   = 2,
        unique       = True,
        help_text    = "Sigla do estado (ex: SP, RJ)"
    )
    nome_estado = models.CharField(
        verbose_name = "Nome do Estado",
        max_length   = 50,
    )
    regiao_estado = models.CharField(
        verbose_name = "Região",
        max_length   = 2,
        choices      = RegiaoEnum.choices,
    )

    class Meta:
        verbose_name = "Estado / UF"
        verbose_name_plural = "Estados / UFs"
        ordering = ['nome_estado']
        db_table = 'Unidade_Federacao'

    def __str__(self):
        return f"{self.uf} - {self.nome_estado}"


# ────────────────────────────────────────────────────────────────────────
# Cidades 
# ────────────────────────────────────────────────────────────────────────
class Cidade(models.Model):
    codigo_ibge = models.IntegerField(
        primary_key = True,
        help_text = "Código IBGE de 7 dígitos (ex: 3550308 para São Paulo)"
    )
    nome_cidade = models.CharField(
        verbose_name = "Nome da Cidade",
        max_length   = 100,
    )
    estado = models.ForeignKey(
        Estado,
        verbose_name = "Estado / UF",        
        on_delete    = models.PROTECT,
        null         = True,
        blank        = True,
        related_name = 'cidades',
    )
    pais = models.CharField(
        verbose_name = "País",
        max_length   = 50,
        default      = "Brasil",
    )

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        db_table = 'Cidade'
        ordering = ['nome_cidade']

    def __str__(self):
        if self.estado:
            return f"{self.nome_cidade}/{self.estado.uf}"

        return f"{self.nome_cidade} ({self.pais})"




