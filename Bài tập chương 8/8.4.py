
import math
a=eval(input("Nhập cạnh tam giác thứ nhất:"));
b=eval(input("Nhập cạnh tam giác thứ hai:"));
c=eval(input("Nhập cạnh tam giác thứ ba:"));
if a+b<c and b+c<c:
    print("Đây không phải là tam giác")
cv=a+b+c
p=cv/2
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Diện tích tam giác = ", S)