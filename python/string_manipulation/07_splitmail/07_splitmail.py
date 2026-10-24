print("Reading mail and give mail name and domain")

mail = input("Select mail if you want know the informations: ")

splitmail = mail.split("@")

namemail = splitmail[0]
domainmail = splitmail[1]

print(f"Your mail name is: {namemail}")
print(f"Your mail domin is: {domainmail}")
