#openfile
file = open("catalogue_","a")

#catalogue structure
name = []
year = []
architect = []
picture = []
description = []
catalogue = [[name],[year],[architect],[picture],[description]]

#inputs
while True:
    n = input("Input building name: ")
    name = name.append(n)

    y = input("Input building year: ")
    year = year.append(y)

    a = input("Input building architect: ")
    architect = architect.append(a)

    p = input("Attach picture: ")
    picture = picture.append(p)

    d = input("Input building description: ")
    description = description.append(d)
    break

print(catalogue)

#save list
for element in catalogue:
    file.write(element+"\n")
file.close()
