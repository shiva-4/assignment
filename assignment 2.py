# 1 st question 
a=[1,2,'hi',2,1]
a=list(dict.fromkeys(a))
print(a)
print()


# 2nd difference between list
a=[1,2,4,5]
b=[1,2,9]
c=list(set(a)-set(b))
print(c)
print()

# 3rd frequency
# Python program to count the frequency of 


def CountFrequency(my_list): 
	
	# Creating an empty dictionary 
	freq = {} 
	for items in my_list: 
		freq[items] = my_list.count(items) 
	
	for key, value in freq.items(): 
		print ("% d : % d"%(key, value)) 

 
if __name__ == "__main__": 
	my_list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2] 
	CountFrequency(my_list)
	print()
	print()
	



# 4th question
from collections import Counter
color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]
counter1 = Counter(color1)
counter2 = Counter(color2)
print("Color1-Color2: ",list(counter1 - counter2))
print("Color2-Color1: ",list(counter2 - counter1))
print()
print()

#5th question
color2 = ["black", "yellow", "green", "blue"]
a=len(max(color2))
print(a)

#6th answer
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))
print()
print()

#7th answer
stri="i am a good boy"
counter=0
lis=['a','e','i','o','u']
for i in stri:
        if i in lis:
                
                counter=counter+1
                print(i)
        

print("total number of vowels ",counter)
print()
print()


#8th answer
n=int(input("enter the n "))
d=dict()

for i in range(1,n+1):
        d[i]=i*i

print(d)
print()
print()


#9th answer

dict1 = {'a': 12, 'for': 25, 'c': 9} 
dict2 = {'Geeks': 100, 'geek': 200, 'for': 300} 


# adding the values with common key 
for key in dict2: 
	if key in dict1: 
		dict2[key] = dict2[key] + dict1[key] 
	else: 
		pass
		
print(dict2)

#10 answer
L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List: ",L)
u_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",u_value)



        
        

        





