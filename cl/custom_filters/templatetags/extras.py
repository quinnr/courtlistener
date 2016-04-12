from django.utils.formats import date_format

from cl.people_db.models import GRANULARITY_DAY, GRANULARITY_MONTH, \
    GRANULARITY_YEAR

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def get_full_host(context, username=None, password=None):
    """Return the current URL with the correct protocol and port.

    No trailing slash.

    :param context: The template context that is passed in.
    :type context: RequestContext
    :param username: A HTTP Basic Auth username to show in the URL
    :type username: str
    :param password: A HTTP Basic Auth password to show in the URL
    :type password: str
    """
    if any([username, password]):
        assert all([username, password]), ("If a username is provided, a "
                                           "password must also be provided and "
                                           "vice versa.")
    r = context.get('request')
    if r is None:
        protocol = 'http'
        domain_and_port = 'courtlistener.com'
    else:
        protocol = 'https' if r.is_secure() else 'http'
        domain_and_port = r.get_host()

    return mark_safe("{protocol}://{username}{password}{domain_and_port}".format(
        protocol=protocol,
        username='' if username is None else username,
        password='' if password is None else ':' + password + '@',
        domain_and_port=domain_and_port,
    ))


@register.simple_tag(takes_context=False)
def granular_date(obj, field_name, granularity=None, iso=False,
                  default="Unknown"):
    """Return the date truncated according to its granularity.

    :param obj: The object to get the value from
    :param field_name: The attribute to be converted to a string.
    :param granularity: The granularity to perform. If None, we assume that
        getattr(obj, 'date_%s_field_name') will work.
    :param iso: Whether to return an iso8601 date or a human readable one.
    :return: A string representation of the date.
    """
    d = getattr(obj, field_name)
    if granularity is None:
        date_parts = field_name.split('_')
        granularity = getattr(obj, "%s_granularity_%s" % (date_parts[0],
                                                          date_parts[1]))

    if not d:
        return default
    if iso is False:
        if granularity == GRANULARITY_DAY:
            return date_format(d, format='F j, Y')
        elif granularity == GRANULARITY_MONTH:
            return date_format(d, format='F, Y')
        elif granularity == GRANULARITY_YEAR:
            return date_format(d, format='Y')
    else:
        if granularity == GRANULARITY_DAY:
            return date_format(d, format='Y-m-d')
        elif granularity == GRANULARITY_MONTH:
            return date_format(d, format='Y-m')
        elif granularity == GRANULARITY_YEAR:
            return date_format(d, format='Y')
