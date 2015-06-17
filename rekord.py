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
            print ("Records")
            for score in scores:
                print (score)
        #Add record
        elif choice=="2":
            score=input("Input your new record: ")
            scores.append(score)
        #Delete record
        elif choice=='3':
            score=input("Input record for delete: ")
            if score in scores:
                scores.remove(score)
            else:
                print("Record",score,"wrong")
        #Sorted scores
        elif choice=="4":
            scores.sort(reverse=True)
        else:
            print ("Sorry, your choise is wrong!")
    except:
        print('Erorre, Press Enter for choice')
        continue
