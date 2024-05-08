# Import necessary modules
import tkinter as tk  # Import tkinter module as tk
from tkinter import messagebox  # Import messagebox from tkinter

# Define global variables for tracking calculations
num_calculations = 0
total_cost = 0
total_sqm = 0  # New global variable for total square meters

# Define the submit_input function
def submit_input():
    global invalid_inputs, num_calculations, total_cost, total_sqm  # Add total_sqm to global variables
    invalid_inputs = 0  # Reset the count of invalid inputs for each submit
    num_calculations += 1  # Increment the number of calculations

    # Validate all input fields
    if not all((validate_input(entry_bedrooms.get()), validate_input(entry_lounges.get()), validate_input(entry_bathrooms.get()), 
                validate_input(entry_toilets.get()), validate_input(entry_pools.get()), validate_input(entry_sqm.get()), risk_var.get())):
        messagebox.showerror("Error", "Please enter valid integer values for all input fields")
    # If there are any invalid inputs, do not proceed
    if invalid_inputs > 0:
        return
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
            sqm_cost = sqm * 2.75
        elif sqm > 150:
            sqm_cost = sqm * 2
        else:
            sqm_cost = sqm

        total += sqm_cost

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

        # Calculate the total cost/average cost
        total_cost += total
        average_cost = total_cost / num_calculations

        # Update total square meters
        total_sqm += sqm

        # Calculate the average square meters
        average_sqm = total_sqm / num_calculations

        # Display the total cost in the result label
        result_label.config(text=f"Total Cost (including GST): ${total:.2f}")

        # Display the average cost in the average result label
        average_result_label.config(text=f"Average Cost: ${average_cost:.2f}")

        # Display the average square meters in the sqm result label
        sqm_result_label.config(text=f"Average Square Meters: {average_sqm:.2f}")

        # Display the number of calculations made
        calculations_label.config(text=f"Number of Calculations: {num_calculations}")

# Function to validate if the input is an integer
invalid_inputs = 0  # Track the number of invalid inputs
num_calculations = 0  # Track the number of calculations
def validate_input(entry):
    global invalid_inputs
    if entry.isdigit():
        return True
    else:
        invalid_inputs += 1
        return False

# Create the main tkinter window
window = tk.Tk()
window.title("McLeod's House Rental Company")  # Set the window title
window.geometry("400x550")  # Set the window size
window.configure(background='#bedafa')  # Set the window background color
window.option_add('*Font', 'Georgia 10')

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

# Create a label to display the average cost
average_result_label = tk.Label(window, text="", bg='#bedafa', fg='black')
average_result_label.pack()

# Create a label to display the average square meters
sqm_result_label = tk.Label(window, text="", bg='#bedafa', fg='black')
sqm_result_label.pack()

# Create a function to clear all input fields and reset radiobuttons
def clear_input():
    entry_bedrooms.delete(0, tk.END)
    entry_lounges.delete(0, tk.END)
    entry_bathrooms.delete(0, tk.END)
    entry_toilets.delete(0, tk.END)
    entry_pools.delete(0, tk.END)
    entry_sqm.delete(0, tk.END)
    result_label.config(text="")
    average_result_label.config(text="")
    sqm_result_label.config(text="")
    risk_var.set(0)

# Create a button to clear all input fields
clear_button = tk.Button(window, text="Clear", command=clear_input, bg='#3366cc', fg='white')
clear_button.pack()

# Create a label to display the number of calculations
calculations_label = tk.Label(window, text="Number of Calculations: 0", bg='#bedafa', fg='black')
calculations_label.pack()

# Run the tkinter main loop
window.mainloop()
