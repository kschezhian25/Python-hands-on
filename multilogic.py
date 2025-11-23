class multifun():
    def Subfields():
        list_AI=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for item in list_AI:
            print(item)
#        return list_AI
        
    def OddEven():
        user_in=int(input("Enter the Number:")) 
        if user_in % 2==0:
            msg= str(user_in)+" is even number"
#            print(msg)
        else:
            msg= str(user_in)+" is odd number"
#           print(msg)
        return msg

    def Elegible():
        in_gen=input("Your Gender:")
        in_age=int(input("Your age:"))
        if in_gen=="male" and in_age<21:
            msg="Not Eligible"
 #           print(msg)
        elif in_gen=="female" and in_age<18:
            msg="Not Eligible"
 #           print(msg)
        elif (in_gen=="male" and in_age>=21) or (in_gen=="female" and in_age>=18):
            msg="Eligible"
 #           print(msg)
        else:
             msg="Enter details Gender or age is incorrect"
 #            print(msg)

        return msg 

    def percentage():
        in1=int(input("Subject1:"))
        in2=int(input("Subject2:"))
        in3=int(input("Subject3:"))
        in4=int(input("Subject4:"))
        in5=int(input("Subject5:"))
        total = in1+in2+in3+in4+in5
        print("total:",total)
        percentage=(total/500)*100
        print("percentage:",percentage)
        msg=f"Total = {total}\n percentage={percentage}"
        return msg

    def triangle():
        h=int(input("Height:"))
        b=int(input("Breath:"))
        area_tri = (h*b)/2
        print("Area of triange:",area_tri)
        h1=int(input("Height1:"))
        h2=int(input("Height2:"))
        b=int(input("breath:"))
        peri_tri = h1+h2+b
        print("Area of triangle:",peri_tri)
        msg = f"Area of triangle = {area_tri}\nPerimeter of triangle = {peri_tri}"
        return msg
        
        