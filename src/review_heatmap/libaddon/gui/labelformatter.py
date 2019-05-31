# -*- coding: utf-8 -*-

# Libaddon for Anki
#
# Copyright (C) 2018-2019  Aristotelis P. <https//glutanimate.com/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version, with the additions
# listed at the end of the license file that accompanied this program.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# NOTE: This program is subject to certain additional terms pursuant to
# Section 7 of the GNU Affero General Public License.  You should have
# received a copy of these additional terms immediately following the
# terms and conditions of the GNU Affero General Public License that
# accompanied this program.
#
# If not, please request a copy through one of the means of contact
# listed here: <https://glutanimate.com/contact/>.
#
# Any modifications to this file must keep this entire header intact.

"""
Utilities to fill out predefined data in dialog text labels
"""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from aqt.qt import *

from ..consts import ADDON_NAME, ADDON_VERSION
from ..platform import ANKI20

format_dict = {
    "ADDON_NAME": ADDON_NAME,
    "ADDON_VERSION": ADDON_VERSION,
}

if not ANKI20:
    fmt_find_params = ((QLabel, QPushButton), QRegExp(".*"),
                       Qt.FindChildrenRecursively)
else:
    # Qt4: recursive by default. No third param.
    fmt_find_params = ((QLabel, QPushButton), QRegExp(".*"))


def formatLabels(dialog, linkhandler=None):
    for widget in dialog.findChildren(*fmt_find_params):
        if widget.objectName().startswith("fmt"):
            widget.setText(widget.text().format(**format_dict))
        if linkhandler and isinstance(widget, QLabel):
            widget.linkActivated.connect(linkhandler)
