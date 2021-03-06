#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# (c) 2020 Nagarro Allgeier ES GmbH
#          Mika Busch <mika.busch@nagarro-es.com>

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

register_notification_parameters("esendex", Dictionary(
    optional_keys=['sms_header', 'max_lenght', 'sub_pattern'],
    elements=[
        ("user_name", TextAscii(
            title=_("User Name"),
            help=_("Esendex username"),
            size=40,
            allow_empty=False,
        )),
        ("api_password", TextAscii(
            title=_("API Password"),
            help=_("You need to provide a valid API passowrd to be able to send notifications "
                   "If you don't have an API password yet, you can log in and generate one on your "
                   "<a href=\"https://www.esendex.com/profile\">user profile</a>"),
            size=40,
            allow_empty=False,
        )),
        ("account_reference", TextAscii(
            title=_("Account Reference"),
            help=_("You need to provide your essendex account reference"),
            size=40,
            allow_empty=False,
        )),
        ("sms_header", TextAscii(
            title=_("SMS Header"),
            help=_("Header added to the start of each SMS"),
            size=40,
            allow_empty=False,
        )),
        ("sub_pattern", TextAscii(
            title=_("Service output sub pattern"),
            help=_("(Regexpattern) Matches get removed from the service output"),
            size=40,
            allow_empty=False,
            default_value="WARN - |CRIT - |OK - ",
        )),
        ("max_lenght", Integer(
            title=_("Max Message Length"),
            help=_("Maximum number of characters bevor message gets cut off"),
            size=40,
            allow_empty=False,
            default_value=160,
        )),
    ]
))
