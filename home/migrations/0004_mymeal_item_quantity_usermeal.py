# Generated by Django 4.0 on 2022-05-13 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('home', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyMeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mymeals', to='home.meal')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='UserMeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usermeals', to='home.mymeal')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
