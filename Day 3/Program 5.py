lst1 = [i for i in input("Enter the list1 items:").split()]
lst2 = [i for i in input("Enter the list2 items:").split()]
print(list(set(lst1).intersection(set(lst2))))
