import math
import random
classCGPA={9.38:["318126511119"],
      9.32:["318126511122"],
      9.23:["318126511161"],
      9.18:["318126511155","318126511160"],
      9.17:["318126511121","318126511129"],
      9.07:["318126511153"],
      9.02:["318126511123","318126511147"],
      9.01:["318126511120"],
      8.95:["318126511150"],
      8.83:["318126511143"],
      8.82:["318126511145"],
      8.81:["318126511134"],
      8.77:["318126511158","318126511159"],
      8.71:["318126511138"],
      8.7:["318126511156"],
      8.67:["318126511117"],
      8.64:["318126511137"],
      8.42:["318126511136"],
      8.38:["318126511157"],
      8.32:["318126511130"],
      8.17:["318126511116"],
      8.16:["318126511131"],
      8.13:["318126511162"],
      8.12:["318126511164"],
      8.11:["319126511L02"],
      8.07:["318126511132"],
      7.97:["318126511149"],
      7.92:["319126511L03"],
      7.9:["318126511133","319126511L04"],
      7.77:["318126511125"],
      7.62:["318126511142"],
      7.57:["318126511148"],
      7.51:["318126511118"],
      7.44:["318126511127"],
      7.35:["318126511124"],
      7.3:["318126511154"],
      7.2:["318126511128"],
      7.15:["318126511141"],
      7.13:["318126511144"],
      7.08:["318126511151"],
      6.86:["318126511140"],
      6.61:["318126511163"],
      6.52:["318126511139"],
      0:["317126511067","317126511144","318126511126","318126511135","318126511152","318126511165","319126511L01"]
      }
count=0
for cgpa,name in classCGPA.items():
    count+=len(name)
print("Number of Students:",count)
membersPerBatch=4
batches=count/membersPerBatch
finalBatches=math.ceil(batches)
print("Number of Batches can form:",finalBatches)
classList=[]
batchesList=[[] for i in range(finalBatches)]
for cgpa,name in classCGPA.items():
    if len(name)>=2:
        for i in range(len(name)):
            classList.append([cgpa,name[i]])
    else:
        classList.append([cgpa,name[0]])
list1=[]
list2=[]
list3=[]
list4=[]
for i in classList:
    if i[0]>9:
        list1.append(i[1])
    elif i[0]>8:
        list2.append(i[1])
    elif i[0]>7:
        list3.append(i[1])
    else:
        list4.append(i[1])
for i in range(finalBatches):
    if len(list1)>0:
        batchesList[i].append(list1.pop(0))
    if len(list1)==0 and batchesList[i]==[]:
        if len(list2)>0:
            batchesList[i].append(list2.pop(0))
for i in range(finalBatches):
    if len(list2)>0:
        batchesList[i].append(list2.pop(random.randrange(len(list2))))
for i in range(finalBatches):
    if len(list3)>0:
        batchesList[i].append(list3.pop(random.randrange(len(list3))))
for i in range(finalBatches):
    if len(list4)>0:
        batchesList[i].append(list4.pop(random.randrange(len(list4))))
for i in range(finalBatches):
    print("Batch ",i+1,":",batchesList[i])
print("left over List2:",list2)
print("left over List3:",list3)
print("left over List4:",list4) 
