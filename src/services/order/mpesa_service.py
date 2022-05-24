from src.models import MpesaTransaction, Order
from src.integrations.mpesa import MpesaPayment
from django.db.models.query import QuerySet
import uuid


class MpesaService:

    def __init__(self):
        self.mpesa_payment = MpesaPayment()

    def initiate_transaction(
            self,
            amount: float,
            phone: str,
            transaction_desc: str,
            order: Order
    ) -> MpesaTransaction:
        response = self.mpesa_payment.lipa_na_mpesa(
            amount=amount,
            phone=phone,
            transaction_desc=transaction_desc
        )
        return MpesaTransaction.objects.create(
            amount=amount,
            phone=phone,
            transaction_desc=transaction_desc,
            merchant_req_id=response.get('MerchantRequestID'),
            checkout_req_id=response.get('CheckoutRequestID'),
            payment_status='PENDING',
            order=order
        )

    @staticmethod
    def complete_successful_transaction(
            checkout_req_id: str,
            result_code: int,
            result_desc: str,
            **meta_data: dict
    ) -> int:
        item = meta_data.get('item')
        return MpesaTransaction.objects.filter(
            checkout_req_id=checkout_req_id
        ).update(
            result_desc=result_desc,
            result_code=result_code,
            receipt_number=item[1].get('value'),
            transaction_date=item[3].get('value'),
            payment_status='SUCCESS'
        )
