# advent code day 1
# meike


f=open("input.txt",'r') # open file to read in input
line = f.readline() #read first line
i=0
newelf=0
calories=[]
calories.append(0)
max=[0,0,0]
while line: #read in file per line
    if any(chr.isdigit() for chr in line): #if line contains  number add this to calories
        if(newelf==1):#if previous line was empty add to new elf
            calories.append(int(line))
        else:#is previous line was not empty add to same elf
            calories[i]+=int(line)
        newelf=0
    else:#if line is empty start new elf and check if last added elf has top 3 maximum calories
        j=0
        for m in max: #check if number of calories last added elf falls within top 3
            if (m<calories[i]):
                max[j]=calories[i]
                break
            j+=1
        i+=1
        newelf=1    #start new elf
    line = f.readline() #read next line in while loop

f.close()


for m in range(0,3,1): #sorting top 3 from high to low
    for n in range(m,3,1):
        if (max[m] < max[n]):
            a=max[m]
            max[m]=max[n]
            max[n]=a 
            b=idmax[m]
            idmax[m]=idmax[n]
            idmax[n]=a

msum=0
for m in max:
    msum+=m
print("total calories 3 elves with most calories = {}".format(msum))
print("number of calories of elf with most calories = {}".format(max[0]))

