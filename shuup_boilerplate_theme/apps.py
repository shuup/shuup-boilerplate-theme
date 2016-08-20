# -*- coding: utf-8 -*-
# This file is part of Shuup Boilerplate Theme.
#
# Copyright (c) 2012-2016, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
import shuup.apps

from .theme import ShuupBoilerplateTheme


class AppConfig(shuup.apps.AppConfig):
    """
    Theme AppConfig

    This is your theme packages main AppConfig.

    Theme package can offer one theme or multiple themes.
    """
    name = ShuupBoilerplateTheme.identifier  # identify the application
    verbose_name = ShuupBoilerplateTheme.name  # Theme package name
    label = ShuupBoilerplateTheme.identifier  # Theme package label, for `settings.INSTALLED_APPS` for example
    provides = {
        "xtheme":  [":".join([ShuupBoilerplateTheme.__module__, ShuupBoilerplateTheme.__name__])]
    }
