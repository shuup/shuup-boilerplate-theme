# -*- coding: utf-8 -*-
# This file is part of Shuup Boilerplate Theme.
#
# Copyright (c) 2012-2016, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
from django import forms
from django.utils.translation import ugettext_lazy as _

from shuup.xtheme import TemplatedPlugin
from shuup.xtheme.plugins.forms import TranslatableField


class StoreInfoPlugin(TemplatedPlugin):
    """
    A simple plugin to show store info in front
    """
    identifier = "boilerplate_store_information"
    name = _("Store information")
    template_name = "boilerplate/plugins/store_info.jinja"
    # editor_form_class = PageLinksConfigForm

    fields = [
        ("title", TranslatableField(label=_("Title"), required=False, initial="")),
        ("show_logo", forms.BooleanField(
            label=_("Show Logo"),
            required=False,
            initial=True,
            help_text=_("Show logo of the shop inside information box."),
        )),
        ("show_contact_address", forms.BooleanField(
            label=_("Show Contact Address information"),
            required=False,
            initial=True,
            help_text=_("Show store contact address information"),
        )),
        ("show_name", forms.BooleanField(
            label=_("Show public name"),
            initial=True,
            required=False,
        )),
    ]

    def get_context_data(self, context):
        show_logo = self.config.get("show_logo", True)
        show_contact_address = self.config.get("show_contact_address", True)
        show_name = self.config.get("show_name", True)

        request = context.get("request")
        return {
            "title": self.get_translated_value("title"),
            "show_logo": show_logo,
            "show_contact_address": show_contact_address,
            "show_name": show_name,
            "shop": request.shop
        }
