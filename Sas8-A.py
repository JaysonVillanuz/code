#List
subject_list = ["OOP","HCI","Data Structure"]

#ask user to add subject
new = input("Enter the subject to add\n ")

#placing the subject that added to the list
subject_list.insert(4,new)

#print the new list
print("List of Subjects ",subject_list)
