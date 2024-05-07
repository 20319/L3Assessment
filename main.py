# Import necessary modules
import tkinter as tk  # Import tkinter module as tk
from tkinter import messagebox  # Import messagebox from tkinter

# Define the submit_input function
def submit_input():
    # Check if all input fields are filled
    if not all((entry_bedrooms.get(), entry_lounges.get(), entry_bathrooms.get(), 
                entry_toilets.get(), entry_pools.get(), entry_sqm.get(), risk_var.get())):
        messagebox.showerror("Error", "Please fill in all the input fields")
    # Check if risk factor is selected
    elif not risk_var.get():
        messagebox.showerror("Error", "Please select a risk factor")
    else:
        # Get the values entered by the user and convert them to integers
        bedrooms = int(entry_bedrooms.get())
        lounges = int(entry_lounges.get())
        bathrooms = int(entry_bathrooms.get())
        toilets = int(entry_toilets.get())
        pools = int(entry_pools.get())
        sqm = int(entry_sqm.get())
        
        # Initialize the initial cost and calculate the total cost based on inputs
        initial_cost = 50
        total = initial_cost + (bedrooms * 50) + (lounges * 25) + (bathrooms * 50) + (toilets * 25) + (pools * 150)

        # Calculate cost based on square meters
        if sqm > 200:
            sqm = sqm * 2.75
        elif sqm > 150:
            sqm = sqm * 2

        total += sqm

        # Calculate risk factor based on the selected option
        risk = risk_var.get()
        if risk == "3":
            riskpercent = total * 0.04
        elif risk == "2":
            riskpercent = total * 0.03
        else:
            riskpercent = total * 0.02

        total += riskpercent

        # Calculate GST (Goods and Services Tax)
        gst = total * 0.15
        total += gst

        # Display the total cost in the result label
        result_label.config(text=f"Total Cost (including GST): {total}")

# Create the main tkinter window
window = tk.Tk()
window.title("McLeod's House Rental Company")  # Set the window title
window.geometry("400x500")  # Set the window size
window.configure(background='#bedafa')  # Set the window background color
window.option_add('*Font', 'Georgia 10')

# Load and display an image
image_path = "path/to/your/image.png"  # Replace this with the actual path to your image
img = tk.PhotoImage(file=image_path)  # Load the image using PhotoImage
image_label = tk.Label(window, image=img, bg='#bedafa')
image_label.pack()
# Create labels and entry fields for input
# Rest of your existing code for labels and entry fields goes here...

# Run the tkinter main loop
window.mainloop()

# Create labels and entry fields for input
label_bedrooms = tk.Label(window, text="Number of Bedrooms:", bg='#bedafa', fg='black')
label_bedrooms.pack()

entry_bedrooms = tk.Entry(window)
entry_bedrooms.pack()

label_lounges = tk.Label(window, text="Number of Lounges:", bg='#bedafa', fg='black')
label_lounges.pack()

entry_lounges = tk.Entry(window)
entry_lounges.pack()

label_bathrooms = tk.Label(window, text="Number of Bathrooms:", bg='#bedafa', fg='black')
label_bathrooms.pack()

entry_bathrooms = tk.Entry(window)
entry_bathrooms.pack()

label_toilets = tk.Label(window, text="Number of Toilets:", bg='#bedafa', fg='black')
label_toilets.pack()

entry_toilets = tk.Entry(window)
entry_toilets.pack()

label_pools = tk.Label(window, text="Number of Pools:", bg='#bedafa', fg='black')
label_pools.pack()

entry_pools = tk.Entry(window)
entry_pools.pack()

label_sqm = tk.Label(window, text="Square Meters:", bg='#bedafa', fg='black')
label_sqm.pack()

entry_sqm = tk.Entry(window)
entry_sqm.pack()

# Create labels and radio buttons for selecting the risk factor
label_risk = tk.Label(window, text="Risk Factor:", bg='#bedafa', fg='black')
label_risk.pack()

risk_var = tk.StringVar(value=None)  
radio_high = tk.Radiobutton(window, text="High", variable=risk_var, value="3", bg='#bedafa')
radio_high.pack()

radio_medium = tk.Radiobutton(window, text="Medium", variable=risk_var, value="2", bg='#bedafa')
radio_medium.pack()

radio_low = tk.Radiobutton(window, text="Low", variable=risk_var, value="1", bg='#bedafa')
radio_low.pack()

# Create a button to calculate the total cost
submit_button = tk.Button(window, text="Calculate", command=submit_input, bg='#3366cc', fg='white')
submit_button.pack()

# Create a label to display the result
result_label = tk.Label(window, text="", bg='#bedafa', fg='black')
result_label.pack()

# Create a function to clear all input fields and reset radiobuttons
def clear_input():
    entry_bedrooms.delete(0, tk.END)
    entry_lounges.delete(0, tk.END)
    entry_bathrooms.delete(0, tk.END)
    entry_toilets.delete(0, tk.END)
    entry_pools.delete(0, tk.END)
    entry_sqm.delete(0, tk.END)
    result_label.config(text="")
    risk_var.set(0)

# Create a button to clear all input fields
clear_button = tk.Button(window, text="Clear", command=clear_input, bg='#3366cc', fg='white')
clear_button.pack()

# Run the tkinter main loop
window.mainloop()