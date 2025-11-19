from collections import Counter
with open(r"C:\Users\victo\Desktop\redi\Python\Lesson_Filepath", "r") as file:
    text = file.read()
    
words = text.split() # split the text into words
word_count = Counter(words)
print(word_count)
