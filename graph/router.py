from utils.llm import get_llm


def route_request(state):


    llm = get_llm()


    prompt = f"""

    Classify this supply chain request.

    Categories:

    shipment
    inventory
    supplier
    recovery
    reporting


    User request:

    {state['user_input']}


    Return only the category name.

    """


    result = llm.invoke(prompt)


    category = result.content.strip().lower()


    state["category"] = category


    return state