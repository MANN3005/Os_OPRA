import time
print("OS Mini Project(March-2021)")
time.sleep(2)
print("  Name              RollNo   ")
time.sleep(1)
print("Mann Patel       IU1941230071")
time.sleep(1)
print("Mohit Beniwal    IU1941230083")
time.sleep(1)
print("Karan Oza        IU1941230089")
time.sleep(2)
k=0
while k == 0 :
    print("(1).What is Optimal Page Replacement Algorithm?")        
    print("(2).OPR Calculator")
    print("(3).Exit")
    option = int(input("Please enter your Selection: "))
    if option==1:
        print("____________________________________________________________________________________")
        print("|                  Optimal Page Replacement Algorithm                              |")
        print("| In operating systems, whenever a new page is referred and not present in memory, |")
        print("| page fault occurs and Operating System replaces one of the existing pages with   |")
        print("| newly needed page. Different page replacement algorithms suggest different ways  |")
        print("| to decide which page to replace.The target for all algorithms is to reduce number|")
        print("| of page faults.                                                                  |")
        print("|                                                                                  |")
        print("| In this algorithm, OS replaces the page that will not be used for the longest    |")
        print("| period of time in future.                                                        |")
        print("|__________________________________________________________________________________|")
    elif option==2:
        print("Enter the Number of Frames: ",end="")
        capacity = int(input())
        f,fault,pf = [],0,"No" 
        print("Enter the Reference String(Enter Page No. using space for eg.(7 0 2 0 1 4)): ",end="")
        s = list(map(int,input().strip().split()))
        print("\nString|Frame →\t",end='')
        for i in range(capacity):
            print(i,end=' ')
        print("Fault\n   ↓\n")
        occurance = [None for i in range(capacity)]
        for i in range(len(s)):
            if s[i] not in f:
                if len(f)<capacity:
                    f.append(s[i])
                else:
                    for x in range(len(f)):
                        if f[x] not in s[i+1:]:
                            f[x] = s[i]
                            break
                        else:
                            occurance[x] = s[i+1:].index(f[x])
                    else:
                        f[occurance.index(max(occurance))] = s[i]
                fault += 1
                pf = 'Yes'
            else:
                pf = 'No'
            print("   %d\t\t"%s[i],end='')
            for x in f:
                print(x,end=' ')
            for x in range(capacity-len(f)):
                print(' ',end=' ')
            time.sleep(1)
            print(" %s"%pf)
        time.sleep(2)
        print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))
    elif option==3:
        k=1
    else:
        k=1 
        
a = input("Press Enter to exit ")