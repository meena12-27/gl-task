from typing import TypedDict, Optional


class SupplyChainState(TypedDict):

    user_input: str

    category: str

    response: str

    history:Optional[str]