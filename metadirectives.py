##############################################################################
#
# Copyright (c) 2003 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""``i18n`` ZCML namespace directive interfaces

$Id$
"""
__docformat__ = 'restructuredtext'
from zope.interface import Interface
from zope.configuration.fields import Path

class IRegisterTranslationsDirective(Interface):
    """Register translations with the global Translation Service."""

    directory = Path(
        title=u"Directory",
        description=u"Directory containing the translations",
        required=True
        )
