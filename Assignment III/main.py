print('Palindrome Checker')

#Function Using While

def is_palindrome_while(input_string:str)->bool:

  word = input_string.lower()
  
  k=0
  will_be_ignored =""
  while k < len(word):
    if word[k].isalnum():
      k+=1
      continue
    else:
      will_be_ignored+=word[k]
      k+=1
  will_be_ignored =set(will_be_ignored)
  
 
  i=0
  concatinated_string = ""
  while i < len(word):
    if word[i] not in will_be_ignored:
      concatinated_string += word[i]
      i+=1
    else:
      i+=1
      continue
  
  back_to_beginning_string =""
  j=len(concatinated_string)-1
  while j >= 0:
    back_to_beginning_string += concatinated_string[j]
    j-=1

  if concatinated_string == back_to_beginning_string :
    result=True
  else:
    result=False

  return result

test = input('Please Enter word,phrase,sentence... : ')
print(f'Checked with while : {is_palindrome_while(test)}')

#Function Using For


def is_palindrome_for(input_string:str)->bool:

  word = input_string.lower()
  
  will_be_ignored =""
  for k in range(len(word)):
    if word[k].isalnum():
      continue
    else:
      will_be_ignored+=word[k]
  will_be_ignored =set(will_be_ignored)
  
  concatinated_string = ""
  for i in range(len(word)):
    if word[i] not in will_be_ignored:
      concatinated_string += word[i]
    else:
      continue
 
  back_to_beginning_string =""
  for j in range(len(concatinated_string)-1,-1,-1):
    back_to_beginning_string += concatinated_string[j]

  if concatinated_string == back_to_beginning_string :
    result=True
  else:
    result=False

  return result

print(f'Checked with for : {is_palindrome_for(test)}')