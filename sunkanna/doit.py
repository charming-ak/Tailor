def printPerson(data):
    for k,v in data.items():
        print(k,':',v)
#mydata = {'name':'Anil','age':31,'city':'Anantapur','country':'India'}
#mydata['mobile']=9347684941
#printPerson(mydata)
userdata={}
e=1
while e!='0':
    userkey=input("Enter a key:")
    uservalue=input("Enter a value:")
    userdata[userkey]=uservalue
    e=input("press 0 to end or enter any key to continue to adding...")
printPerson(userdata)