#percentage

percentage = 60

if percentage >= 90:
    print("Distinction")
elif percentage < 90 and percentage >= 80:
    print("First Division")
elif percentage < 80 and percentage >= 70:
    print("First Division")
elif percentage < 70 and percentage >= 60:
    print("First Division")
elif percentage < 60 and percentage >= 50:
    print("Passed")
else:
    print("Failed")


#To reduce redundancy, hierarchy can be maintained as below:
if percentage >= 90:
    print("Distinction")
elif percentage >= 80:
    print("First Division")
elif percentage >= 70:
    print("First Division")
elif percentage >= 60:
    print("First Division")
elif percentage >= 50:
    print("Passed")
else:
    print("Failed")