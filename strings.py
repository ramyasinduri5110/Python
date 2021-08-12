#Strings in python 

#how we can write strings in python

str1_singlequote='Hello World!'
str2_doublequotes="The string declaration in double quotes"
str_block=''' this is the biggest block of code with 
multiple lines of text
'''

#type gives you the information about the data type 
print(type(" Hey! there I am using python :D"))
print('The string written with single quotes : '+str1_singlequote)
print('The string written with double quotes : '+str2_doublequotes)
print('The string block : '+str_block)

#string concatenation 
#string concatenation only works with strings 
first_name='ramya'
last_name='kondepudy'
full_name=first_name+''+last_name
print('full name after concatenation: '+full_name)


#Type Conversion 
print('converting an integer value to a string ')
print(type(str(100)))

b=str(100)
c=int(b)
d=type(c)
print(d)

#Escape Sequences
#t adds the tab
#n adds the new line  
weather="it's \"kind of\" sunny"
print(weather)
