#ENTER TWO LISTS BY THE USER AND RETRIEVE COMMON ELEMENTS OF TWO LISTS INTO ANOTHER USING LAMBDA?
l1 = [int(i) for i in input().split()]
l2 = [int(j) for j in input().split()]
out = list(filter(lambda i : i in l2,l1))
print(out)