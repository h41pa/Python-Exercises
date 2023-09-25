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

