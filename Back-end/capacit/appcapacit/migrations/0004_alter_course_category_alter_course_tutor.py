# Generated by Django 4.2.1 on 2024-05-15 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appcapacit', '0003_category_tutor_remove_course_teacher_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appcapacit.category'),
        ),
        migrations.AlterField(
            model_name='course',
            name='tutor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appcapacit.tutor'),
        ),
    ]
