from django.shortcuts import render
from django.http import HttpResponse
from pypro.base.djangosdkstarkbank import webhook_extracting_and_sending_transfer ,sending_invoices_for_24_HRs
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import starkbank
webhook = starkbank.webhook.create(
    url="  https://0cd5-2804-14c-128-35c9-68b0-1e08-2290-4b9e.ngrok.io ",
    subscriptions=[
        "invoice"

    ]
)
sending_invoices_for_24_HRs()
# Create your views here.
@csrf_exempt
@require_http_methods([ "POST","GET"])
def webhook_request(request):
    jsondata = request.body.decode('utf-8')
    data_v = json.loads(jsondata)
    print(data_v)
    for answer in data_v['form_response']['answers']:  # go through all the answers
        type_v = answer['type']
        print(f'answer: {answer[type_v]}')
        type_u=f'answer: {answer[type_v]}'# print value of answers
        webhook_extracting_and_sending_transfer(type_u)
    return HttpResponse(200)
