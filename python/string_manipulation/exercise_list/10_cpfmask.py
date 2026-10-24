print("CPF with not mask")

error = True

while error:
    cpf = input("Enter your CPF with format ###.###.###-##: ")
    
    if(
        cpf.count(".") == 2
        and cpf.count("-") == 1 
    ):
        cpfsplit = cpf.split(".")

        digit = cpfsplit[2]
        digitsplit = digit.split("-")
        digit = digitsplit[1]

        cpfsplit[2] = digitsplit[0]
        

        cpf = "".join(cpfsplit)

        if(
            cpf.isdigit()
            and all (len(valor) == 3 for valor in cpfsplit)
            and len(digit) == 2
        ):
            error = False

        else:
            print("CPF is invalid")
    else:
        print("The format of CPF is incorrect")


print(f"Your CPF number is: {cpf}")
print(f"And your CPF verify digit is: {digit}")
    

