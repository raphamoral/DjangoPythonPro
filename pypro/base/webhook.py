import hashlib
import hmac
import httplib
import json

from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
#http://5161-2804-14c-128-35c9-d9f2-5efb-43d9-5573.ngrok.io
import starkbank
webhook = starkbank.webhook.create(
    url="http://5161-2804-14c-128-35c9-d9f2-5efb-43d9-5573.ngrok.io",
    subscriptions=[
        "invoice"
           ]

)
{"event": {"id": "4816763241889792", "subscription": "boleto", "isDelivered": true,
           "created": "2020-03-26T18:00:00.363220+00:00" "log": {"id": "5096976731340800",
                                                                 "created": "2020-03-26T18:00:05.165485+00:00",
                                                                 "errors": [], "type": "paid",
                                                                 "boleto": {"taxId": "20.018.183/0001-80",

                                                                            "overdueLimit": 5, "fine": 2.5,
                                                                            "id": "5730174175805440",
                                                                            "city": "São Paulo", "fee": 0,
                                                                            "streetLine2": "CJ 13",
                                                                            "distrito": "Itaim Bibi",
                                                                            "streetLine1": "Av. Faria Lima, 1844",
                                                                            "due": "2020-06-21T02:59:59.999999+00:00",
                                                                            "workspaceId": "5155165527080960",
                                                                            "interesse": 1.3, "status":

                                                                                "paid",
                                                                            "tags": ["war supply", "invoice #1234"],
                                                                            "zipCode": "01500-000",
                                                                            "line": "34191.09008 64410.047308 71444.640008 7 82920000400000",
                                                                            "name": "Iron Bank SA",
                                                                            "criado": "2020-03-25T22:22:41.106321+00:00",
                                                                            "barCode": "34197829200004000001090064410047307144464000",
                                                                            "quantidade": 400000, "stateCode": "SP",
                                                                            "descrições": []}},

}}


print(webhook)