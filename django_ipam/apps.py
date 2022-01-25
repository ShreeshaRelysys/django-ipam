from django.apps import AppConfig

from .compat import patch_ipaddress_lib


class DjangoIpamConfig(AppConfig):
    name = 'django_ipam'
    verbose_name = 'IPAM'

    def ready(self):
        patch_ipaddress_lib()
