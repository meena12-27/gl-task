def human_approval(state):

    print(
        "Human approval required:"
    )

    print(
        state["response"]
    )


    approval=input(
        "Approve action? yes/no:"
    )


    if approval.lower()=="yes":
        state["approved"]=True

    else:
        state["approved"]=False


    return state