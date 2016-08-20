# -*- coding: utf-8 -*-
# This file is part of Shuup Boilerplate Theme.
#
# Copyright (c) 2012-2016, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
import setuptools

# Change these to match your own theme
theme_identifier = "shuup_boilerplate_theme"  # unique identifier for application
theme_description = "Shuup Boilerplate Theme"  # human readable description for application

try:
    import shuup_setup_utils
except ImportError:
    shuup_setup_utils = None

if __name__ == '__main__':
    setuptools.setup(
        name=theme_identifier,
        version="1.0.0",
        description=theme_description,
        packages=setuptools.find_packages(),
        include_package_data=True,
        entry_points={"shuup.addon": "%s=%s" % (theme_identifier, theme_identifier)},
        cmdclass=(shuup_setup_utils.COMMANDS if shuup_setup_utils else {}),
        install_requires=[
            'shuup>=0.5.3',
        ],
    )
