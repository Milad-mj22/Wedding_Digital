import jdatetime
from django import template

register = template.Library()

@register.filter
def shamsi_date(value, fmt="%Y/%m/%d"):
    if not value:
        return ""
    shamsi = jdatetime.datetime.fromgregorian(datetime=value)
    return shamsi.strftime(fmt)