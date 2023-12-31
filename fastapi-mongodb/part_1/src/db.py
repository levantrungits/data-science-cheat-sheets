# Local modules
from uuid import UUID
from .schemas import Category, ItemSchema

# In this version, fake MongoDB usage.
# Pydantic class
# UUID: A universally unique identifier (UUID) is a 128-bit label used for information in computer systems.
#       The term globally unique identifier (GUID) is also used.
#
items = {
    UUID('dbb86c27-2eed-410d-881e-ad47487dd228'): ItemSchema(
        id=UUID('dbb86c27-2eed-410d-881e-ad47487dd228'),
        name="Hammer",
        price=9.99,
        count=20,
        category=Category.TOOLS,
    ),
    UUID('32c1383a-b79e-43c1-8313-c8704382c48a'): ItemSchema(
        id=UUID('32c1383a-b79e-43c1-8313-c8704382c48a'),
        name="Pliers",
        price=5.99,
        count=20,
        category=Category.TOOLS,
    ),
    UUID('c65943f6-a376-4265-98bb-5b13ed6a54c8'): ItemSchema(
        id=UUID('c65943f6-a376-4265-98bb-5b13ed6a54c8'),
        name="Nails",
        price=1.99,
        count=100,
        category=Category.CONSUMABLES,
    ),
}
