#INPUT THREE NUMBERS FROM THE USER AND FIND THE GREATEST OF THREE NUMBERS USING LAMBDA FUNCTION?
l1 = int(input())
l2 = int(input())
l3 = int(input())
n = (lambda a, b, c :((a if a>b else b)if b>c else c))(l1, l2, l3)
print('Max of them',n)
