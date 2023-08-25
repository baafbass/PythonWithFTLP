print("Guest Party Manager\n")

guests ={}

guest_names = ("Alice",28,"alice@gmail.com","Bob",35,"bob@gmail.com","Charlie",30,"charlie@gmail.com")

i=0
controller=0

while controller < len(guest_names):
 guests[guest_names[i]] = tuple([guest_names[i+1],guest_names[i+2]])
 i+=3
 controller +=3 

guests.update({'David':(22,'david@gmail.com')})
guests.pop('Bob')

def get_guest_info(guest_name):
  if guest_name in guests.keys():
    print(f"{guest_name} (Age:{guests[guest_name][0]}) is coming to the party! Email: {guests[guest_name][1]}")
  else:
    print(f'{guest_name} is not on the guest list')

print(f"Total number of guests on the list : {len(guests)}")

print('''
Tape 1 to get a Guest Info
Tape 2 to add a Guest
Tape 3 to display Guests
''')

choice = int(input("Enter your option : "))

if choice == 1 :
   Gname = input('Enter the Guest Name : ')
   get_guest_info(Gname)
elif choice == 2:
   name = input("Enter the guest Name : ")
   if name in guests.keys():
     ch=input("The guest already exist,Do you want to update Y/N :")
     if ch == 'Y' or ch=='y':
       age = int(input("Enter the guest Age : "))
       email = input("Enter the guest Email: ")
       guests.update({name:(age,email)})
     elif ch=='N' or ch=='n':
       print("Add the new Guest")
       name = input("Enter the guest Name : ")
       age = int(input("Enter the guest Age : "))
       email = input("Enter the guest Email: ")
       guests.update({name:(age,email)})
   else:
      age = int(input("Enter the guest Age : "))
      email = input("Enter the guest Email: ")
      guests.update({name:(age,email)})

 

def display_guests():
  sorted_by_age = sorted(guests.items(),key=lambda item: item[1])
  for name,info in sorted_by_age:
     print(f'{name} : {info}')

display_guests()
  
 


