#def singer_counter(n):
Nana = input()
#Nana is here just because she's required lol.
n = input()
#that the songs input
nlist = list(n.split(" "))
#we make a list of songs, but it's considered a list of strings so we make it an int list
intlist = []

for n in nlist:
    n = int(n)
    intlist.append(n)
# we finally got our int list
countlist = {}
#this dictonary will contain each song as a key and how many time it's repeated as a value

for i in range(len(intlist)): # first loop picks up an element
    count = 0 #song counter that is reseted for each song 
    for j in range(len(intlist)): # second loop compares it to every other element in the list.
        if intlist[i] == intlist[j]:#if it's equal to other element(repeated) it adds to the count.
            count += 1
    countlist[f'{intlist[i]}'] = count # we use an f string to represent each element in our intlist and the value is how many times it's repeated        
z= max(countlist.values())# we get the highest value in the dictonary 

x = int(len([i for i in countlist if countlist[i]== z])) #we get keys that have this value and see how many of them using len() and store it in x
print(x) #we print x. 
