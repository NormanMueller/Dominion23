from dataclasses import asdict, astuple, dataclass, fields
import sys

sys.path.append(r"c:\Users\norma\Github\Dominion2023")
from expansions.utils.field import Field
from cards.treasurecards.card_entitys import Copper, Gold, Silver
from cards.victorycards.card_entitys import Estate, Duchy, Province
from enum import Enum


@dataclass
class BaseExpansionField(Field):
    Copper: Copper = Copper()
    Silver: Silver = Silver()
    Gold: Gold = Gold()
    Estate: Estate = Estate()
    Duchy: Duchy = Duchy()
    Province: Province = Province()
