import uuid
from django.db import models


class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    balance = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.id)

