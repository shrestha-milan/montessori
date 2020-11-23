# Generated by Django 3.1.2 on 2020-11-21 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('assignment', '0003_auto_20201121_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentquestion',
            name='question_file',
            field=models.FileField(blank=True, null=True, upload_to='assignments/'),
        ),
        migrations.CreateModel(
            name='AssignmentSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_at', models.DateField(auto_now=True)),
                ('answer_text', models.CharField(blank=True, max_length=255, null=True)),
                ('answer_file', models.FileField(blank=True, null=True, upload_to='answers/')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.assignmentquestion')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
            ],
        ),
    ]
