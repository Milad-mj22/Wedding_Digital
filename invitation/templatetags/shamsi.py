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
    


@register.filter
def shamsi_date(value, arg=None):
    """
    Convert a Gregorian date to Shamsi (Jalali) date.
    
    Usage in template:
        {{ my_date|shamsi_date:"%Y / %m / %d" }}
        {{ my_date|shamsi_date:"%Y-%m-%d %H:%M" }}
        {{ my_date|shamsi_date }}
    
    Args:
        value: A datetime or date object
        arg: Format string (optional)
    
    Returns:
        Formatted Shamsi date string
    """
    if not value:
        return ''
    
    # If value is a string, try to parse it
    if isinstance(value, str):
        try:
            # Try common formats
            for fmt in ['%Y-%m-%d', '%Y-%m-%d %H:%M:%S', '%Y/%m/%d']:
                try:
                    value = datetime.datetime.strptime(value, fmt)
                    break
                except ValueError:
                    continue
            else:
                return value
        except Exception:
            return value
    
    # Handle timezone-aware datetime
    if timezone.is_aware(value):
        value = timezone.localtime(value)
    
    # Convert to Shamsi
    try:
        # If it's a date object (not datetime)
        if isinstance(value, datetime.date) and not isinstance(value, datetime.datetime):
            shamsi_date = jdatetime.date.fromgregorian(date=value)
        else:
            shamsi_date = jdatetime.datetime.fromgregorian(datetime=value)
        
        # Format the output
        if arg:
            # Convert format string (Django format to jdatetime format)
            # %Y -> %Y, %m -> %m, %d -> %d, %H -> %H, %M -> %M, %S -> %S
            return shamsi_date.strftime(arg)
        else:
            # Default format
            return shamsi_date.strftime("%Y/%m/%d")
            
    except Exception as e:
        # If conversion fails, return the original value
        return value
