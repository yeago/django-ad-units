from django import template
from django.template import Context
from django.utils.safestring import mark_safe

from django.conf import settings
from adunits.models import Unit

register = template.Library()


@register.simple_tag(takes_context=True)
def ad(context, name):
    if getattr(settings, 'AD_SERVING_DISABLED', False):
        return ''

    try:
        tmpl = template.loader.get_template('adunits/%s.html' % name)
    except template.TemplateDoesNotExist:
        try:
            unit = Unit.objects.get(name=name)
        except Unit.DoesNotExist:
            if settings.DEBUG:
                raise
            return ''
        tmpl = template.Template(unit.source)

    context.update({'context': context})
    return mark_safe(tmpl.render(Context(context)))
