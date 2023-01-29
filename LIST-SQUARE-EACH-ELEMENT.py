#ENTER THE LIST FROM USER AND SQUARE EACH ELEMENT OF THE LIST USING LAMBDA?
l1 = [int(i) for i in input().split()]
out = list(map(lambda i : i**2,l1))
print(out)