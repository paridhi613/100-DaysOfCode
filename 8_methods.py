name="jiminnn!!!!!"
print(name.rstrip("!"))   #jiminnn   #given jimin wihtout the ! at the end 


name="harry"
print(name.replace("harry","josh"))   #josh  harry will be replaced by josh


song="silver spoon"
print(song.split())   #['silver', 'spoon']  the string will be split into a list of words


intro = "my name is jimin"
print(intro.capitalize())   #My name is jimin  the first character of the string will be capitalized
print(len(intro))   #16  the length of the string will be printed


intro1 = "my name is jimin"
print(intro1.center(50))   #                 my name is jimin                  the string will be centered within a field of 50 characters
print(len(intro1.center(50)))   #50  the length of the string along with the spaces will be printed



name = "jimin you got no jams jimin"
print(name.count("jimin"))   #2  the number of occurrences of "jimin" in the string will be counted and printed


hello="hello world!!!!!"
print(hello.endswith("!!"))   #True  the string end with "!" 


str1="welcome to the console"
print(str1.endswith("to",4,10))   #True  the substring "to" is found at the end of the specified range (4 to 10) in the string~



str2="welcome to the console"
print(str2.find("to"))         #8  the index of the first occurrence of "to" in the string will be printed
print(str2.find("toooo"))      #-1  since "toooo" is not found in the string, -1 will be printed