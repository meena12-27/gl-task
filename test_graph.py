from graph.workflow import app


result = app.invoke(
    {
        "user_input":
        "Track shipment SH002"
    }
)


print(result)