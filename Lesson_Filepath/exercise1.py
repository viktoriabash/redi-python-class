"""
outfile = open("exercise_1.txt", "x")
outfile.write("This is first line\n" )
outfile.write("This is second line" )
outfile.close()

outfile = open("exercise_1.txt", "r")
content = outfile.read()
print(content)
outfile.close() 
"""
outfile = open("exercise_1.txt", "x")
outfile.write("This is first line\n" )
outfile.write("This is second line" )
outfile.close()

outfile = open("exercise_1.txt", "r")
print(outfile.read())
outfile.close()





