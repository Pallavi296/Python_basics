def find_union(a,b):
     
     union_set = set()  # set removes duplicates from list

     for elem in a:
          union_set.add(elem)

     for elem in b:
          union_set.add(elem)

     return sorted(list(union_set))

a = [1,2,3,4,5]
b = [1,3,6,4,5]
 
ans = find_union(a,b)
print(ans)


# it is union of two arrays or lists 
     