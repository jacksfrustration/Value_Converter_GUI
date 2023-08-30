from tkinter import *
from tkinter import messagebox

#outputs the result of the conversion
def miles_to_km(first_value):
   return round(first_value * 1.60934, 2)

#outputs the result of the conversion
def meters_to_feet(first_value):
    return round(first_value * 3.28084,2)

#outputs the result of the conversion
def feet_to_meters(first_value):
   return round (first_value * 0.3048,2)

#outputs the result of the conversion
def km_to_miles(first_value):
   return round(first_value * 0.621371)

#outputs the result of the conversion
def kilos_to_pounds(first_value):
   return round(first_value * 2.20462, 2)


#outputs the result of the conversion
def celcius_to_farenheit(first_value):
    return round((first_value * 9/5) + 32,2)

#outputs the result of the conversion
def farenheit_to_celsius(first_value):
   return round ((first_value -32) * 5/9,2)

#outputs the result of the conversion
def pounds_to_kilos(first_value):
    return round (first_value * 0.45359237,2 )

def process(_event):
    try:
    #assign the first value to a variable
        initial_value=float(first_value_entry.get())
    except ValueError:
        initial_value=first_value_entry.get()
        messagebox.showerror(title="Oops",message=f"{initial_value} is not a number")

    #assign the option menu output to variable
    values=value_inside.get()

    #trigger the appropriate conversion formula
    #based on the option menu output
    if values=="Miles to Kilometers":
        result=miles_to_km(initial_value)
        #output result of the formula
        messagebox.showinfo(title="Conversion Result",message=f"{initial_value} miles equals {result} Kilometers")
    elif values=="Meters to Feet":
        result=meters_to_feet(initial_value)
        #output result of the formula
        messagebox.showinfo(title="Conversion Result",message=f"{initial_value} Meters equals {result} Feet")

    elif values=="Feet to Meters":
        result=feet_to_meters(initial_value)
        #output result of the formula
        messagebox.showinfo(title="Conversion Result",message=f"{initial_value} Feet equals {result} Meters")

    elif values=="Kilometers to Miles":
        result=km_to_miles(initial_value)
        #output result of the formula
        messagebox.showinfo(title="Conversion Result",message=f"{initial_value} Kilometers equals {result} Miles")

    elif values=="Kilos to Pounds":
        result=kilos_to_pounds(initial_value)
        #output result of the formula
        messagebox.showinfo(title="Conversion Result",message=f"{initial_value} Kilos equals {result} Pounds")

    elif values=="Celsius to Farneheit":
        result=celcius_to_farenheit(initial_value)
        #output result of the formula
        messagebox.showinfo(title="Conversion Result",message=f"{initial_value} Celsius equals {result} Farenheit")

    elif values=="Farenheit to Celsius":
        result=farenheit_to_celsius(initial_value)
        #output result of the formula
        messagebox.showinfo(title="Conversion Result",message=f"{initial_value} Farenheit equals {result} Celsius")
    elif values=="Pounds to Kilos":
        result=pounds_to_kilos(initial_value)
        # output result of the formula
        messagebox.showinfo(title="Conversion Result", message=f"{initial_value} Pounds equals to {result} Kilos")


window=Tk()
window.title("Values Converter")
window.config(padx=25,pady=25)
canvas=Canvas()
first_value=Label(text="First Value:")
first_value.grid(row=0,column=0)

first_value_entry=Entry()
first_value_entry.grid(row=1,column=0)

value_inside=StringVar(window)
values=OptionMenu(window,value_inside, "Miles to Kilometers","Kilometers to Miles","Meters to Feet",
         "Feet to Meters","Kilos to Pounds","Pounds to Kilos",
         "Celsius to Farneheit","Farenheit to Celsius")
values.grid(row=2,column=0)

convert_button=Button(text="Convert",command=process)
convert_button.grid(row=1,column=1)
window.bind("<Return>",process)

window.mainloop()