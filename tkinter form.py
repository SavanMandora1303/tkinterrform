from tkinter import *

def getvals():
    print("form submitted")
    with open("record.txt","a") as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentvalue.get(),foodvalue.get()}\n")


root = Tk()
root.geometry("500x500")
# root.minsize(500, 500)
root.maxsize(500, 500)
root.title("Tkinter Form")

# Text for our form
name = Label(root, text="Name")
phone = Label(root, text="Phone No.")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact no.")
payment = Label(root, text="Payment Mode ")

# packing all items
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
payment.grid(row=5, column=2)

# variable for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentvalue = StringVar()
foodvalue = IntVar()

#entries for our form
name_entry = Entry(root, textvariable=namevalue).grid(row=1, column=3)
phone_entry = Entry(root, textvariable=phonevalue).grid(row=2, column=3)
gender_entry = Entry(root, textvariable=gendervalue).grid(row=3, column=3)
emergency_entry = Entry(root, textvariable=emergencyvalue).grid(row=4, column=3)
payment_entry = Entry(root, textvariable=paymentvalue).grid(row=5, column=3)


#checkBox and packing it
foodservices = Checkbutton(text="Want to prebook your meal ?", variable=foodvalue)
foodservices.grid(row=6, column=3)


#submit button and packing it
submit = Button(root, text="Submit", command=getvals)
submit.grid(row=7, column=3)

root.mainloop()
