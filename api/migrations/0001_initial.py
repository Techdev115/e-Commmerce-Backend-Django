from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(
            name='Utsav',
            email='utsav.patel.india@gmail.com',
            is_staff=True,
            is_superuser=True,
            phone='1234567890'
        )

        user.set_password('abc@1234')
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]