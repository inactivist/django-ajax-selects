
from django.http import HttpResponse
from django.conf import settings
from ajax_select import get_lookup

def ajax_lookup(request,channel):
    """ this view supplies results for both foreign keys and many to many fields """
    
    query = request.GET.get('q', None)
    
    lookup_channel = get_lookup(channel)
    
    if query:
        instances = lookup_channel.get_query(query,request)
    else:
        instances = []

    results = []
    for item in instances:
        results.append(u"%s|%s|%s\n" % (item.pk,lookup_channel.format_item(item),lookup_channel.format_result(item)))
    return HttpResponse("\n".join(results))


