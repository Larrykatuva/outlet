from django.db import models
from django.db.models.deletion import DO_NOTHING
from src.models import Order
import uuid


class MpesaTransaction(models.Model):
    PAYMENT_STATUS = (
        ('PENDING', 'PENDING'),
        ('SUCCESS', 'SUCCESS'),
        ('FAILED', 'FAILED')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, to_field='id', on_delete=DO_NOTHING, related_name='order_transactions')
    amount = models.FloatField()
    phone = models.CharField(max_length=256)
    transaction_desc = models.CharField(max_length=256)
    merchant_req_id = models.CharField(max_length=256)
    checkout_req_id = models.CharField(max_length=256)
    result_code = models.IntegerField(null=True)
    result_desc = models.TextField(null=True)
    receipt_number = models.CharField(max_length=256, null=True)
    transaction_date = models.DateTimeField(null=True)
    payment_status = models.CharField(choices=PAYMENT_STATUS, max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
