# invitation/templatetags/shamsi.py
import jdatetime
from django import template
from django.utils import timezone

register = template.Library()


@register.filter(name='to_shamsi')
def to_shamsi(value, fmt="%d %B %Y"):
    """
    تبدیل تاریخ میلادی به شمسی.
    استفاده: {{ invitation.wedding_date|to_shamsi }}
    """
    if not value:
        return ""

    # اگر datetime آگاه از تایم‌زون بود، به وقت محلی تبدیل کن
    if timezone.is_aware(value):
        value = timezone.localtime(value)

    try:
        j_date = jdatetime.datetime.fromgregorian(datetime=value)
    except Exception:
        return value

    return j_date.strftime(fmt)


@register.filter(name='to_shamsi_short')
def to_shamsi_short(value):
    return to_shamsi(value, fmt="%Y/%m/%d")