from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_location_alter_ad_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='address',
        ),
        migrations.AlterField(
            model_name='ad',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.user'),
        ),
    ]
