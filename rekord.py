# Programm record
#
scores = []
choice = None

while choice != "0":
    try:
        print(
            """
	0- Exit
	1- View record
	2- Add record
	3- Delete record
	4- Sorted list
	"""
        )
        choice = input('Enter position: ')
        print()
        # Exit
        if choice == '0':
            print("Goodbay")
            input("\n\nPress Enter for Quit")
        # View records
        elif choice =="1":
            print ("Records\n")
            print("Name\tResult")
            for entry in scores:
                score, name=entry
                print (name, "\t", score)
        #Add record
        elif choice=="2":
            name=input("Input name: ")
            score=int(input("Input your new record: "))
            entry=(score, name)
            scores.append(entry)
            scores.sort(reverse=True)
            score=scores[:5]
        #Delete record
        elif choice=='3':
            name=input("Input name for delete: ")
            score = input("Input record for delete: ")
            if score and name in scores:
                scores.remove(name, score)
            else:
                print("Record",score,"or",name,"wrong")
        #Sorted scores
        elif choice=="4":
            scores.sort(reverse=True)
        else:
            print ("Sorry, your choise is wrong!")
    except:
        print('Erorre, Press Enter for choice')
        continue
