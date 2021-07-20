Emp_names=["Aadrika","Anshita","Vaishnavi","Aparna","Yashika"]
Emp_id=[1,2,3,4,5]
print(len(Emp_names)) # finding the length of list
print(Emp_names+Emp_id) # merging two lists
print(Emp_id*4)   #printing list 4 times
del Emp_names[3]  # deleting item at index 3
print(Emp_names)
Emp_names.remove("Yashika")  #deleting item using its name
print(Emp_names)
Emp_names.pop(1)            #deleting item at top
print(Emp_names)
Emp_names[0]="vaidehi" #update
print(Emp_names) 
Emp_names.clear()           #clears the content of list
print(Emp_names)
