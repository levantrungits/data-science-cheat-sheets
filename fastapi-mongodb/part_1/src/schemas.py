# BUILTIN modules
from enum import Enum
from typing import List, Optional

# Third party modules
from pydantic import BaseModel, UUID4

# ------------------------------------------------------------------------
#


class Category(str, Enum):
    """ Category of an item. """
    TOOLS = "tools"
    CONSUMABLES = "consumables"


class ItemSchema(BaseModel):
    """ Representation of an item in the system. """
    id: UUID4
    name: str
    count: int
    price: float
    category: Category