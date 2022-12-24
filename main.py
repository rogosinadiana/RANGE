import random
def main():
    size=6
    list=[]
    for i in range(size):
        list.append(random.randrange(0,40))
    print(list)
    list_1=[]
    for i in range(1,len(list),2):
        list_1.append(list[i])
    print(list_1)
    list_2=[]
    for i in range(2,len(list),3):
        list_2.append(list[i])
    print(list_2)
    list_3=[]
    for i in range(len(list) -1,-1,-1):
        list_3.append(list[i])
    print(list_3)
main()