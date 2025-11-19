"""
cd 'Path' -- to go to this location
filepath = "blabla"
ls -- list of files
cd.. -- to go tot parenth directory
"r" - read
"a" - append
"w" - write
"x" - create
\n - next line
"""
filepath = 'c:/Users/victo/Desktop/redi/Python/Lesson_Filepath/test.py'
content = "hello, I am Vika"
# filename = 'text.py'
outfile = open(filepath, 'w')
outfile.write(content)
outfile.close()
##################
filename = 'test.py'
file = open(filepath)
print(file.readline()) # or readlines to read everything
file.close()
######### open with for loop
filename = 'test.py'
file = open(filepath)

for j in file.readlines():
      print(j)
file.close()

