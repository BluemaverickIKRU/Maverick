times = int(input())
p = 0
num_list = []
while True:
    p += 1
    num = input()
    num_list.append(num)
    if p == times:
        break
for i in num_list:
    if int(i[1]) % 3 == 0:
        print("Trendy number")
    else:
        print("Not a Trendy number")