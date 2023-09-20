# BUILTIN modules
from enum import Enum
from typing import List, Optional

# Third party modules
from pydantic import BaseModel, Field, UUID4

# Local modules
from .apidocs.openapi_documentation import query_example, item_example


# ------------------------------------------------------------------------
#


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


class QueryArguments(BaseModel):
    """ Representation of item query arguments in the system. """
    name: Optional[str] = None
    count: Optional[str] = None
    price: Optional[str] = None
    category: Optional[str] = None


class ItemArgumentResponse(BaseModel):
    """ REpetitions of an argument query response in the system. """
    query: QueryArguments
    selection: List[ItemSchema]