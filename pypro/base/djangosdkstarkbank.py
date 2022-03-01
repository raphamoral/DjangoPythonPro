import starkbank
from datetime import datetime
import time
from django.http import HttpResponse
import names
from random import randint

from pypro.Private_key import PRIVATE_KEY_CONTENT

data_list_temporary = []
private_key, public_key = starkbank.key.create("sample/destination/path")
private_key_content = PRIVATE_KEY_CONTENT
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


def creating_invoices():
    number_boletos = randint(8, 12)
    cont = 0
    while cont < number_boletos:
        starkbank.invoice.create([
            starkbank.Invoice(
                amount=1000,
                fine=2.5,
                descriptions=[{'key': 'Winter', 'value': 'is comming!'}],
                interest=1.3,
                name=f'{new_name}',
                tax_id="29.176.331/0001-69",
            )
        ])
        cont += 1
    return HttpResponse(200)


def sending_invoices_for_24_hrs():
    hours_inicial = 0.00
    while hours_inicial <= 24:
        creating_invoices()
        time.sleep(10800)
        hours_inicial += 3.01
    return HttpResponse(200)


def invoice_taxs_and_transfer(payment_me, amount):
    qr_code = 0.15
    pix_tax = 0.50
    boleto_emitido = 0.99
    boleto_liquidado = 1.49
    ted_tax = 2
    amount = float(amount)

    if payment_me == "qr_code":
        transfer_value = amount - qr_code
    elif payment_me == 'pix_payment':
        transfer_value = amount - pix_tax
    elif payment_me == 'boleto':
        transfer_value = amount - boleto_emitido - boleto_liquidado
    elif payment_me == 'TED':
        transfer_value = amount - ted_tax
    elif payment_me == 'pix_qr_code':
        transfer_value = amount - qr_code - pix_tax
    elif payment_me == 'error':
        print("This is a mistake")
        return "Try again"

    return starkbank.transfer.create([
        starkbank.Transfer(
            amount=f'{transfer_value}',
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


def parse_webhook(content, signature):
    event = starkbank.event.parse(content=content, signature=signature)
    if event.subscription != 'invoice':
        raise UnexpectedSubscriptionError

    if event.log.invoice.status == 'paid':
        id_status = f'{event.log.invoid.id}'
        if id_status in data_list_temporary:
            value_amount = event.log.invoice.amount

            payment = "pix_qr_code"
            invoice_taxs_and_transfer(payment, value_amount)
            print("You are really Lannister")
        else:
            print('You already paid , Lannister')
            pass
    else:
        print("When are you be really Lannister?")

    return event.log.invoice


class UnexpectedSubscriptionError(Exception):
    pass
