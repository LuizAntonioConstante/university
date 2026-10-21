print("Verify if your change state starts with 'RIO'")

state = input("Type what state you whant verify: ")

splitstate = state.lower().split()

if splitstate[0] == "rio":
    print(f"The state '{state}' init with Rio")
else:
    print(f"The state {state} don't init with Rio")
