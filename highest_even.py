Created on Sun Aug  8 13:26:15 2021

@author: rkondepu
"""
#  Finding highest even number in a list with user input 
def highest_even():
   n= int(input("Enter the list of numbers: "))
   listt=[] 
   for i in range(0,n):
      listt.append(int(input("Enter the elements in the list: ")))
   even_list=[]
   for j in listt:
       if j % 2 == 0:
          even_list.append(j)
   return(max(even_list))
    
    
print(highest_even())

# Finding the highest even number in a list by passing the list as argument 
"""
def highest_even(listt):
    even_list=[]
    for i in listt:
        if i % 2 == 0:
            even_list.append(i)
    return(max(even_list))

print(highest_even([2,3,4,5,6,12]) 
      """
