#!/usr/bin/env python
# coding: utf-8

# In[10]:


#indentation
for i in range(1,12):
    print("value of i "+str(i))
print("for loop complete")


# In[12]:


for var1 in range(1,12):
    print("No.{} squared {} and cubed is {} ".format(var1,var1**2,var1**3))
print ("for loop complete")


# In[13]:


#function
def function1():
    print("hello,knowledge shelf")
function1()


# In[16]:


# 1.no arguement and no return type
def add():
    var1= int(input("enter the first no.: "))
    var2=int(input("enter the second no.: "))
    var3=var1+var2
    print("sum is :",var3)
add()


# In[18]:


#with arguement and no return type
def subtract(var1,var2):
    var3=var1-var2
    print("subtraction= ",var3)
subtract(12,6)


# In[19]:


#no arguement but with return type
def multiply():
    var1= int(input("enter the 1st number: "))
    var2= int(input("enter the 2nd number: "))
    var3=var1*var2
    return var3
var4= multiply()
print ("multiply= ",var4)


# In[21]:


#with arguement and with return type
def divide(var1,var2):
    var3=var1/var2
    return var3
var4= divide(49,7)
print ("divide = ",var4)


# In[1]:


#input function and escape charecters
greeting = 'hello '
name= input("enter the name: ")
print(greeting +''+name)


# In[2]:


var1= int (input("enter the value : "))
type(var1)


# In[3]:


var2=(input("enter the value"))
var2= var2*2
print(var2)


# In[ ]:


#MODULES IN PYTHON
# to import use: import filename -> filename.function()
#another way : from filename import function-> call function after that
# another way to import all the functions: from filename import * -> call function after that


# In[4]:


#If else ,elif
name= input("enter the name : ")
age= int(input("how old are you, {0} ".format(name)))
print("your age is {0} ".format(age))
if age >=18:
    print("you can cast vote")
else:
    print("you are below age,come after {0} years".format(18-age))


# In[12]:


print("guess a number between 1 to 10")
guess= int(input())
if guess<5:
    print("enter a higher number")
    guess= int (input())
    if guess == 5:
        print("well done your guess is correct")
    else:
        print("sorry you have not guessed the correct number")
elif guess>5:
    print("please guess lower")
    guess=int(input())
    if guess == 5:
        print("well done your guess is correct")
    else:
        print("sorry you have not guessed the correct number")
else:
    print("CONGO!!! you have entered the correct number")


# In[3]:


#break 
name='arpita'
while True:
    print("please enter your name")
    name1=input()
    if name1==name:
        break
print('Thankyou',name)


# In[6]:


#continue
while True:
    print("who are you")
    name= input()
    if name!= 'arpita':
        continue
    print("hello arpita,what is your password?")
    password= input()
    if password=='1234':
        break
print("congo,granted")


# In[7]:


#for loop
for i in range(20):
    print("i is now {}".format(i))


# In[8]:


for i in range(1,20):
    print("i is now {}".format(i))


# In[9]:


for i in range(1,20,2):
    print("i is now {}".format(i))


# In[7]:


for i in range(20,1,-1):
    print("i is now {}".format(i))


# In[8]:


#how to excess string from loop
number= '12,5,69,589'
for i in range(0,len(number)):
    print(number[i])


# In[10]:


number= '12,5,69,589'
for i in range(0,len(number)):
    if number[i] in '0123456789':
        print(number[i],end='')


# In[11]:


number= '12,5,69,589'
cleanedNumber=''
for i in range(0,len(number)):
    if number[i] in '0123456789':
        cleanedNumber=cleanedNumber + number[i]
newnumber=int(cleanedNumber)
print("so the no. is {}".format(newnumber))
print(type(newnumber))


# In[ ]:


#while loop
var1=0
while var1<=10:
    print("value of var1 is ",var1)
    var1 +=1


# In[2]:


available_exit=["east","north-east","south"]
chosen_exit=""
while chosen_exit not in available_exit:
    chosen_exit=input("enter the direction ")
    if chosen_exit == "quit":
        print("your game over")
        break
else:
    print("you are out of loop")


# In[22]:


#list
print([1,2,3,4,5,6])
['cat','dog']
print(['hello','24',None,True,True])
animal=['cat','bat','dog','fox']
print(animal)
print(animal[0])
print(animal[0:2])
print('hello '+ animal[0])
animal[-1]
animal[:]
len(animal)
var1=[[1,2,3,4],['cat','bat','dog','fox']]
print(var1[1][3])
animal.append('elephant')
animal[-1]
animal.insert(1,'chicken')
animal[:]
animal.remove('chicken')
animal[:]
spam=[1,2,3.4,-4,-5]
spam.sort()
print(spam)


# In[25]:


#iterators
string="123456789"
iterator=iter(string)
print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# In[26]:


string="123456789"
for char in iter(string):
    print(char)


# In[28]:


mylist=['monday','tuesday','wednesday','thrusday','friday']
iteration= iter(mylist)
for char in range(0,len(mylist)):
    next_iter=next(iteration)
    print(next_iter)


# In[31]:


#dictionaries
mycat={'size':'fat','color':'gray','disposition':'loud'}
mycat['size']
spam=['cat','dog','rat']
spam1=['dog','rat','cat']
spam==spam1
#order should match otherwise false will be shown in list


# In[32]:


mycat1={'size':'fat','color':'gray','disposition':'loud'}
mycat2={'size':'fat','disposition':'loud','color':'gray'}
mycat1==mycat2
#true incase of dictionary,because values excess through key values


# In[36]:


data={'name':'arpita','gender':'female','occupation':'student'}
for v in data.values():
    print(v)
for k in data.keys():
    print(k)
for i in data.items():
    print(i)


# In[ ]:


data={'arpita':'6','sakshi':'9'}
while True:
    print("enter the name")
    name=input()
    if name=='':
        break
    if name in data:
        print(data[name]+' is the birthday of '+ name)
    else:
        print('no information')
        print('what is the birthday')
        birthday=input()
        data[name]=birthday
        print('data base updated')


# In[ ]:



    

