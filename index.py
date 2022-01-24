# n = int(input("enter the n value : "))
# lst = []
# for i in range(n):
#     lst.append(int(input()))   

from ast import Not, Return
from curses import flash
from operator import index, indexOf


class mani:
    def TataelixProgram(n,lst):
        lsta=[]
        lstb=[]
        lstans=[]  
        lst.sort() 
        for i in range(n):
            if lst[i]%2==0:
                lsta.append(lst[i])
            else:
                lstb.append(lst[i])   
        for i in range(n):
            if lst[0]%2==0:
                if i%2==0:
                    if len(lsta)==0:
                        break
                    else:
                        lstans.append(lsta[0])
                        lsta.remove(lsta[0])
                else:
                    if len(lstb)==0:
                        break
                    else:
                        lstans.append(lstb[0])
                        lstb.remove(lstb[0])
            else:
                if i%2!=0:
                    if len(lsta)==0:
                        break
                    else:
                        lstans.append(lsta[0])
                        lsta.remove(lsta[0])
                else:
                    if len(lstb)==0:
                        break
                    else:
                        lstans.append(lstb[0])
                        lstb.remove(lstb[0])
        return lstans
# print(TataelixProgram(n,lst))
    def program(n,lst):
        lstans=[]
        lst.sort()
        odd=1
        even=0
        for i in range(n):
            if lst[0]%2==0:
                if lst[i]%2==0:
                    lstans.insert(even,lst[i])
                    even=even+2
                else:
                    lstans.insert(odd,lst[i])
                    odd=odd+2
            else:
                if lst[i]%2!=0:
                    lstans.insert(even,lst[i])
                    even=even+2
                else:
                    lstans.insert(odd,lst[i])
                    odd=odd+2
        return lstans
    # print(program(n,lst))
    ## qustion form tata elixe
    ## input1 : 5
    ## input2 :
    ## [9,12,23,8,5]
    ## Output 
    ## [5,8,9,12,23]
    # n=int(input("enter the n vlaue : "))
    # lst2d=[]
    # for i in range(n):
    #     row=[]
    #     for j in range(2):
    #         row.append(int(input()))
    #     lst2d.append(row)
    # print(lst2d)
    # tlst=[]
    # for i in lst2d:
    #     for j in i:
    #         tlst.append(j)
    #     for h in range(n):
    #         for g in range(2):
    #             if lst2d[h][g]==h:
    #                 print("equal")
    #             else:
    #                 print("not equal")
#-------------------------------------------------------------------------------------
    #  mallow techonlogy code one 
    def mallowTechonlogyCode():
        max1=0
        max2=0
        max3=0
        min1=99999
        min2=99999
        min3=99999
        n=int(input("enter the n value : "))
        for i in range(n):
            x=int(input(">>> "))
            if(x>max3):
                max3=x
                if (max3>max2):
                    y=max2
                    max2=max3
                    max3=y
                    if(max2>max1):
                        y=max1
                        max1=max2
                        max2=y
            else:
                if(x<min3):
                    min3=x
                    if(min3<min2):
                        y=min2
                        min2=min3
                        min3=y
                        if(min2<min1):
                            y=min1
                            min1=min2
                            min2=y
        print(max1,max2,max3)
        print(min1,min2,min3)
    # mallowTechonlogyCode()
    # n=int(input("enter the n value : "))
    # m=n/100
    # if int(m)%4==0:
    #     if int(m)%400==0:
    #         if int(m)%100==0:
    #             ture=3
    # mounthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
    # n=int(input("Enter the number : "))
    # year= n/100
    # mounth=n%100
    # if int(year)%100==0:
    #     if int(year)%400==0:
    #         if mounth==2:
    #             print((mounthDays[mounth-1])+1)
    #         else:
    #             print(mounthDays[mounth-1])
    # elif int(year)%4==0:
    #     if mounth==2:
    #         print((mounthDays[mounth-1])+1)
    #     else:
    #         print(mounthDays[mounth-1])
    # else:
    #     print(mounthDays[mounth-1])
#----------------------------------------------------------------# n = int(input("enter the n value : "))
# lst = []
# for i in range(n):
#     lst.append(int(input()))   

class mani:
    def TataelixProgram(n,lst):
        lsta=[]
        lstb=[]
        lstans=[]  
        lst.sort() 
        for i in range(n):
            if lst[i]%2==0:
                lsta.append(lst[i])
            else:
                lstb.append(lst[i])   
        for i in range(n):
            if lst[0]%2==0:
                if i%2==0:
                    if len(lsta)==0:
                        break
                    else:
                        lstans.append(lsta[0])
                        lsta.remove(lsta[0])
                else:
                    if len(lstb)==0:
                        break
                    else:
                        lstans.append(lstb[0])
                        lstb.remove(lstb[0])
            else:
                if i%2!=0:
                    if len(lsta)==0:
                        break
                    else:
                        lstans.append(lsta[0])
                        lsta.remove(lsta[0])
                else:
                    if len(lstb)==0:
                        break
                    else:
                        lstans.append(lstb[0])
                        lstb.remove(lstb[0])
        return lstans
# print(TataelixProgram(n,lst))
    def program(n,lst):
        lstans=[]
        lst.sort()
        odd=1
        even=0
        for i in range(n):
            if lst[0]%2==0:
                if lst[i]%2==0:
                    lstans.insert(even,lst[i])
                    even=even+2
                else:
                    lstans.insert(odd,lst[i])
                    odd=odd+2
            else:
                if lst[i]%2!=0:
                    lstans.insert(even,lst[i])
                    even=even+2
                else:
                    lstans.insert(odd,lst[i])
                    odd=odd+2
        return lstans
    # print(program(n,lst))
    ## qustion form tata elixe
    ## input1 : 5
    ## input2 :
    ## [9,12,23,8,5]
    ## Output 
    ## [5,8,9,12,23]
    # n=int(input("enter the n vlaue : "))
    # lst2d=[]
    # for i in range(n):
    #     row=[]
    #     for j in range(2):
    #         row.append(int(input()))
    #     lst2d.append(row)
    # print(lst2d)
    # tlst=[]
    # for i in lst2d:
    #     for j in i:
    #         tlst.append(j)
    #     for h in range(n):
    #         for g in range(2):
    #             if lst2d[h][g]==h:
    #                 print("equal")
    #             else:
    #                 print("not equal")
#-------------------------------------------------------------------------------------
    #  mallow techonlogy code one 
    def mallowTechonlogyCode():
        max1=0
        max2=0
        max3=0
        min1=99999
        min2=99999
        min3=99999
        n=int(input("enter the n value : "))
        for i in range(n):
            x=int(input(">>> "))
            if(x>max3):
                max3=x
                if (max3>max2):
                    y=max2
                    max2=max3
                    max3=y
                    if(max2>max1):
                        y=max1
                        max1=max2
                        max2=y
            else:
                if(x<min3):
                    min3=x
                    if(min3<min2):
                        y=min2
                        min2=min3
                        min3=y
                        if(min2<min1):
                            y=min1
                            min1=min2
                            min2=y
        print(max1,max2,max3)
        print(min1,min2,min3)
    # mallowTechonlogyCode()
    # n=int(input("enter the n value : "))
    # m=n/100
    # if int(m)%4==0:
    #     if int(m)%400==0:
    #         if int(m)%100==0:
    #             ture=3
    # mounthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
    # n=int(input("Enter the number : "))
    # year= n/100
    # mounth=n%100
    # if int(year)%100==0:
    #     if int(year)%400==0:
    #         if mounth==2:
    #             print((mounthDays[mounth-1])+1)
    #         else:
    #             print(mounthDays[mounth-1])
    # elif int(year)%4==0:
    #     if mounth==2:
    #         print((mounthDays[mounth-1])+1)# n = int(input("enter the n value : "))
# lst = []
# for i in range(n):
#     lst.append(int(input()))   

class mani:
    def TataelixProgram(n,lst):
        lsta=[]
        lstb=[]
        lstans=[]  
        lst.sort() 
        for i in range(n):
            if lst[i]%2==0:
                lsta.append(lst[i])
            else:
                lstb.append(lst[i])   
        for i in range(n):
            if lst[0]%2==0:
                if i%2==0:
                    if len(lsta)==0:
                        break
                    else:
                        lstans.append(lsta[0])
                        lsta.remove(lsta[0])
                else:
                    if len(lstb)==0:
                        break
                    else:
                        lstans.append(lstb[0])
                        lstb.remove(lstb[0])
            else:
                if i%2!=0:
                    if len(lsta)==0:
                        break
                    else:
                        lstans.append(lsta[0])
                        lsta.remove(lsta[0])
                else:
                    if len(lstb)==0:
                        break
                    else:
                        lstans.append(lstb[0])
                        lstb.remove(lstb[0])
        return lstans
# print(TataelixProgram(n,lst))
    def program(n,lst):
        lstans=[]
        lst.sort()
        odd=1
        even=0
        for i in range(n):
            if lst[0]%2==0:
                if lst[i]%2==0:
                    lstans.insert(even,lst[i])
                    even=even+2
                else:
                    lstans.insert(odd,lst[i])
                    odd=odd+2
            else:
                if lst[i]%2!=0:
                    lstans.insert(even,lst[i])
                    even=even+2
                else:
                    lstans.insert(odd,lst[i])
                    odd=odd+2
        return lstans
    # print(program(n,lst))
    ## qustion form tata elixe
    ## input1 : 5
    ## input2 :
    ## [9,12,23,8,5]
    ## Output 
    ## [5,8,9,12,23]
    # n=int(input("enter the n vlaue : "))
    # lst2d=[]
    # for i in range(n):
    #     row=[]
    #     for j in range(2):
    #         row.append(int(input()))
    #     lst2d.append(row)
    # print(lst2d)
    # tlst=[]
    # for i in lst2d:
    #     for j in i:
    #         tlst.append(j)
    #     for h in range(n):
    #         for g in range(2):
    #             if lst2d[h][g]==h:
    #                 print("equal")
    #             else:
    #                 print("not equal")
#----------------------------------------------------------------
 #  mallow techonlogy code one 
    def mallowTechonlogyCode():
        max1=0
        max2=0
        max3=0
        min1=99999
        min2=99999
        min3=99999
        n=int(input("enter the n value : "))
        for i in range(n):
            x=int(input(">>> "))
            if(x>max3):
                max3=x
                if (max3>max2):
                    y=max2
                    max2=max3
                    max3=y
                    if(max2>max1):
                        y=max1
                        max1=max2
                        max2=y
            else:
                if(x<min3):
                    min3=x
                    if(min3<min2):
                        y=min2
                        min2=min3
                        min3=y
                        if(min2<min1):
                            y=min1
                            min1=min2
                            min2=y
        print(max1,max2,max3)
        print(min1,min2,min3)
    # mallowTechonlogyCode()
    # n=int(input("enter the n value : "))
    # m=n/100
    # if int(m)%4==0:
    #     if int(m)%400==0:
    #         if int(m)%100==0:
    #             ture=3
    # mounthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
    # n=int(input("Enter the number : "))
    # year= n/100
    # mounth=n%100
    # if int(year)%100==0:
    #     if int(year)%400==0:
    #         if mounth==2:
    #             print((mounthDays[mounth-1])+1)
    #         else:
    #             print(mounthDays[mounth-1])
    # elif int(year)%4==0:
    #     if mounth==2:
    #         print((mounthDays[mounth-1])+1)
    #     else:
    #         print(mounthDays[mounth-1])
    # else:
    #     print(mounthDays[mounth-1])
#----------------------------------------------------------------
    #     print(mounthDays[mounth-1])
#----------------------------------------------------------------
    # for i in range(n):
    #     word.append(input())
    # for i in range(n):
    #     if word[i] == "this":
    #         word[i]="there"
    # print(word)
#----------------------------------------------------------------
    #     print(mounthDays[mounth-1])
#----------------------------------------------------------------
    # for i in range(n):
    #     word.append(input())
    # for i in range(n):
    #     if word[i] == "this":
    #         word[i]="there"
    # print(word)
#----------------------------------------------------------------
    def new():
        n = []
        newlst =[] 
        number = int(input("Enter the value : "))
        for i in range(number):
            n.append(int(input()))
        limit1=int(input(" enter the limit 1 : "))
        limit2 =int(input(" enter the limit 2 : "))
        for i in range(len(n)):
            if n[i]>limit1 and n[i]<limit2:
                newlst.append(n[i])
        avg = sum(newlst)/len(newlst)
        print(int(avg))

# mani.new()
# m pattern
# n= int(input("enter the number : "))
# for i in range (n):
#     for j in range(n):
#         if j==0 or j==n-1 or (i==j and i<=n/2  )or(j==n-i-1 and j>=n/2-1) :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ")

# calculator 
# from telegram.ext import Updater, InlineQueryHandler, CommandHandler
# import requests
# import re

# def get_url():
#     contents = requests.get('https://random.dog/woof.json').json()
#     url = contents['url']
#     return url

# def bop(bot, update ):
#     url =get_url()
#     chat_id =update.massage.chat_id
#     bot.send_photo(chat_id=chat_id, photo=url)

# def main():
#     updater=Updater('YOUR_TOKEN')
#     dp =Updater.dispatcher
#     dp.add_handler(CommandHandler('bop',bop))
#     updater.start_polling()
#     updater.idle()


# if __name__=='__main__':
#     main()

# n = input('enter the mane  : ')
# infosys code for checking the unique letter 
def getUniletter(n):
    l=[]
    for i in range(len(n)):
        j=i
        coun=0
        for j in range(len(n)):
            if n[i]==n[j]:
                coun+=1
        l.append(coun)
    if 1 in l:
        for i in range(len(n)):
            if l[i]==1:
                return i+1
        
    else:
        return -1

# infosys code for card sfiting 

n = int(input("Enter the n value : "))
lst =[]
for i in range(n):
    lst.append(input(">> "))
idx=int(input("enter the index : "))
findObj=input("enttet the finding value : ")
lst2=lst
def cardShifting(lst,lst2,findObj,idx):
    def sapLeft():
        countl=0
        stoper=True
        while stoper:
            if findObj==lst2[idx]:
                stoper =False
                print("count left ",countl)
                
            else:
                fist=lst2[0]
                for i in range(len(lst2)):
                    if i<len(lst2)-1:
                        lst2[i]=lst2[i+1]
                lst2[len(lst2)-1]=fist
                countl+=1
    def sapRight():
        countr=0
        stoper1=True
        while stoper1:
            if findObj==lst[idx]:
                stoper1=False
                print("count right ",countr)
            else:
                last=lst[len(lst)-1]
                for j in range(len(lst)-1,-1,-1):
                    lst[j]=lst[j-1]
                lst[0]=last
                countr+=1
    sL=sapLeft()
    sR=sapRight()
    
    if sR<=sL:
        return sR
    else:
        return sL
print(cardShifting(lst,lst2,findObj,idx))
        
