mark=int(input("Enter Mark:"))
if(mark>=80 and mark<100):
    print("A+ Grade")
elif(mark>70 and mark<=80):
    print("A grade")
elif(mark>=60 and mark<70):
    print("A- Grade")
elif(mark>=50 and mark<60):
    print("B Grade")
elif(mark>=40 and mark<50):
    print("C Grade")
elif(mark>=33 and mark<40):
    print("D Grade")
elif(mark>=0 and mark<33):
    print("F Grade")
else:
    print("Invalid Mark")