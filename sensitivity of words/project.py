import os
from textblob import TextBlob
choice=0
print("******PYTHON PROJECT******")
print("SENSITIVITY OF WORDS")
while(choice!=3):
	print("Your choice: \n\t 1)Enter sentence to calculate \n\t 2)Enter file name \n\t 3)To exit\n")
	choice=int(input("Enter your choice"))
	if(choice==1):
		os.system('python C:/Users/yeshu/OneDrive/Desktop/pythontext.py')
	if(choice==2):
		os.system('python C:/Users/yeshu/OneDrive/Desktop/pythonfile.py')

print("Press any key to quit")
f=input()
quit
