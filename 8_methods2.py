str="hellomynameisjungkook"
print(str.isalnum())      #return true because strings are only present in continuous manner without any space or special characters

str1="hello my name is jungkook"
print(str1.isalnum())     #return false because there are spaces in the string

str2="hey4hio5hgj"
print(str2.isalnum())     #return true because there are only letters and numbers without any spaces or special characters



a="hello wp"
print(a.isalpha())       #return false because there are spaces in the string

b="helloworld"
print(b.isalpha())       #return true because there are only letters without any spaces or special characters

c="123bdkeeieo4567890"
print(c.isalpha())       #return false because there are numbers with letters




s="jehois"
print(s.islower())       #return true because all the characters in the string are in lowercase



k="hello we are BTS"
print(k.isprintable())   #return true because all the characters in the string are printable (letters, numbers, spaces, and punctuation)

m="hello world\n"
print(m.isprintable())   #return false because the string contains a newline character (\n) which is not printable



j="hello world"
print(j.isspace())       #return false because there are characters in the string other than spaces

n="     "
print(n.isspace())       #return true because the string contains only spaces and no other characters



title="The Great Gatsby"
print(title.istitle())   #return true because the first letter of each word in the string is capitalized and the rest of the letters are lowercase"