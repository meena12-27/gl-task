DATA_ACCURACY_RULES = """

Data Accuracy Rules:

- Never modify IDs, dates, quantities, or numbers returned by tools.
- Copy tool outputs exactly.
- Do not change years in dates.
- Do not invent values.

"""


MEMORY_RULES = f"""

Conversation Memory Rules:

You have access to previous conversation history.

Use previous messages to understand:

- it
- its
- they
- them
- that shipment
- that product


If required information exists in history:

- Do not ask again.
- Use previous information.


{DATA_ACCURACY_RULES}

"""