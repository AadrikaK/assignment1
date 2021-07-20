movie_list=["YJHD","DDLJ","Jab we met","Bahubali","Robot"]
mov_id=[1,2,3,4,5]
print(len(movie_list)) # finding the length of list
print(movie_list+mov_id) # merging two lists
print(movie_list*4)   #printing list 4 times
del movie_list[3]  # deleting item at index 3
print(movie_list)
movie_list.remove("Robot")  #deleting item using its name
print(movie_list)
movie_list.pop(1)            #deleting item at top
print(movie_list)
movie_list[1]="Race" #update
print(movie_list) 
movie_list.clear()           #clears the content of list
print(movie_list)