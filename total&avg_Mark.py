# get marks of 3 subjects from user
subject_one = int(input("Enter the mark acquired in subject 1: "))
subject_two = int(input("Enter the mark acquired in subject 2: "))
subject_three = int(input("Enter the mark acquired in subject 3: "))

# calculating total
total_mark = subject_one + subject_two + subject_three

# calculating average
average_mark = total_mark / 3

print("Total Mark of Student: ", total_mark)
print("Average Mark of Studnet: ",average_mark)