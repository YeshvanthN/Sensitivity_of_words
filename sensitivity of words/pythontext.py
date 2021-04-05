import sys
import os
#os.system("python -m install textblob")
from textblob import TextBlob
fcount=int(input("Enter the number of feedbacks to analyse:"))
fp1=open('blobtext.txt','w+')
for i in range(fcount):
  fblob = input("Enter the blob: ")
  fp1.write(fblob)
  fp1.write("\n")
fp1.close()


fp2=open('blobtext.txt','r')
for fblob in fp2:  
  rblob=(TextBlob(fblob)).sentiment.polarity
  print("sentiment of",fblob,"=",rblob)
fp2.close()

print("Press any key to exit")
f=input()
