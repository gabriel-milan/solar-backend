# -*- coding: utf-8 -*-
from tortoise import fields
from tortoise.models import Model


class LightIntensity(Model):
    id = fields.BigIntField(pk=True)
    latitude = fields.FloatField()
    longitude = fields.FloatField()
    lux = fields.FloatField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"({self.latitude}, {self.longitude}) - {self.lux}"
