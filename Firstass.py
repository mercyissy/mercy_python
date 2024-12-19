my_strings = ["My name is ", "Dike Mercy \n" "I am in " "level 2 of " "Data science"]
combined_string = " ".join(my_strings)
print(combined_string)

my_string1 = "My name is " "Dike Mercy ,\n"
my_string2 = "I am in" 
my_string3 = "level 2 of"
my_string4 = "Data science"
combined_string = f"{my_string1} {my_string2} {my_string3} {my_string4}"
print(combined_string)


mmy_string1 = "My name is " "Dike Mercy ,\n"
my_string2 = "I am in" 
my_string3 = "level 2 of"
my_string4 = "Data science"
combined_string = "%s %s" % (my_string1, my_string2)
print(combined_string)
