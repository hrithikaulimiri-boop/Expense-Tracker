import css 
b = []
p = []
def expense():
    l = []
    while(l!=[4,2,2]):
        date = input("Please enter date of expense(YYYY-MM-DD):")
        i = 0
        c = 0
        l = []
        for a in date:
            if(a=="-"):
                l.append(i)
                i = 0
            elif(c==(len(date)-1)):
                i = i + 1
                l.append(i)
            else:
               i = i + 1
            c = c + 1
    cat = input("What is your category of expense?(food/travel)")
    amt = float(input("Enter amount of expense:"))
    desc = input("Describe your expense briefly")
    exp = {'date':date, 'category':cat, 'amount': amt, 'description':desc}
    p.append(int(exp['amount']))
    for x in exp.values():
        b.append(x)
def view():
    for x in b:
        if(x==""):
            print("Incomplete entry")
        else:
            print(x)

def budget():
    a = int(input("Enter your monthly budget:"))
    s = 0
    for x in p:
        s = s+x
    if(s>a):
        print("Warning! Monthly budget exceeded!")
    elif(s<a):
        print("You have {} remaining!".format(a-s))
    
        
    

def save():
    with open('output.csv',mode = 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date','Category','Amt','Desc'])
        for i in range(0,len(b),4):
            writer.writerow(b[i:i+4])
    with open('output.csv', newline = '') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def menu():
    e = 0
    while(e!=5):
        e = int(input("Select one option(1-5):\n1.Add Expense\n2.View Expenses\n3.Track budget\n4.Save Expenses\n5.Exit\n"))
        if(e==1):
            expense()
        elif(e==2):
            view()
        elif(e==3):
            budget()
        elif(e==4):
            save()
        else:
            break

menu()
