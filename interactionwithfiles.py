"""
1.	Create a text file called “hello1.txt.txt” and add the following text inside of it:
Python
Java
Javascript
C/C++/C#
PHP
Node.js
Write a short program to read and display the text file


"""
# with open('files/hello1.txt', 'r') as myfile:
#     print(myfile.read())

# with open('files/hello1.txt','r') as my_file:
#     for file in my_file:
#         print(file)

"""
2.	Write a short program to append the following lines to “hello1.txt” (you will use a list of strings and a for-loop):
Go                                                                                              
Kotlin
Swift
Display the new contents of the file

"""
# my_list = ['Go\n', 'Kotlin\n', 'Swift\n']
# with open('files/hello1.txt', 'a') as my_file:
#     my_file.writelines(my_list)

# with open('files/hello1.txt', 'a') as my_file:
#     for line in my_list:
#         my_file.write(line)



# with open('files/hello1.txt', 'a') as my_file:
#     my_file.writelines(['Go\n', 'Kotlin\n', 'Swift\n'])

# with open('files/hello1.txt', 'r') as my_file:
#     for line in my_file:
#         print(line)

"""
3.	Write a short program that reads the “hello.txt” file and displays every other line (only odd lines).
"""

# with open('files/hello1.txt', 'r') as my_file:
#     lines = my_file.readlines()
#     for i in range(len(lines)):
#         if i % 2 == 0:
#             print(lines[i].split())

"""
4.	Write a program that generates 26 text files, called `A.txt`, `B.txt`, … `Z.txt`. 
Each file will contain the sentences below:
My name is letter X.
I am the 24th letter of the alphabet.

"""

# alphabet = []
# start = ord('A')
# for i in range(26):
#     alphabet.append(chr(start + i))
# print(alphabet)
# for letter in alphabet:
#     with open(f'files/alphabet/{letter}.txt', 'w') as new_file:
#         new_file.writelines(f'My name is letter {letter}.\n')
#         if letter == 'A':
#             new_file.writelines('I am the 1st letter of the alphabet. \n')
#         elif letter == 'B':
#             new_file.writelines('I am the 2nd letter of the alphabet. \n')
#         elif letter == 'C':
#             new_file.writelines('I am the 3rd letter of the alphabet. \n')
#         else:
#             new_file.writelines(f'I am the {ord(letter)-ord("A")+1}th letter of the alphabet. \n')




# alphabet = []
# start = ord('A')
# for i in range(26):
#     alphabet.append(chr(start + i))
# print(alphabet)
# for letter in alphabet:
#     with open(f'files/alphabet/{letter}.txt', 'w') as new_file:
#         new_file.writelines(f'My name is letter {letter}.\n')
#         new_file.writelines(f'I am the {ord(letter)-ord("A")+1}th letter of the alphabet. \n')


# for letter in alphabet:
#     with open(f'files/alphabet/{letter}.txt') as my_file:
#         for line in my_file:
#             print(line)

"""

5.	Create a csv file called “students.csv” and add the following text inside of it:
id,fname,lname,age,grade
1,Maria,Popescu,31,7.5
2,Andrei,Ionescu,26,8.0
3,Adriana,Marinescu,21,7.5
4,Matei,Gheorghescu,42,8.5
5,Eusebiu,Pop,33,9.5
6,Ioana,Popa,29,9.0
Read the file using Python’s `csv` standard library, and display it in the terminal as a table, using the options for string formatting from Python:



id	fname		lname		age	grade
---------------------------------------------------
1	Maria		Popescu		31	7.5
2	Andrei		Ionescu		26	8.0
3	Adriana		Marinescu		21	7.5
4	Matei		Gheorghescu	42	8.5
5	Eusebiu		Pop			33	9.5
6	Ioana		Popa			29	9.0

"""
# import csv
# data = [
#     ["id", "fname", "lname", "age", "grade"],
#     [1, "Maria", "Popescu", 31, 7.5],
#     [2, "Andrei", "Ionescu", 26, 8.0],
#     [3, "Adriana", "Marinescu", 21, 7.5],
#     [4, "Matei", "Gheorghescu", 42, 8.5],
#     [5, "Eusebiu", "Pop", 33, 9.5],
#     [6, "Ioana", "Popa", 29, 9.0]
# ]
#
# with open('files/students.csv', 'w') as writecsv:
#     writer = csv.writer(writecsv)
#     writer.writerows(data)

# with open('files/students.csv', 'r') as read_csv:
#     my_file = csv.reader(read_csv)
#     print('_' * 55)
#     for line in my_file:
#         print(f'{line[0]:^5}| {line[1]:<10}| {line[2]:<15}| {line[3]:^8}| {line[4]:^8}')
#         print('_' * 55)
"""
6.	Read again the information from the csv file above, store it all in a list of data, and then write a new file, called “students.json”, which will contain a valid JSON object. Use the following format for each student (and use Python’s standard JSON module):
[
	{
		"id": 1,
		"fname": "Maria",
		"lname": "Popescu",
		"age": 31,
		"grade": 7.5	
	},
	...
]

"""

import csv
import json
with open('files/students.csv', 'r') as my_csv:
    my_file = csv.reader(my_csv)
    my_json_file = list(my_file)
    for i in range(1, len(my_json_file)):
        dict_add = {
            "id": my_json_file[i][0],
            "fname": my_json_file[i][1],
            "lname": my_json_file[i][2],
            "age": my_json_file[i][3],
            "grade": my_json_file[i][4]
        }

        with open('files/students.json', 'a') as new_json:
            json.dump(dict_add, new_json, indent=4)
