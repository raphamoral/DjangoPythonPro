import starkbank
from datetime import datetime, timedelta
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import time
import names
from random import randint
import asyncio
private_key, public_key = starkbank.key.create("sample/destination/path")
private_key_content = """"
-----BEGIN EC PRIVATE KEY-----
MHQCAQEEIF7Jtu3zY5DjqiYz0A9yWo6TkUshPe1hQ51sWPSJCAjboAcGBSuBBAAK
oUQDQgAE5Z30Y6Bb2foc91j1sk0IivZ1a86ykANMrY4hUBXeKEqOgSRN6VJmACdA
9GweG8md6GId7mUGi7k+5UugjKjKxQ==
-----END EC PRIVATE KEY-----
"""

new_name = names.get_full_name()
current_time = f'{(datetime.now())}'
current_data_bank = current_time[0:9]
print(current_data_bank)
print(current_time)
new_avenue = f'Avenida {names.get_full_name()},{randint(0, 15000)}'
new_zip_code = f"{randint(0, 99999)}-{randint(0, 999)}"
new_tax_id = f'{randint(0, 999)}.{randint(0, 999)}.{randint(0, 999)}-{randint(0, 99)}'
new_city = names.get_full_name()
new_district = names.get_full_name()
new_state = f"{names.get_full_name()}"
new_simbol_state = f'{new_state[0:2]}'.upper()

user = starkbank.Project(
    environment="sandbox",
    id="5933018535428096",
    private_key=private_key_content
)
starkbank.user = user


# DATA E HORA UTC ISO


def sending_invoices_for_24_HRs():
    number_boletos = randint(8, 12)
    hours_inicial = 0.00

    while hours_inicial <= 24:
        cont=0

        while (cont < number_boletos):
            invoices = starkbank.invoice.create([
                starkbank.Invoice(
                    amount=248000,
                    fine=2.5,
                    descriptions=[{'key': 'Winter', 'value': 'is comming!'}],
                    interest=1.3,
                    name=f'{new_name}',
                    tax_id="29.176.331/0001-69",
                )
            ])
            cont+=1
        time.sleep(10800)
        hours_inicial += 3.01
    return HttpResponse()


def invoice_taxs_and_transfer(payment_metod=str, amount=float):
    qr_code = 0.15
    pix_tax = 0.50
    boleto_emitido = 0.99
    boleto_liquidado = 1.49
    ted_tax = 2
    if payment_metod == "qr_code":
        transfer_value = amount - qr_code
    elif payment_metod == 'pix_payment':
        transfer_value = amount - pix_tax
    elif payment_metod == 'boleto':
        transfer_value = amount - boleto_emitido - boleto_liquidado
    elif payment_metod == 'TED':
        transfer_value = amount - ted_tax

    return starkbank.transfer.create([
        starkbank.Transfer(
            amount=transfer_value,
            tax_id="20018183000180",
            name="Stark Bank S.A.",
            bank_code="20018183",
            branch_code="0001",
            account_number="6341320293482496",
            external_id="my-external-id",
            scheduled="2020-08-14",
            tags=["lannister", "invoice/1234"]
        )
    ])


@csrf_exempt
@require_POST
def webhook_request(request):
    jsondata = request.body
    data = json.loads(jsondata)
    for answer in data['form_response']['answers']:  # go through all the answers
        type = answer['type']
    return type


def webhook_extracting_and_sending_transfer():
    response = webhook_request()

    event = starkbank.event.parse(
        content=response.data.decode("utf-8"),
        signature=response.headers["Digital-Signature"],
    )
    status_paid = event(['type'])
    amount_value = event(['amount'])
    if event.subscription == "transfer":
        id_transfer = event(['id'])
        if status_paid == 'processing':
            time.sleep(300)
            webget = starkbank.webhook.get(id_transfer)
            webget_status = webget(['type'])
            if webget_status == 'success':
                payment_metod = 'pix_payment'



        elif status_paid == 'sent':
            time.sleep(300)
            webget = starkbank.webhook.get(id_transfer)
            webget_status = webget(['type'])
            if webget_status == 'success':
                payment_metod = 'TED'

        else:
            payment_metod = 'error'



    elif event.subscription == "boleto":

        if status_paid == 'paid':
            payment_metod = "boleto"
        else:
            payment_metod = 'error'

    elif event.subscription == "brcode-payment":
        if status_paid == 'success':
            payment_metod = "qr_code"
        else:
            payment_metod = 'error'
    return invoice_taxs_and_transfer(payment_metod, amount_value)

