## strings are immutable
## every modification to existing string just makes a new string

string1="name"
string2="hi"

string = string1 + string2 + "huu "# string concatination

multiLineString="""1
2
3
"""

print(string)
print(multiLineString)

"""
commonly used string functions 
.lower()
.upper()
.isalpha()
.isdigit()
.isalnum()
.isupper()
.islower()
.strip()
.replace('old','new')
.split()

global strings functions:
len('string')

escape character :
\n - new line
\t - tab
'\' - escapes next character print('be'a')-> breaks, (print('be/'a')-> be'a works

slicing
string[start:stop(exlcusive):step]
"""
x="0123456789"
print(x[:]) ## prints all string
print(x[:8]) ## start to index 8
print(x[1:5]) ## specific range
print(x[1:8:2]) ## specific range with step 2
print()
