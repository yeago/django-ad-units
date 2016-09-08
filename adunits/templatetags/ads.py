from django import template
from django.template import Context
from django.utils.safestring import mark_safe
from django.contrib.sites.models import Site
from django.conf import settings
from adunits.models import Unit, Settings

register = template.Library()


@register.simple_tag(takes_context=True)
def ad(context, name):
    if getattr(settings, 'AD_SERVING_DISABLED', False):
        return ''

    try:
        tmpl = template.loader.get_template('adunits/%s.html' % name)
    except template.TemplateDoesNotExist:
        site = Site.objects.get_current()
        ad_settings = Settings.objects.get(site=site)
        kwargs = {'name': name}
        if ad_settings.active_vendor_id:
            kwargs.update({'vendor': ad_settings.active_vendor_id})
        try:
            unit = Unit.objects.get(**kwargs)
        except Unit.DoesNotExist:
            if settings.DEBUG:
                raise
            return ''
        tmpl = template.Template(unit.source)

    context.update({'context': context})
    return mark_safe(tmpl.render(Context(context)))
