#ENTER THE LIST FROM USER AND RETRIEVE EVEN ELEMENTS FROM OF THE LIST USING LAMBDA?
l1 = [int(i) for i in input().split()]
out = list(filter(lambda i : i%2==0,l1))
print(out)