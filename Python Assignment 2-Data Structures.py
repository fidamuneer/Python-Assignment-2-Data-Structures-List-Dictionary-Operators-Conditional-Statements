## List Creation
age_list = [21,22,23,24,25]
print(age_list)

name_list = ["Ayisha","Fida","Yaseen","Arya","Rahul"]
print(name_list)

## List Operations/Modifications
name_list.append("Yazhini")
print(name_list)

age_list.insert(2,30)
print(age_list)

name_list.remove("Yazhini")
print(name_list)

age_list.pop()
print(age_list)

age_list.extend([29,30,26])
print(age_list)

age_list.sort()
print(age_list)
age_list.reverse()
print(age_list)

max_age = max(age_list)
print(max_age)
min_age = min(age_list)
print(min_age)
sum_of_ages = sum(age_list)
print(sum_of_ages)


## Accessing List Elements
first_element = name_list[0]
print(first_element)

last_element = name_list[-1]
print(last_element)

x = name_list[2:5]
print(x)

reverse_name = name_list[::-1]
print(reverse_name)


## Dictionary
student_marks = {"Ayisha":95 , "Yaseen":92 , "Fida":85 , "Arya":80 , "Rahul":72}
print(student_marks)

print(student_marks["Yaseen"])
print(student_marks["Rahul"])
print(student_marks["Ayisha"])

student_marks.update({"Janani":80})
print(student_marks)

student_marks.update({"Rahul":82})
print(student_marks)

dic_keys = student_marks.keys()
print(dic_keys)

dic_values = student_marks.values()
print(dic_values)

dic_items = student_marks.items()
print(dic_items)

## Sets
my_set = {"a","e","i","o","u","a","a","i"}
print(my_set)
''' The important characters of the Set are unordered , unchangeable and duplicates are not allowed.
So the repeated values 'a' and 'i' appear only once and also Python may display the letters in a different order because it has a character -unordered. '''

'''my_set[4]= "s"
Set do not support indexing and also it has a character -unchangeable,
so can't make changes after set has been created.'''

set1 = {1,3,5,7,9}
print(set1)
set2 = {2,3,5,8,10}
print(set2)

union = set1.union(set2)
print(union)

intersection = set1.intersection(set2)
print(intersection)


## Operators & Conditional Statements
score = int(input("Enter your Score(0 to 10): "))
if score<0 and score>10:
    print("Invalid Input")
elif score > 7:
    print("Above Average:Excellent work!Keep up your performance.")
    print
elif score >=4:
    print("Average:Good effort!Keep practicing,there's room for improvement.")
else:
    print("Below Average:Need to improve your performance,consistent practice will lead to better results.")
    
