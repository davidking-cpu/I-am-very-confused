st = {'item1','item2','item3'}

fruits = {'apple','orange','mango','banana'}

print(len(fruits))

if 'banana' in fruits:
    print("'Banana' is in set")
else:
    print("'banana' not in set")

    def check_item(item):
        if item in fruits:
            print(f"{item} is in the set")
        else:
            print(f"{item} is not in the set")

check_item ('banana')
check_item('orange')
check_item('pear')