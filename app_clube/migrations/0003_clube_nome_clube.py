from django.db import migrations, models


def copiar_nome_existente(apps, schema_editor):
    Clube = apps.get_model('app_clube', 'Clube')
    Clube.objects.filter(nome_clube__isnull=True).update(nome_clube=models.F('nome'))


class Migration(migrations.Migration):

    dependencies = [
        ('app_clube', '0002_remove_clube_capacidade_remove_clube_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clube',
            name='nome_clube',
            field=models.CharField(max_length=100, null=True, verbose_name='Nome do Clube'),
        ),
        migrations.RunPython(copiar_nome_existente, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='clube',
            name='nome_clube',
            field=models.CharField(max_length=100, verbose_name='Nome do Clube'),
        ),
    ]
