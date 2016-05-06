from django.contrib.sites.models import Site


def create_initial_settings(*args, **kwargs):
    from adunits.models import Settings
    if Site.objects.count():
        Settings.objects.get_or_create(site=Site.objects.get_current())
