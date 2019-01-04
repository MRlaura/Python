age1 = 18
age2 = 15
age3 = 21
m_age = 18
if age1 >= m_age:
     print ("You have the majority age required")
     if True:
          print ("This is executed, every time it has the majority age required")
else:
    print ("You don’t have the majority age required")

print ("Hello! This will always be executed")

if age3 >= m_age:
     print ("You have the majority age required")
     if False:
          print ("This is executed, every time it doesn’t has the majority age required")
     else:
          print ("Anything")
else:
    print ("You don’t have the majority age required")
if age2 >= m_age:
     print ("You have the majority age required")
else:
    print ("You don’t have the majority age required")
