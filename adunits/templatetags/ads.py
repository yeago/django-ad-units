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
        kwargs = {'name': name}
        try:
            ad_settings = Settings.objects.get(site=site)
            if ad_settings.active_vendor_id:
                kwargs.update({'vendor': ad_settings.active_vendor_id})
        except Settings.DoesNotExist:
            pass
        try:
            unit = Unit.objects.get(**kwargs)
        except Unit.DoesNotExist:
            return ''
        except Unit.MultipleObjectsReturned:
            return Unit.objects.filter(**kwargs)[0]  # Maybe transitional where you're setting up vendors
        tmpl = template.Template(unit.source)

    context.update({'context': context})
    return mark_safe(tmpl.render(Context(context)))


@register.simple_tag(takes_context=True)
def ad2(context, vendor, name):  # another take
    if getattr(settings, 'AD_SERVING_DISABLED', False):
        return ''

    kwargs = {'name': name, 'vendor': vendor}
    try:
        unit = Unit.objects.get(**kwargs)
    except Unit.DoesNotExist:
        return ''
    except Unit.MultipleObjectsReturned:
        return Unit.objects.filter(**kwargs)[0]  # Maybe transitional where you're setting up vendors
    tmpl = template.Template(unit.source)
    context.update({'context': context})
    return mark_safe(tmpl.render(Context(context)))
