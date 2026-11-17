import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from users.models import CustomUser

email = os.environ.get('ADMIN_EMAIL', 'admin@example.com')
password = os.environ.get('ADMIN_PASSWORD', 'Admin@12345')

user, created = CustomUser.objects.get_or_create(email=email)
user.is_staff = True
user.is_superuser = True
user.is_active = True
user.set_password(password)
user.save()

if created:
    print(f"[SUCCESS] Created new superuser with email: {email}")
else:
    print(f"[SUCCESS] Updated user {email} as superuser with the new password.")

all_admins = list(CustomUser.objects.filter(is_superuser=True).values_list('email', flat=True))
print(f"[INFO] All superuser emails in database: {all_admins}")
