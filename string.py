#strings
'''Strings in python are immutable: cannot be changed once created'''
# Reverse a string
a="Kajal"
print(a[::-1])
print(a[1:])            #excluding 1



#deleting a string
s= "wjniducnyfb"

del s

#Updating a string:
str = "HELLO PYTHON"

str1 = "HEY" + str[6:]

print(str1)

str2 = str.replace("PYTHON","WORLD")

print(str2)

#Common String methods:

st = "Pythonnnnnn"

print(len(st))

print(st.upper())
print(st.lower())

'''strip() and replace(): strip() removes leading and trailing whitespace from the string and replace(old, new) replaces all occurrences of a specified substring with another.'''

u = "   gfg  "
print(u.strip())

print(u.replace("gfg","Geeks"))


#Concating and repeating using + and * operator
#concatination
s1 = "Python "
s2 = "Language"

print(s1+s2)

#repeating:
s3 = "Hey Pythonn"
print(s3*4)