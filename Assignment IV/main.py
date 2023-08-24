print("Guest Organizer\n")

run_program = True
guest_list = []

while run_program :
  print('''
Tape 1 to list your Guests
Tape 2 to add a Guest
Tape 3 to remove a Guest
''')

  choice = int(input('Enter your option :'))

  if choice == 1 :
    if len(guest_list)==0:
      print('There is no guest in your list')
    else:
      print("Your guests are listed bellow")
      for guest in guest_list:
       print(guest)
        
  elif choice == 2 :
    first_name = input('Enter the guest first name : ')
    last_name =input('Enter the guest last name : ')
    age = int(input('Enter the age of the guest : '))
    full_name = first_name+' '+last_name

    if age < 18:
      print('The guest is too young to be added on the list')
    else:
      guest_info = f'{full_name} {age} years old'
      guest_list.append(guest_info)
      print('The guest is successfully added to the list')
      
  elif choice == 3:
      if len(guest_list) !=0:
         removed_guest = input('Please enter correct info of the Guest : ')
         while removed_guest not in guest_list:
             print('You enter a wrong information')
             removed_guest = input('Please enter correct info of the Guest : ')
         guest_list.remove(removed_guest)
         print("The guest gets successfully deleted from the list")
      else :
         print("There is no guest to remove from the list")
  else:
    while choice != 1 or choice != 2 or choice !=3:
      print('''
Tape 1 to list your Guests
Tape 2 to add a Guest
Tape 3 to remove a Guest
''')
      choice = int(input('Enter your option :'))
      break


  while run_program:
     continue_operation = input("Do you want to continue Y/N : ")
     if continue_operation == "Y" or  continue_operation == "y":
       run_program = True
       break
     elif continue_operation == "N" or continue_operation == "n":
       run_program = False
         
print('See you the next time')