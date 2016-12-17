# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from enum import Enum


class EnumUserRole(Enum):
    """ It provides possible user types. """
    delete = 1
    revoke = 2
    admin = 3
    user = revoke
