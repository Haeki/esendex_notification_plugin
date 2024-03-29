#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# (c) 2022 Nagarro ES GmbH
#          Mika Busch <mika.busch@nagarro.com>

# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

# Version 2.4.1 (2023-04-19)

from cmk.gui.valuespec import (
    Dictionary,
    Integer,
    TextInput,
)

from cmk.gui.i18n import _
from cmk.gui.plugins.wato.utils import (
    IndividualOrStoredPassword,
    notification_parameter_registry,
    NotificationParameter,
)


@notification_parameter_registry.register
class NotificationEsendex(NotificationParameter):
    @property
    def ident(self) -> str:
        return "esendex"
    @property
    def spec(self):
        return Dictionary(
            title=_("Configuration to send sms notification via esendex"),
            optional_keys=['sms_header', 'sub_pattern'],
            elements=[
                ("user_name", TextInput(
                    title=_("User Name"),
                    help=_("Esendex username"),
                    size=40,
                )),
                ("api_token", IndividualOrStoredPassword(
                    title=_("API Token"),
                    help=_("You need to provide a valid API token to be able to send notifications "
                        "If you don't have an API token yet, you can log in and generate one on your "
                        "<a href=\"https://www.esendex.com/profile\">user profile</a>"),
                    size=40,
                )),
                ("account_reference", TextInput(
                    title=_("Account Reference"),
                    help=_("You need to provide your essendex account reference"),
                    size=40,
                )),
                ("max_lenght", Integer(
                    title=_("Max Message Length"),
                    help=_("Maximum number of characters bevor message gets cut off"),
                    size=40,
                    default_value=160,
                )),
                ("sms_header", TextInput(
                    title=_("SMS Header"),
                    help=_("Header added to the start of each SMS"),
                    size=40,
                )),
                ("sub_pattern", TextInput(
                    title=_("Service output sub pattern"),
                    help=_("(Regexpattern) Matches get removed from the service output"),
                    size=40,
                    default_value="WARN - |CRIT - |OK - ",
                )),
            ]
        )
    
