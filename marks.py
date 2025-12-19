subject_name1 = input("Enter name of subject 1:")
marks1 = int(input(f"Enter marks of {subject_name1}:"))
subject_name2 = input("Enter name of subject 2:")
marks2 = int(input(f"Enter marks of {subject_name2}:"))
subject_name3 = input("Enter name of subject 3:")
marks3 = int(input(f"Enter marks of {subject_name3}:"))

full_marks  = int(input(f"Enter full marks of one subject:"))
sum = marks1 + marks2 + marks3
percentage = (sum/(full_marks*3))*100

print(f"Marks of {subject_name1}: {marks1}")
print(f"Marks of {subject_name2}: {marks2}")
print(f"Marks of {subject_name2}: {marks3}")

print(f"Total marks: {sum}")
print(f"Percentage: {percentage:.4f}")
