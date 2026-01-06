from ms_active_directory import ADDomain
from django.conf import settings

def get_ad_domain() -> ADDomain:
    return ADDomain(
        settings.AD_DOMAIN,
        settings.AD_USERNAME,
        settings.AD_PASSWORD,
        ldap_server=settings.AD_DC
    )