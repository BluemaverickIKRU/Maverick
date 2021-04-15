times = int(input())
num_list = []
for i in range(times):
    num = int(input())
    num_list.append(num)
for i in num_list:
    if int(i[1]) % 3 == 0:
        print("Trendy number")
    else:
        print("Not a Trendy number")
