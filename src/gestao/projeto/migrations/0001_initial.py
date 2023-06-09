# Generated by Django 4.2 on 2023-04-09 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionario', '0001_initial'),
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('horas_para_concluir_projeto', models.IntegerField()),
                ('data_prazo_estimado', models.DateField()),
                ('horas_realizadas', models.IntegerField()),
                ('data_ultimo_calculo_horas', models.DateField()),
                ('departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='departamento.departamento')),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='funcionario.funcionario')),
            ],
            options={
                'unique_together': {('nome', 'departamento')},
            },
        ),
    ]
