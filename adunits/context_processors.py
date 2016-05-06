from django.contrib.sites.models import Site
from adunits.models import Settings


def settings(request):
    try:
        return {
            'adunit_settings': Settings.objects.get(
                site=Site.objects.get_current())
        }
    except Settings.DoesNotExist:
        return {}
