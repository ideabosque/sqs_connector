#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

__author__ = "bibow"

import boto3


class SQSConnector(object):
    def __init__(self, logger, **setting):
        self.logger = logger
        self.setting = setting
        self.sqs = self.connect()

    def connect(self):
        if (
            self.setting.get("region_name")
            and self.setting.get("aws_access_key_id")
            and self.setting.get("aws_secret_access_key")
        ):
            return boto3.client(
                "sqs",
                region_name=self.setting.get("region_name"),
                aws_access_key_id=self.setting.get("aws_access_key_id"),
                aws_secret_access_key=self.setting.get("aws_secret_access_key"),
            )
        else:
            return boto3.client("sqs")

    @property
    def sqs(self):
        return self._sqs

    @sqs.setter
    def sqs(self, sqs):
        self._sqs = sqs
