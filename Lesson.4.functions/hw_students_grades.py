"""
# Grade Calculator Exercise

## Problem
You're building a grade calculator for a teacher who needs to calculate final grades for students. The teacher needs to:

1. Calculate the average of multiple test scores
2. Apply a curve (add points to boost grades)
3. Convert numerical grades to letter grades
4. Format the output nicely

## Requirements
Without using functions, you would need to repeat the same calculations for each student. Your task is to:

1. Create functions that eliminate code repetition
2. Make the main program easy to read and understand
3. Handle the grade calculations for multiple students

## Expected Behavior
The program should ask for student names and their test scores, then display:
- Student name
- Original average
- Curved average
- Letter grade

## Sample Run
```
Enter student name (or 'done' to finish): Alice
Enter test scores separated by spaces: 85 92 78 88
Student: Alice
Original Average: 85.8
Curved Average: 90.8 (+5 curve)
Letter Grade: A-

Enter student name (or 'done' to finish): Bob  
Enter test scores separated by spaces: 72 68 75 70
Student: Bob
Original Average: 71.2
Curved Average: 76.2 (+5 curve)
Letter Grade: B-

Enter student name (or 'done' to finish): done
```

## Hints
Think about what code you would repeat for each student and turn those into functions:
- Calculating averages
- Applying curves
- Converting to letter grades
- Formatting output
"""
def calculate_average(scores):
    return sum(scores)/len(scores)

def apply_curve(average, curve_amount):
    return average + curve_amount

curve_amount = 5

def Converting_to_letter_grades(score):
    if score >= 93:
        return "A"
    elif score >= 90:
        return "A-"
    elif score >= 87:
        return "B+"
    elif score >= 83:
        return "B"
    elif score >= 80:
        return "B-"
    elif score >= 77:
        return "C+"
    elif score >= 73:
        return "C"
    elif score >= 70:
        return "C-"
    elif score >= 67:
        return "D+"
    elif score >= 65:
        return "D"
    else:
        return "F"   


while True:
    student_name = input("Enter student name (or 'done' to finish):")
    if student_name.lower() == "done":
        print("End of choosing the name of student")
        break
    
    print("Student: ", student_name)
 
        
    score_input = input("Enter test scores separated by spaces: ")
    scores = list(map(float, score_input.split()))

    original_avg = calculate_average(scores)
    curved_avg = apply_curve(original_avg, curve_amount)
    letter_grade = Converting_to_letter_grades(curved_avg)

    print(original_avg)
    print(curved_avg)
    print(letter_grade)


