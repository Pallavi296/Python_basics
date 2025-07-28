#given a list
a = [1,2,3,4,5,6,7]

#interchange first and last digit of the list
a[0],a[-1] = a[-1],a[0]

print("The new list is " ,a)


#Swap the 2 digits:
List = [1,2,3,4,5,6,7,8,90]

#swap
List[0],List[2]=List[2],List[0]

print(List)


#using Temporary operator:
x=[2,3,4,5,6,2,1,7]
temp = x[3]
x[3]=x[5]
x[5]=temp

print(x)


k,l = 2,3
#before swapping:
print("Before swapping",k,l)

k,l = l,k
#After swapping
print("After swapping",k,l)


# swap elements in  string

smthg = ["Apple","Kajal","bananna","delhi"]
print(smthg)
index1 =1
index2 = 2

smthg[index1],smthg[index2] = smthg[index2],smthg[index1]

print(smthg)


#Swapping Characters Within Strings in a List:
b = ["APE","EYE","BIL","KIL"]
res = [sub.replace("A","temp").replace("E","A").replace("temp","E") for sub in b]
print(res)
'''A=temp
   E = A
   temp = E'''

