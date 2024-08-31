#Copyright 2024 Diego San Andrés Vasco

"""
This file is part of Similator.

Similator is free software you can redistribute it andor modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Similator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Similator. If not, see httpswww.gnu.orglicenses.
"""
from similator import _rst_similator

from .memory import Memory
from .valid_data import ValidData
from .text_similator import TextSimilator

__all__ = [TextSimilator, ValidData, Memory]