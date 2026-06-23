print("1 Add contact | 2 View contact | 3 search contact | 4 Exit")

contacts = {}

while True:
    opt=input("Choose option")

    if opt == "1":
        x = input("Enter contact: ")
        y = int(input("Enter contact number: "))

        contacts [x]=y
        

    elif opt == "2":
        if len(contacts) == 0:
            print("There are no contacts")
        else:
            for x,y in contacts.items():
                print(x,":",y)

    elif opt == "3":
        if len(contacts) == 0:
            print("There are no contacts")
        else:
            z = input("Search contact: ")

                        
            if z in contacts:
                    print(z, ":", contacts[z])
                    

            else:
                print("Contact not found")

    elif opt == "4":
        break
    else:
     print("invalid input")
