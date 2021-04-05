
from textblob import TextBlob
pos_correct=0
neg_correct=0
nut_correct=0
total=0
with open("C:/Users/yeshu/OneDrive/Desktop/blobtext.txt","r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)
        if analysis.sentiment.polarity > 0:
            pos_correct += 1
            total +=1
with open("C:/Users/yeshu/OneDrive/Desktop/blobtext.txt","r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)
        if analysis.sentiment.polarity < 0:
            neg_correct += 1
            total +=1   
with open("C:/Users/yeshu/OneDrive/Desktop/blobtext.txt","r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)
        if analysis.sentiment.polarity == 0:
            nut_correct += 1
            total +=1      
print("result: +ve( ;) ) = ",pos_correct/total,"-ve( ;( ) = ",neg_correct/total,"nutral ( :| ) = ",nut_correct/total)
print("Press any key to exit")
f=input()
