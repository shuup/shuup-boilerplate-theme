# -*- coding: utf-8 -*-
# This file is part of Shuup Boilerplate Theme.
#
# Copyright (c) 2012-2016, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
from django import forms
from django.utils.translation import gettext_lazy as _

from shuup.themes.classic_gray.theme import ClassicGrayTheme


class ShuupBoilerplateTheme(ClassicGrayTheme):
    """
    Boilerplate Theme

    This is a simple theme that shows the inheritance from one of the Shuup base themes
    """

    identifier = "shuup_boilerplate_theme"  # internal identifier for theme, used system wide to differentiate themes
    name = _("Shuup Boilerplate Theme")  # Template name, shown in admin
    author = "Shoop Commerce Ltd"  # The author of the theme, shown in admin
    template_dir = "boilerplate"  # this is the dir your template is found

    """
    Plugings the theme offers

    Theme can offer wide variety of `Plugin`s these are declared in here.

    Boilerplate offers one plugin that shows store information for visiting customer.
    """
    plugins = ["shuup_boilerplate_theme.plugins:StoreInfoPlugin"]

    """
    Configurable fields

    These can be accessed from template by using
    `{{ xtheme.get(field_name, <default value>) }}`.
    See example usage in `templates/boilerplate/shuup/front/index.jinja`

    Values are also saved in settings so you can access them inside theme
    object by calling `self.get_setting(setting_name, <default_value>)`
    Example usage of this can be found below.
    """
    fields = [
        (
            "show_boilerplate",
            forms.BooleanField(
                required=False,
                initial=True,
                label=_("Show the boilerplate information on frontpage"),
            ),
        ),
        (
            "boilerplate_text",
            forms.CharField(required=False, label=_("Boilerplate text")),
        ),
        (
            "boilerplate_date",
            forms.DateField(required=False, label=_("Boilerplate date")),
        ),
    ]

    def should_show_boilerplate(self):
        return self.get_setting("show_boilerplate", False)
