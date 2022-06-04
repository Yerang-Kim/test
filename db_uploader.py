import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projectA.settings")
django.setup()

from tests.models import Test

Test.objects.all().delete()

for title in ['하나', '둘', '셋']:
    Test.objects.create(
        title = title
    )