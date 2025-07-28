s1 = [1,2,3,4,5,6,7]
s2 = [20,93,43,55,86,7,9]

common= set(s1) & set(s2)


if common:
    print("common",common)
else:
    print("Not common")

#Common using list method:
a = [1,2,3,4,5,6]
b = [2,3,4,5,6,7]
common = [item for item in a if item in b]

if common:
    print("COMMON",common)

else:
    print("not common")