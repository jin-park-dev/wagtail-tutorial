# Generated by Django 2.0.8 on 2018-08-24 06:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('blog', '0004_blogtagindexpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('username', models.CharField(max_length=30)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('surname', models.CharField(blank=True, max_length=30)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('profile', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.ProfilePage'),
        ),
    ]
