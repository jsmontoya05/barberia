# Generated by Django 3.2.11 on 2022-06-05 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barbero',
            fields=[
                ('id_barbero', models.AutoField(primary_key=True, serialize=False)),
                ('detalle', models.CharField(max_length=200)),
                ('foto', models.ImageField(upload_to='app')),
            ],
        ),
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id_catalogo', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('0', 'Servicio'), ('1', 'Producto')], default='0', max_length=1)),
                ('nombre', models.CharField(max_length=30)),
                ('detalle', models.CharField(max_length=30)),
                ('valor', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('imagen', models.ImageField(upload_to='app')),
            ],
        ),
        migrations.CreateModel(
            name='Hora',
            fields=[
                ('id_hora', models.AutoField(primary_key=True, serialize=False)),
                ('hora', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('celular', models.CharField(max_length=15)),
                ('rol', models.CharField(choices=[('1', 'Administrador'), ('2', 'Barbero'), ('3', 'Cliente')], default='3', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('id_barbero', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.barbero')),
                ('id_catalogo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.catalogo')),
                ('id_hora', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.hora')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='barbero',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.usuario'),
        ),
    ]