import random
Asescheers= []
Bsescheers=[]
Asesrec=[]
Bsesrec=[]
Asessend=[]
Bsessend=[]
Asesmem = []
Bsesmem = []

def read():
    text= open("theCheers.txt", "r")
    lines = text.readlines()
    all = []
    recipients= []
    senders = []
    cheers = []
    for i in lines:
        all += i.split('|')
    num = 0
    while num < len(all):
        if num % 3 == 0:
            all[num] = all[num].rstrip(" ")
            recipients.append(all[num])
        elif num % 3 == 1:
            cheers.append(all[num])
        else:
            all[num] = all[num].rstrip("\n")
            senders.append(all[num])
        num+=1
        
    memtext = open("members.txt", "r")
    memlines = memtext.readlines()
    all1 = []
    for i in memlines:
        all1+= i.split(' ')
    num1 = 0
    members = []
    session = []
    while num1 < len(all1):
        if num1 % 2 == 0:
            all1[num1]=all1[num1].rstrip(" ")
            members.append(all1[num1])
        else:
            all1[num1]=all1[num1].rstrip("\n")
            session.append(all1[num1])
        num1+=1
    count = 0
    for i in session:
        if i == 'A':
            Asesmem.append(members[count])
        else:
            Bsesmem.append(members[count])
        count += 1
    count = 0
    for i in cheers:
        if (recipients[count] in Asesmem):
            Asesrec.append(recipients[count])
            Asescheers.append(cheers[count])
            Asessend.append(senders[count])
        else:
            Bsesrec.append(recipients[count])
            Bsescheers.append(cheers[count])
            Bsessend.append(senders[count])
        count+=1


randomlistA = []
randomlistB = []
Asesread = []
Bsesread = []
def choose():
    randomlistA = random.sample(range(0, len(Asesmem) ), len(Asesrec))
    randomlistB = random.sample(range(0, len(Bsesmem) ), len(Bsesrec))
    checkA(randomlistA, Asessend, Asesmem, Asesrec)
    checkB(randomlistB, Bsessend, Bsesmem, Bsesrec)
    for i in randomlistA:
        Asesread.append(Asesmem[i])
    for i in randomlistB:
        Bsesread.append(Bsesmem[i])
    


def checkA(li, send, mem, rec):
    num = 0
    for i in li:
        name = mem[i]
        if(rec[num] == name or send[num] == name):
            randomlistA = random.sample(range(0, len(Asesmem) ), len(Asesrec))
            checkA(randomlistA, send, mem, rec)
        else:
            num+= 1

def checkB(li, send, mem, rec):
    num = 0
    for i in li:
        name = mem[i]
        if(rec[num] == name or send[num] == name):
            randomlistB = random.sample(range(0, len(Bsesmem) ), len(Bsesrec))
            checkB(randomlistB, send, mem, rec)
        else:
            num+= 1

read()
choose()
print("B members ")
print(Bsesmem)
print("B recievers ")
print( Bsesrec)
print("B senders ")
print( Bsessend)
print("B readers ")
print( Bsesread)
