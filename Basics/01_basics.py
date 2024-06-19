#this program takes month number as a input from the keyboard and print month name and no.days in the month
print("hello python")
# year=int(input("enter the year:"))
month_number=int(input("enter the month number"))
month_list=["January","february","march","April","may",'June','july',"august","september","0ctober","november","december"]
if(month_number==1):
   print(f"months name is {month_list[month_number-1]}")
   print("no. of days in month=31")
elif(month_number==2 ):
    year=int(input("enter the year:"))
    if ((year %4==0 or year%400==0) and (year%100!=0)):
        print(f"month_name is {month_list[month_number-1]}")
        print("no. of days in month=29")
    else:
        print(f"month_name is {month_list[month_number-1]}")
        print("no. of days in month=28")
elif(month_number %2==0 and month_number!=2):
    print(f"month's name is {month_list[month_number-1]}")
    print("no. of days in month=30")
elif(month_number %2!=0 ):
    print(f"month's name is {month_list[month_number-1]}")
    print("no. of days in month=31")
else:
    print("Some Error has occured ,\n try Again")


        


