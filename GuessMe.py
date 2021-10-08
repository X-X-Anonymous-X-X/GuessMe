import time
import os
import random
os.system("color E")
os.system('cls')
end="Thanks for playing"
best=["HAHAHAHAHA","\nI am somewhat smart you know :) !....","I pat myself for this..!","Wanna try again mate ?","\nBeing smart is a tedious work ","\nI knew it from the beginning ","\nSo Easssssyyyy...! ","\nThats it ? ","\nThink harder next time buddy..! "]
good=["\nMy guesses are really getting better ! ","\nI Appreciate myself ","\nAm i reading your brain ? ","\nI am gettin close "]
bad=["Wrong..??? I guess my programmer is an idiot","\nI think i should take a nap ! ","Really ??? ","Call an ambulance..but not for me :)) ","\nHow can i be wrong ?? ","\nFun fact :-Will AI take over humans ? :))) ","\nYou are frustating me now ..! ","\nEnough..i m tired ","\nGet me a drink please...! ","\nI am heating up buddy..! "]
err=["Wrong choice..Better luck next time","Wrong choice buddy","You had to type y or n","Not a valid response buddy","Try again with a valid choice","Invalid input buddy"]
name=input("Enter your username buddy..!  -->  ")
print("\nWelcome",name,"\n")
print("\nAre you ready ??? ")
time.sleep(1.5)
print("\nI guess you are ..!\n")
input("\nHit Enter to start")
print("loading",end=" ",flush=True)
for i in range(4):
    print(".",end=" ",flush=True)
    time.sleep(0.5)
os.system("cls")
print(" \n")
print("Think of any number between 1 to 10\n")
for i in range(4):
    print(".",end=" ",flush=True)
    time.sleep(1)
print(" \n")
    #input("Done ?")
a=[1,2,3,4,5,6,7,8,9,10]
ar=list(a)
c=list()
while True:
    while True:
        r=random.choice(a)
        a.remove(r)
        if len(c)==len(set(c)):
            c.append(r)
            if len(c)==5:
                break
        else:
            c.pop()
    random.shuffle(c)
    for i in c:
        print(i,end=" ",flush=True)
        time.sleep(0.5)
    print(" ")
    el=list()
    i1=input("\nIs your number here in this list ? y/n")
    if i1.lower()=="y":
        print("\n",random.choice(good),name)
        random.shuffle(ar)
        #case 1
        #exclude list
        for i in a:
            if i!=c[0] and i!=c[1] and i!=c[2] and i!=c[3] and i!=c[4]:
                el.append(i)
            else:
                continue

        print("\n")
        el0=el
        c0=c.pop()
        el0.append(c0)
        random.shuffle(c)
        r0=random.shuffle(el0)
        for i in el0:
            print(i,end=" ",flush=True)
            time.sleep(0.5)
        print(" ")
        i2=input("What about here ? y/n ")
        if i2.lower()=="y":
            for i in ar:
                print(i,end=" ",flush=True)
                time.sleep(0.5)
            print(" ")
            print("\nHoooray !! Your number is : ",c0)
            print("\n",random.choice(best),name)
        elif i2.lower()=="n":
            print("\n",random.choice(bad),name)
            #shuffling v1
            print("\n")
            el1=el
            c1=c.pop()
            el0.append(c1)
            random.shuffle(c)
            r1=random.shuffle(el1)
            for i in el1:
                print(i,end=" ",flush=True)
                time.sleep(0.5)
            print(" ")
            i3=input("\nIs your number present here ? y/n ")
            if i3.lower()=="y":
                for i in ar:
                    print(i,end=" ",flush=True)
                    time.sleep(0.5)
                print(" ")
                print("\nHoooray !! Your number is : ",c1)
                print("\n",random.choice(best),name)
            elif i3.lower()=="n":
                print("\n",random.choice(bad),name)
                print("\n")
                #shuffling v2
                print("\n")
                el2=el
                c2=c.pop()
                el0.append(c2)
                random.shuffle(c)
                r2=random.shuffle(el2)
                for i in el2:
                    print(i,end=" ",flush=True)
                    time.sleep(0.5)
                print(" ")
                i4=input("\nIs your number present here ? y/n ")
                if i4.lower()=="y":
                    for i in ar:
                        print(i,end=" ",flush=True)
                        time.sleep(0.5)
                    print(" ")
                    print("\nHoooray !! Your number is : ",c2)
                    print("\n",random.choice(best),name)
                elif i4.lower()=="n":
                    print("\n",random.choice(bad),name)
                    print("\n")
                    #shuffling v3
                    print("\n")
                    el3=el
                    c3=c.pop()
                    el0.append(c3)
                    random.shuffle(c)
                    r3=random.shuffle(el3)
                    for i in el3:
                        print(i,end=" ",flush=True)
                        time.sleep(0.5)
                    print(" ")
                    i5=input("\nIs your number present here ? y/n ")
                    if i5.lower()=="y":
                        for i in ar:
                            print(i,end=" ",flush=True)
                            time.sleep(0.5)
                        print(" ")
                        print("\nHoooray !! Your number is : ",c3)
                        print("\n",random.choice(best),name)
                    elif i5.lower()=="n":
                        print("\n",random.choice(bad),name)
                        print("\n")
                        #shuffling v4
                        print("\n")
                        el4=el
                        c4=c.pop()
                        el0.append(c4)
                        random.shuffle(c)
                        r4=random.shuffle(el4)
                        for i in el4:
                            print(i,end=" ",flush=True)
                            time.sleep(0.5)
                        print(" ")
                        i6=input("Is your number present here ? y/n ")
                        if i6.lower()=="y":
                            for i in ar:
                                print(i,end=" ",flush=True)
                                time.sleep(0.5)
                            print(" ")
                            print("\nHoooray !! Your number is : ",c4)
                            print("\n",random.choice(best),name)
                        else:
                            print(random.choice(err))
                            os.system("color 7")
                            break
                    else:
                        print(random.choice(err))
                        os.system("color 7")
                        break
                else:
                    print(random.choice(err))
                    os.system("color 7")
                    break
            else:
                print(random.choice(err))
                os.system("color 7")
                break
        else:
            print(random.choice(err))
            os.system("color 7")
            break

    elif i1.lower()=="n":
        #big predict
        print("\n",random.choice(bad),name)
        print("\n")
        random.shuffle(ar)
        k=a
        k0=k
        c0=c
        c0.pop()
        rk0=random.choice(k)
        k.remove(rk0)
        c0.append(rk0)
        random.shuffle(c0)
        for i in c0:
            print(i,end=" ",flush=True)
            time.sleep(0.5)
        print(" ")
        ik0=input("Is your number here then ?? y/n")
        if ik0.lower()=="y":
            for i in ar:
                print(i,end=" ",flush=True)
                time.sleep(0.5)
            print(" ")
            print("\nHoooray !! Your number is : ",rk0)
            print("\n",random.choice(best),name)
        elif ik0.lower()=="n":
            print("\n",random.choice(bad),name)
            print("\n")
            k1=k
            c1=c
            c1.pop()
            rk1=random.choice(k)
            k.remove(rk1)
            c1.append(rk1)
            random.shuffle(c1)
            for i in c1:
                print(i,end=" ",flush=True)
                time.sleep(0.5)
            print(" ")
            ik1=input("\nIs your number here ? y/n")
            if ik1.lower()=="y":
                for i in ar:
                    print(i,end=" ",flush=True)
                    time.sleep(0.5)
                print(" ")
                print("\nHoooray !! Your number is : ",rk1)
                print("\n",random.choice(best),name)
            elif ik1.lower()=="n":
                print("\n",random.choice(bad),name)
                print("\n")
                k2=k
                c2=c
                c2.pop()
                rk2=random.choice(k)
                k.remove(rk2)
                c2.append(rk2)
                random.shuffle(c2)
                for i in c2:
                    print(i,end=" ",flush=True)
                    time.sleep(0.5)
                print(" ")
                ik2=input("\nIs your number here ? y/n")
                if ik2.lower()=="y":
                    for i in ar:
                        print(i,end=" ",flush=True)
                        time.sleep(0.5)
                    print(" ")
                    print("\nHoooray !! Your number is : ",rk2)
                    print("\n",random.choice(best),name)
                elif ik2.lower()=="n":
                    print("\n",random.choice(bad),name)
                    print("\n")
                    k3=k
                    c3=c
                    c3.pop()
                    rk3=random.choice(k)
                    k.remove(rk3)
                    c3.append(rk3)
                    random.shuffle(c3)
                    for i in c3:
                        print(i,end=" ",flush=True)
                        time.sleep(0.5)
                    print(" ")
                    ik3=input("\nIs your number here ? y/n")
                    if ik3.lower()=="y":
                        for i in ar:
                            print(i,end=" ",flush=True)
                            time.sleep(0.5)
                        print(" ")
                        print("\nHoooray !! Your number is : ",rk3)
                        print("\n",random.choice(best),name)
                    elif ik3.lower()=="n":
                        rk4=random.choice(k)
                        for i in ar:
                            print(i,end=" ",flush=True)
                            time.sleep(0.5)
                        print(" ")
                        print("\nHoooray !! Your number is : ",rk4)
                        print("\n",random.choice(best),name)
                    else:
                        print(random.choice(err))
                        os.system("color 7")
                        break
                else:
                    print(random.choice(err))
                    os.system("color 7")
                    break
            else:
                print(random.choice(err))
                os.system("color 7")
                break
        else:
            print(random.choice(err))
            os.system("color 7")
            break
    else:
        print(random.choice(err))
        os.system("color 7")
        break   
    end_name=end+" "+name
    for i in end_name:
        print(i,end=" ",flush=True)
        time.sleep(0.1)
    print(" ")
    print("\n")
    admin="Created by Shreyash"
    for i in admin:
        print(i,end=" ",flush=True)
        time.sleep(0.05)
    os.system("color 7")
    break
    

