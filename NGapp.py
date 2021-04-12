import time


result_list = []
counted_list = []
f_count = 0
list_item = []

print("Welcome to IKRU APP")
print("----------------------------------------")
print("Please follow the following procedures: ")
print("To CREATE list : Type 'A' ")
print("To ADD the count of item : Type 'C' ")
print("To PRINT the list : Type 'P' ")
print("----------------------------------------")
print("1)Create List", "2)Add count", "3)Print List", "4)Quit")

while True:
    command = input("What do you want to do?:  ").upper()
    if command == "QUIT":
        print("Thank u for using us.CHEER UP :) ....")
        time.sleep(1)
        break

    while command == "A":
        n = int(input("How many items to be added in your list? : "))
        print("Creating a list......")
        time.sleep(1.5)
        create_list = input("Ready to add the items, Y/N? ").upper()
        while create_list == "Y":
            if len(list_item) < n:
                items = input("Enter the items to be added to the list:  ").upper()
                list_item.append(items)
            else:
                print("You have added the required amount of items.")
                break
        break

    while command == "C":
        print("----------------------------------------")
        print(list_item)
        print("----------------------------------------")
        select = input("To which item do you want to add count? ").upper()
        if select == "DONE":
            print("Done adding the counts....")
            result_list = counted_list
            time.sleep(1)
            break

        count = int(input("How much you wanna add to it? : "))
        for i in list_item:
            if select == i:
                f_count += count
                result = f"{select} = {f_count}"
                counted_list.append(result)
                print(counted_list)
                f_count = 0

    while command == "P":
        print("Your list is below:")
        print(result_list)
        break

    else:
        print("Enter a relavant command buddy!")
        print("----------------------------------------")
        print("To CREATE list : Type 'A' ")
        print("To ADD the count of item : Type 'C' ")
        print("To PRINT the list : Type 'P' ")
        print("----------------------------------------")
