import starkbank
from datetime import datetime, timedelta
import json

from decouple import config
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import time
import names
from random import randint

private_key, public_key = starkbank.key.create("sample/destination/path")
private_key_content = """
"""
new_name = names.get_full_name()
current_time = f'{(datetime.now())}'
current_data_bank = current_time[0:9]

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
                    amount=1000,
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
    elif payment_metod =='pix_qr_code':
        transfer_value = amount - qr_code - pix_tax
    elif payment_metod == 'error':
        print("This is a mistake")
        return ("Try again")

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





def webhook_extracting_and_sending_transfer(data_value):
    response = data_value

    event = starkbank.event.parse(
        content=response.data.decode("utf-8"),
        signature=response.headers["invoice"],
    )
    status_paid_for_invoice = event(['status'])

    amount_value = event(['amount'])
    if status_paid_for_invoice =='paid':
        payment_metod = 'pix_qr_code'
        print('Invoice Paid, ok you are really  Lannister')
        print(event)
    else :
        payment_metod = 'error'
        print('This invoice is not paid, when are you gonna be a really Lannister?  ' )
        print(event)
    return invoice_taxs_and_transfer(payment_metod, amount_value)


