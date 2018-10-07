import zipfile

"""
######EXTRACTING THE FILES WHICH THE ZIP FILE CONTAINS IN######


file = "‪#Location of your zip file"
destination = "‪#Place or file where you want to extract all files within zip file."

#Checking whether there is a zip file or not
if zipfile.is_zipfile(file):
    with zipfile.ZipFile(file, "r") as content:
        content.extractall(destination)
else:
    print ("That's not a zip file!")
"""

""" 
######LISTING AND PRINTING WHAT THE ZIP FILE CONTAINS######


zip = zipfile.ZipFile ("/Users/galip/Desktop/list.zip","r"
files= zip.namelist()
for file in files:
    print(file)

"""

"""
######CREATING A NEW ZIP FILE######

file = "‪#Location of your zip file"
zip  = zipfile.ZipFile(file,mode="w", compression =zipfile.ZIP_DEFLATED)

zip.write("Location of the file that you want to add any type of file into zip file", arcname="You can re-name your file in zip here")
zip.write("Location of the file that you want to add any type of file into zip file", arcname="You can re-name your file in zip here")
zip.write("Location of the file that you want to add any type of file into zip file", arcname="You can re-name your file in zip here")

zip.close()


"""