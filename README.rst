Shuup Boilerplate Theme
=======================

Shuup Boilerplate Theme provides a conventional file and 
folder structure for Shuup theme development.

Copyright
=========

Copyright (C) 2012-2016 by Shoop Commerce Ltd. <contact@shuup.com>

Shuup is International Registered Trademark & Property of Shoop Commerce Ltd.,
Business ID: FI24815722, Business Address: Aurakatu 12 B, 20100 Turku,
Finland.


License
=======

Shuup Boilerplate Theme is published under the GNU Affero General Public License,
version 3 (AGPLv3). See the LICENSE file distributed with Shuup Boilerplate Theme.

Some external libraries and contributions bundled with Shuup may be
published under other AGPLv3-compatible licenses.  For these, please
refer to VENDOR-LICENSES.md file in the source code tree or the licenses
included within each package.

Installation
============

* run ``pip install -e /path/to/shuup-boilerplate-theme``
* add ``shuup_boilerplate_theme`` to ``settings.INSTALLED_APPS``

Using this theme as a starting point
====================================

* ``theme.py``: Change identifier and name for the theme
* ``theme.py``: Rename ``ShuupBoilerplateTheme`` and occurances
* ``apps.py``: Change application folder names to match your theme
* ``setup.py``: Change identifier and description
* Change the folder name of ``shuup_boilerplate_theme/templates/boilerplate``
