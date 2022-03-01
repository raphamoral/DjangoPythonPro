import time

from django.db.transaction import non_atomic_requests
from django.shortcuts import render
from django.http import HttpResponse
from pypro.base.djangosdkstarkbank import  sending_invoices_for_24_hrs, parse_webhook
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_POST
import starkbank

#webhook = starkbank.webhook.create(
#    url="https://a006-200-173-168-111.ngrok.io/",
#    subscriptions=[
#        "invoice",]
#)
#print(webhook)


sending_invoices_for_24_hrs()

@csrf_exempt
@require_POST
def webhook(request):
    invoice_event = parse_webhook(request.body.decode(),request.headers['Digital-Signature'])
    print(type(invoice_event))
    time.sleep(2)

    return HttpResponse(200)