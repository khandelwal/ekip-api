import json

from django.http import HttpResponse, HttpResponseBadRequest

from recordlocator import generator


# The maximum number of record locators that can be requested
MAX_REQUESTABLE = 50


def record_locators(request):
    """ View that generates at least one record locator, generating 'n' if
    specified through a query parameter. """

    num_locators = int(request.GET.get('n', 1))

    if num_locators > MAX_REQUESTABLE:
        return HttpResponseBadRequest(
            'Maximum of %s record locators can be requested' % MAX_REQUESTABLE)

    record_locators = generate_locators(num_locators)
    record_locators = save_locators(record_locators)

    data = {'record_locators': record_locators}
    response = json.dumps(data)

    return HttpResponse(response, content_type='application/json')


def save_locators(record_locators):
    locators = []
    for locator in record_locators:
        if not Ticket.objects.filter(record_locator=locator).exists():
            create_new_ticket(locator)

        #check against database 

        #if does not exist, save

        #else 
        
        #generate a new one

def generate_locators(n=1):
    """ Generate 'n' unique record locators. """

    record_locators = [generator.safe_generate() for r in range(0, n)]
    return record_locators
