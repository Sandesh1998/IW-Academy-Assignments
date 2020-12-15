# 11. Create a variable,filename.Assuming that it has a three-letter extension,and using sliceoperations,find the extension.For README.txt,the extension should be txt.
# Write code using slice operations that will give the name without the extension.Does your code work on filenames of arbitrary length?
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
print ("The name of the file is : " + repr(f_extns[0]))
