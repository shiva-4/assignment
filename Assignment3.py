#ist answer

a=10
b=20
c=67
if a>b:

    if a>c:
        print("a is grater ",a)
    else:
        print("c is greater",c)
elif b>a:
    if b>c:
        print("b is greater",b)
    else:
        print("c ids greater ",c)
else:
    pass

print()
print()


#2nd answer

st="malayalam"
def reverse(st):
    s1=st[::-1]
    if st==s1:
         print("given Strings are palindrome")
   
    else:
        print("given strings are not palindrome")
reverse(st)
print()
print()

#3rd answer
string="hello Excuse Me "
count1=0
count2=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)
print()

#4th answer
total = 0
list1 = [11, 5, 17, 18, 23] 
for ele in range(0, len(list1)):
	total = total + list1[ele]
print("Sum of all elements in given list: ", total)
print()
print()

#5th annswer
# Python program to find sum of elements in list
total = 1

list1 = [11, 5, 17, 18, 23] 
for ele in range(0, len(list1)):
	total = total * list1[ele]

print("multiplication of all elements in given list: ", total)

print()
print()

#6th aanswer
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 





  



    


