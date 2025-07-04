#read the file 
"""f=open('C://Users//dell//Desktop//learning_python//rose.txt')
#f = open("demofile.txt")
print(f.read())"""
"""with open("C://Users//dell//Desktop//learning_python//rose.txt") as f:
  print(f.read())

  Close the file when you are finished with it:
"""
"""f = open("C://Users//dell//Desktop//learning_python//rose.txt")
print(f.readline())
f.close()"""
"""with open("C://Users//dell//Desktop//learning_python//rose.txt") as f:
  print(f.readline())
  print(f.readline())"""
"""f=open("C://Users//dell//Desktop//learning_python//rose.txt")
print(f.read())"""
#loop in reading file
"""with open("C://Users//dell//Desktop//learning_python//rose.txt") as f:
    for x in f:
        print(x)"""


#Open the file "demofile.txt" and append content to the file:

"""with open("C://Users//dell//Desktop//learning_python//rose.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("rose.txt") as f:
  print(f.read())"""

"""f = open("your_file.txt", "x")

Check if file exists, then delete it:"""

"""import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")"""