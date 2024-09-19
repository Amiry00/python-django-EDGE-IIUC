#1.convert to uppercase
user_name="Amirul"
original_name=user_name.upper()
print("converted username: ",original_name)

#2.convert to lowercase 
user_name="AMIRUL"
original_name=user_name.lower()
print("converted username: ",original_name)

#3.convert to title case
user_name="python programming"
title_name=user_name.title()
print("converted username: ",title_name)

#4.convert to sentence case
user_name="PYTHON PROGRAMMING"
sentence_name=user_name.capitalize()
print("converted username: ",sentence_name)

# 5. Finding length of a string
user_name="AMIRUL HOQUE"
legth_name=len(user_name)
print("length of the string",legth_name)

# 6. Finding the first character of a string
user_name="AMIRUL HOQUE"
first_name=user_name[0]
print("first character of the string: ",first_name)

# 7. Finding the last character of a string
user_name="AMIRUL HOQUE"
last_name=user_name[-1]
print("Last character of the string: ",last_name)

# 8. Swapping case in a string
user_name="Amirul Hoque"
swap_name=user_name.swapcase()
print("swap case: ",swap_name)

# 9. Checking if string is numeric
user_name="12345"
numeric_name=user_name.isnumeric()
print("Is numeric??",numeric_name)

# 10. Checking if string is alphabetic
user_name="Amirul"
alpha_name=user_name.isalpha()
print("Is string is alphabetic??",alpha_name)

# 11. Checking if string is alphanumeric
user_name="Amirul123"
alphanumeric_name=user_name.isalnum()
print("Is string is alphanumeric??",alphanumeric_name)

# 12. Checking if string is in lowercase
user_name="amirul"
lower_name=user_name.islower()
print("Is string in lowercase??",lower_name)

# 13. Checking if string is in uppercase
user_name="AMIRUL"
upper_name=user_name.isupper()
print("Is string in uppercase??",upper_name)

# 14. Checking if string is in title case
user_name="Python Programming"
title_name=user_name.istitle()
print("Is string in title case??",title_name)

# 15. Checking if string is in sentence case
user_name="Python Programming"
sentence_name=user_name.istitle()
print("Is string in sentence case??",sentence_name)

# 16.Replacing a substring in a string
user_name="Amirul Hoque"
replace_name=user_name.replace("Amirul","AMIRUL")
print("Replace name",replace_name)

# 17. Splitting a string
user_name="Amirul Hoque"
split_name=user_name.split()
print(" ",split_name)

# 18. Checking if string starts with a prefix
user_name="Python programming"
start_name=user_name.startswith("python")
print("Is start with the prefix ",start_name)

# 19. Finding the index of a substring in a string
user_name="python programming"
index_name=user_name.index("programming")
print("Index of the string ",index_name)

#20. Finding the count of a substring in a string
user_name="python programming"
count_name=user_name.count("programming")
print("Count of the string ",count_name)

#21. Checking if string is a valid identifier
user_name="python"
identifier_name=user_name.isidentifier()
print("Is valid identifier??",identifier_name) 

#22. Checking if string is a valid number
user_name="12345"
number_name=user_name.isnumeric()
print("Is valid number??",number_name)

#23. Checking if string is a valid decimal number
user_name="123.45"
decimal_name=user_name.isdecimal()
print("Is valid decimal number??",decimal_name)

#24. Checking if string is a valid hexadecimal number
user_name="0x12345"
hexadecimal_name=user_name.isdecimal()
print("Is valid hexadecimal number??",hexadecimal_name)

#25. Checking if string is a valid octal number
user_name="0o12345"
octal_name=user_name.isdecimal()
print("Is valid octal number??",octal_name)

#26. Checking if string is a valid binary number
user_name="010101"
binary_name=user_name.isdecimal()
print("Is valid binary number??",binary_name)

#27. Checking if string is a valid ASCII number
user_name="123"
ascii_name=user_name.isascii()
print("Is valid ASCII number??",ascii_name)

#28.Checking if string is empty
user_name=" "
empty_name=user_name.isspace()
print("Is empty??",empty_name)

#29. Checking if string is printable
user_name="12345"
printable_name=user_name.isprintable()
print("Is printable??",printable_name)

#30.  Removing a prefix from a string
user_name="python programming"
remove_name=user_name.removeprefix("python")
print("Remove prefix",remove_name)

#31. Removing a suffix from a string
user_name="python programming"
remove_name=user_name.removesuffix("programming")
print("Remove suffix",remove_name)

#32.Multiplying string
user_name="Amirul"
multiply_name=user_name*3
print("Multiply string: ",multiply_name)

#33. Concatenating strings
user_name="Amirul"
concatenate_name=user_name+"Hoque"
print("Concatenate string: ",concatenate_name)

#34.lstrip method to remove leading whitespaces
user_name=" Amirul"
strip_name=user_name.lstrip()
print("Leading whitespaces removed: ",strip_name)

#35.rstrip method to remove trailing whitespaces
user_name="Amirul "
strip_name=user_name.rstrip()
print("Trailing whitespaces removed: ",strip_name)

#36.strip method to remove leading and trailing whitespaces
user_name=" Amirul "
strip_name=user_name.strip()  
print("Leading and trailing whitespaces removed: ",strip_name)

#37.  Partitioning a string
user_name="Python programming"
partition_name=user_name.partition("programming")
print("Partition of the string: ",partition_name)

#38. Rpartitioning a string
user_name="Python programming"
partition_name=user_name.rpartition("Python")
print("Rpartition of the string: ",partition_name)

#39. Casefold for aggressive lowercases
user_name="Amirul"
casefold_name=user_name.casefold()
print("Aggressive lowercases: ",casefold_name)

#40. Centering a string
user_name="Amirul"
center_name=user_name.center(10)
print("Centered string: ",center_name)

#41. Justifying a string
user_name="Amirul"
just_name=user_name.rjust(10)
print("Justified string: ",just_name)

#42. Zfilling a string
user_name="Amirul"
fill_name=user_name.zfill(10)
print("Zfilled string: ",fill_name)

#43. Expanding tabs in a string
user_name="Amirul\tHoque"
expand_name=user_name.expandtabs(1)
print("Expanded tabs: ",expand_name)

#44.Using min to find lowest alphabetical character
user_name="Amirul"
min_name=min(user_name)
print("Lowest alphabetical character: ",min_name)

#45.Using max to find highest alphabetical character
user_name="Amirul"
max_name=max(user_name)
print("Highest alphabetical character: ",max_name)


