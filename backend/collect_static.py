import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.management import call_command

call_command('collectstatic', interactive=False, verbosity=0)
print("✅ Static files collected successfully.")