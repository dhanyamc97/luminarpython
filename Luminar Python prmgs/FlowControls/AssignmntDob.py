
d_date=int(input("Enter Born Date"))
d_mnth=int(input("Enter Born Month"))
d_year=int(input("Enter Born Year"))


c_date=int(input("Enter Today's Date"))
c_mnth=int(input("Enter Current Month"))
c_year=int(input("Enter Current Year"))

if(c_year>d_year):
    if(c_mnth>=d_mnth):
        print("Age= ",c_year-d_year)
    else:
        print("Age= ",(c_year-1)-d_year)
else:
    print("Year is not appropriate")

