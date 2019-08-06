
'''a = [53941,38641,31525,75864,29026,12199,8352,58200,64784,80987]
b = len(a)-1
print(len(a))
for i in range(b):
    for j in range(i):
        if (a[i]+a[i+1])%2!=0:
            a[i],a[i+1]=a[i+1],a[i]
print(a)
'''
a = input()#个数
b = input()#数组

print(len(a))
