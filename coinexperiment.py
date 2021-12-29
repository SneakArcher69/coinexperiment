import random
numberOfstreaks=0
list1=[]
print("Enter how much times the experiment should be repeated")
noOfexp=int(input())
print("Calculating...")
for experimentNumber in range(noOfexp):
    while True:
        result=random.randint(1,2)
        if result==1:
            result="H"
            list1=list1+[result]
            if len(list1)==100:
                x=-1
                while x < 101:
                    x=x+1
                    if list1[x:x+6]==["T","T","T","T","T","T"]:
                        numberOfstreaks+=1
                        x=x+5
                    elif list1[x:x+6]==["H","H","H","H","H","H"]:
                        numberOfstreaks+=1
                        x=x+5
                list1=[]
                break
        else:
            result="T"
            list1=list1+[result]
            if len(list1)==100:
                x=-1
                while x < 101:
                    x=x+1
                    if list1[x:x+6]==["T","T","T","T","T","T"]:
                        numberOfstreaks+=1
                        x=x+5
                    elif list1[x:x+6]==["H","H","H","H","H","H"]:
                        numberOfstreaks+=1
                        x=x+5
                list1=[]
                break
print("streak:",numberOfstreaks)
print('Chance of streak:',(numberOfstreaks / (noOfexp/100)),"%")


    
    
