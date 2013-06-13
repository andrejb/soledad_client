# -*- coding: utf-8 -*-
# leap_backend.py 
# Copyright (C) 2013 LEAP
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


"""
This file exists to provide backwards compatibility with code that uses
Soledad before the refactor that removed the leap_backend module.
"""


from leap.soledad.document import SoledadDocument
from leap.soledad.target import EncryptionSchemes


class LeapDocument(SoledadDocument):
    """
    This class exists to provide backwards compatibility with code that still
    uses C{leap.soledad.backends.leap_backend.LeapDocument}
    """
    pass

class EncryptionSchemes(EncryptionSchemes):
    """
    This class exists to provide backwards compatibility with code that still
    uses C{leap.soledad.backends.leap_backend.EncryptionSchemes}
    """
    pass
