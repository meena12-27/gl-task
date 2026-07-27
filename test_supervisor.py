from agents.supervisor import create_supervisor


agents = create_supervisor()

print(agents.keys())


# response=agents['shipment'].invoke(
#     {
#         'input':'Track shipment SH002'
#     }
# )

# print(response)