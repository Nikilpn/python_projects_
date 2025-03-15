profit=0

resources={
    "water":500,
    "milk":200,
    "coffee":100
}


is_on=True
while is_on:
    choice=input("what would you like to have ?(late/espresso/cappuccino), report to show details,off to switch off machine :")
    if choice=="off":
        is_on=False
    if choice=="report":
        print(f"Water={resources['water']}ml ")
        print(f"Milk={resources['milk']}ml ")
        print(f"Coffee={resources['coffee']}g ")
        print(f"Money={profit}Rs")

