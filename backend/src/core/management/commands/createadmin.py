import django.contrib.auth.models as auth_models
import django.core.management.base
from django.utils.translation import gettext_lazy as _

__all__ = []


class Command(django.core.management.base.BaseCommand):
    def handle(self, *args, **options):
        admin_exists = auth_models.User.objects.filter(
            username="admin",
        ).exists()

        if not admin_exists:
            auth_models.User.objects.create_superuser(
                "admin",
                None,
                "admin",
            )
            self.stdout.write(
                self.style.SUCCESS(_("Суперпользователь успешно создан.")),
            )
        else:
            self.stdout.write(
                self.style.WARNING(_("Суперпользователь уже существует.")),
            )
