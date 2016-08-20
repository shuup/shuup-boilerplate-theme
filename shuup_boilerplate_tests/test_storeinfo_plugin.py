# -*- coding: utf-8 -*-
# This file is part of Shuup Boilerplate Theme.
#
# Copyright (c) 2012-2016, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
import pytest
from django.core.urlresolvers import reverse
from shuup.testing.factories import get_default_shop
from shuup.xtheme._theme import override_current_theme_class, get_theme_by_identifier
from shuup_boilerplate_theme.theme import ShuupBoilerplateTheme
from shuup_tests.utils import SmartClient


@pytest.mark.django_db
def test_frontpage_loads():
    get_default_shop()
    with override_current_theme_class(ShuupBoilerplateTheme):
        c = SmartClient()
        soup = c.soup(reverse("shuup:index"))
        assert "Search for products" in soup.find("h2").text  # template loaded


@pytest.mark.django_db
def test_storeinfo_loads():
    get_default_shop()

    boilerplate_text = "Boilerplate loaded!"

    theme = get_theme_by_identifier(ShuupBoilerplateTheme.identifier)
    theme.set_setting("show_boilerplate", True)
    theme.set_setting("boilerplate_text", boilerplate_text)

    with override_current_theme_class(ShuupBoilerplateTheme):
        c = SmartClient()
        soup = c.soup(reverse("shuup:index"))
        texts = [p.text for p in soup.find_all("p")]
        assert "This is your text: %s" % boilerplate_text in texts
