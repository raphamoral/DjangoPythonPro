from django.db.transaction import non_atomic_requests
from django.shortcuts import render
from django.http import HttpResponse
from pypro.base.djangosdkstarkbank import webhook_extracting_and_sending_transfer ,sending_invoices_for_24_HRs
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_POST
import starkbank

#webhook = starkbank.webhook.create(
#    url=" https://6810-200-173-164-191.ngrok.io",
#    subscriptions=[
#        "invoice"
#
#    ]
#)
#print(webhook)
sending_invoices_for_24_HRs()
# Create your views here.
#@csrf_exempt
#@require_POST
#@non_atomic_requests
#def webhook_request(request):
#    jsondata = request.POST
#    data_v = json.loads(jsondata)
#    print(data_v)
    #webhook_extracting_and_sending_transfer(data_v)
#    return HttpResponse(200)
#csrfExemptMixin
@csrf_exempt
@require_http_methods([ "POST","GET"])
def webhook_request(request):
    jsondata = request.POST
    data_v = json.loads(jsondata)
    print(data_v)

    return HttpResponse(200)