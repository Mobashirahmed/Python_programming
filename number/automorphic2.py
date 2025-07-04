n = int(input("Enter a no. "))
o = n
t = 10
sq = n ** 2
# print(sq)
flag = False


while n > 0:
    r = sq % t
    # print(r)
    # print(o)
    if o == r:
        flag = True
        break
    n = n // 10
    # print(n)
    t = t * 10
    # print(t)
    
# print(flag)
    
if flag:
    print("Automorphic")
else:
    print("not Automorphic")