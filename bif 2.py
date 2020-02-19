num=input('number of students:')
`ns_list=[] 
s_list=[]
for i in range (int(num)):
    #students_name=input('student:')
    #ns_list.append(students_name)
    score=input('score:')
    ns_list.append(score)
    s_list.append(int(score))
print(ns_list)
def get_avg(s_list):
    #total=0
    #for i in range(0,int(num),1):
        #total=total+s_list[i]
    classavg=(sum(s_list)/int(num))
    return classavg
classavg=get_avg(s_list)
print("Class Avg = ", classavg)
def get_high(ns_list):
    #high=0
    for i in range(1,int(num)*2,2):
        #if int(ns_list[i])>high:
            #high=int(ns_list[i])
            high=(max(s_list))
            #highname=(max(ns_list)[i-1])
    print('highest score:', high)
get_high(ns_list)
def get_low(ns_list):
    #low=100
    for i in range(1,int(num)*2,2):
        #if int(ns_list[i])<low:
            #low=int(ns_list[i])
            low=(min(s_list))
            #lowname=ns_list[i-1]
    print('lowest score:', low)
get_low(ns_list)