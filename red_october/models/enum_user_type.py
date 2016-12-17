# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from enum import Enum


class EnumUserType(Enum):
    """ It provides possible user types. """
    rsa = 1
    ecc = 2
