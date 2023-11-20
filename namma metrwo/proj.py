
import numpy as np
t1=("Nagasandra","jalahali","peerya","yeshwantapur","Mahalakshmi","Mahakavi Kuvempu Road","Mantri square sampige Road","chickpete","National College","South End Circle","Rashteraya Vidyalaya Road","Jaya Prakash Nagar","puttenahalli","Doddakallasandra","Thalaghattapura","silk institute")
amt=50


st=np.array([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80])

def Share_Location():
    import phonenumbers
    import folium
    from number import number
    key="4bb0a4f774544c0bb88c6b05c3c93c9e"
    from phonenumbers import geocoder
    from opencage.geocoder import OpenCageGeocode
    from phonenumbers import carrier

    sanNumber=phonenumbers.parse(number)

    yourlocation=geocoder.description_for_number(sanNumber,"en")
    print(yourlocation)


    #servicce provider
    service_provider=phonenumbers.parse(number)
    print(carrier.name_for_number(service_provider,"en"))


    geocoder=OpenCageGeocode(key)
    query=str(yourlocation)
    results=geocoder.geocode(query)
    lat=results[0]['geometry']['lat']
    lng=results[0]['geometry']['lng']
    print(lat,lng)
    myMap=folium.Map(location=[lat,lng],zoom_start= 9)
    folium.Marker([lat,lng],popup=yourlocation).add_to((myMap))
    myMap.save("yourlocation.html")


def payment():
    import pyqrcode
    import png


    myUPI="myupiid988@okhdfc"
    qrcode=pyqrcode.create(myUPI)
    qrcode.png("myUPIid.png",scale=8)

def tickets(i,j,source,destination):
    import datetime
    import qrcode
    import math
    from datetime import date
    import time
    print("No of the passenger=1")
    print("source station: ",source)
    print("destitnation Staion : ",destination)
    print("Travel date: ", date.today())
    y=math.fabs(st[i]-st[j])
    print("Travel Amount:Rs ",y)
    print("do you wish to confirm these details and proceed for the payment now")
    print("1.proceed\n2.change details")
    ch3=int(input())
    if ch3==1:
        payment()
        time.sleep(2)
        
    else:
        Type_Station_Name()
        payment()
        time.sleep(2)
       
    generate_image=qrcode.make()
    generate_image.save("image.png")
 
def Type_Station_Name():
   
    print(("Got it. You can type in the Source Station Name here"))
    source=input()
    if source in t1:
            print("Great,your source station is set to ",source)
            print("Could you type in destination Station Name now")
            destination=input()
            if destination in t1:
                print("Alright,your destination station is set to ",destination)
                print("Thanks! Please check and verify the below booking details")
                tickets(t1.index(source),t1.index(destination),source,destination)
            else:

                print("Hmm,I could not find that station in my list")
                print("to share the starting station for your journey ,choose one of the option")
                print("1.Type Station Name\n2.Search from the list")
                ch4=int(input())
                if ch4==1:
                    Type_Station_Name()
                else:
                    search()
    
    else:

        print("Hmm,I could not find that station in my list")
        print("to share the starting station for your journey ,choose one of the option")
        print("1.Type Station Name\n2.Search from the list")
        ch4=int(input())
        if ch4==1:
            Type_Station_Name()
        else:
            search()

            
def search():
        print(t1)
        Type_Station_Name()
l=[]
def Faourite_Station():
    import pickle
    import os
    check_file=os.path.getsize("fav.txt")
  
    if check_file==0:
        ch6=1
        while ch6!=0:
       
            print("Add your favourite station to the list")
            print("choose from the list")
            print(t1)
            print("enter your favourite station")
            name=input()
            l.insert(len(l),name)
            print("do want to add an item to the list yes=1 or no=0")
            ch6=int(input())
        pickle_write=open("fav.txt","wb")
        pickle.dump(l,pickle_write)
        pickle_write.close()
        QRtickects()
    else:
        pickle_write=open("fav.txt","rb")
        l1=pickle.load(pickle_write)
        pickle_write.close()
        print("Okay please choose source station from below list of favorite station")
        print(l1)
        s=input()
        print("Thankyou .Now ,how do you wish to choose the destination station?")
        print("1.Type Station Name\n2.Search From List\n3.Favourite List")
        ch7=int(input())
        if ch7==1:
            print("Could you type in destination Station Name now")
            d=input()
            if d in t1:
                print("Alright,your destination station is set to ",d)
                print("Thanks! Please check and verify the below booking details")
                tickets(t1.index(s),t1.index(d),s,d)
            else:
                print("Hmm,I could not find that station in my list")
                QRtickects()
        elif ch7==2:
            print(t1)
            print("Could you type in destination Station Name now")
            d=input()
            print("Alright,your destination station is set to ",d)
            print("Thanks! Please check and verify the below booking details")
            tickets(t1.index(s),t1.index(d),s,d)
        else:
            print("Could you type in destination Station Name now")
            print(l1)
            d=input()
            print("Alright,your destination station is set to ",d)
            print("Thanks! Please check and verify the below booking details")
            tickets(t1.index(s),t1.index(d),s,d)
    return l1


            
def if_scan():
    
    inp=input("Have you  scanned the qrcode yes=1 and no=0")
    if(inp==1):
        return True
    else:
        return False
def cancel():
    import os
    if(if_scan()==True):
        print("Since the qr code is Scaned , It cannot be deleted")
    else:
        os.remove("image.png")
        print("Your ticket has been successfully cancelled , your 50per of your payment will be returned within 2-3 day to the registered payment")


def QRtickects():
    print("Alright! what would you like to do?")
    print("1.Buy Tickets \n2.Cancel Ticket")
    ch1=int(input())
    if ch1==1:
        print("Sure! I can help you buy an online QR tickets for today ")
        print("You can choose from the option below or type your query")
        print("choose from here")
        print("1.Share Location\n2.Type Station Name\n3.Search from the list\n4.Faourite Station")
        ch2=int(input())
        if ch2==1:
           Share_Location()   
        elif ch2==2:
            Type_Station_Name()
        elif ch2==3:
            search()
        else:
            Faourite_Station()
    else :
         cancel()
    
l9=["7975077741"]
def card_info_recharge():
    global amt
    if "7975077741"in l9:
        print("How much do you want to recharge")
        s=int(input())
        amt=amt+s
        print("avaliable balance is ",amt)
        QRtickects()
    else:
        print("I can't seem to find the a card against your whattsapp number")
        print("So, what name do you go by")
        QRtickects()
   
        

def check_balance():
        if "7975077741"in l9:
            global amt
            print("Avaliable balance ",amt)
            print("do you want to recharge? yes or no ")
            g=input()
            if(g=="yes"):
                card_info_recharge()
                return
            else:
                QRtickects()
                return
                
            
        else:
            print("I can't seem to find the a card against your whattsapp number")
            print("So, what name do you go by")
            QRtickects()
        
            
            





s=input("enter Hi to start the conversation ")
#print emojis using cldr \N{grinning face}
print("hello!\U0001f600 \nI am Shreya, your travel guide from Namma Metro.\nI can help you with the smart card top ups ,metro timings and much more!")
print("Type your queries or choose one of the option  below for me to assit")
print("1.QR tickets \n2.card info and recharge \n3.check balance")
ch=int(input())
if ch==1:
    QRtickects()
elif ch==2:
    card_info_recharge()
else:
    check_balance()

print()
