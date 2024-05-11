import tkinter as tk  # Import the tkinter library with an alias 'tk'
from tkinter import messagebox  # Import the messagebox module from tkinter

# Define global variables for tracking calculations
num_calculations = 0  # Initialize a global variable to track the number of calculations
total_cost = 0  # Initialize a global variable to track the total cost
total_sqm = 0  # Initialize a global variable to track the total square meters

# Create the main tkinter window
window = tk.Tk()  # Create a Tkinter window
window.title("McLeod's House Rental Company")  # Set the window title
window.geometry("400x550")  # Set the window size
window.configure(background='#bedafa')  # Set the background color
window.option_add('*Font', 'Georgia 10')  # Set default font for all widgets

# Define initial value for risk_var
risk_var = tk.StringVar(value="")  # Set initial value to None

# Create a label for the title
title_label = tk.Label(window, text="McLeod's Rental Agency", bg='#bedafa', fg='black', font=('Georgia', 16, 'bold'))
title_label.pack(pady=10)  # Place the title label in the window with padding

# Define the submit_input function
def submit_input():
    """
    Function to handle the submission of input and calculate the total cost.
    """
    global num_calculations, total_cost, total_sqm  # Access global variables

    # Validate all input fields
    valid_inputs = [validate_input(entry.get()) for entry in (entry_bedrooms, entry_lounges, entry_bathrooms, entry_toilets, entry_pools, entry_sqm)]
    if not all(valid_inputs):
        messagebox.showerror("Error", "Please enter valid integer values for all input fields")
        return  # Exit the function if any input is invalid

    # Check if a risk factor is selected
    if risk_var.get() == "":
        messagebox.showerror("Error", "Please select a risk factor")
        return  # Exit the function if no risk factor is selected

    # Increment the number of calculations if all inputs are valid and a risk factor is selected
    num_calculations += 1

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

    # Update total square meters & Calculate average
    total_sqm += sqm
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
invalid_inputs = 0  # Initialize a variable to count invalid inputs
def validate_input(entry):
    """
    Function to validate if the input is an integer.

    Args:
    entry (str): The input to be validated.

    Returns:
    bool: True if the input is an integer, False otherwise.
    """
    global invalid_inputs  # Access global variable
    if entry.isdigit():
        return True  # Return True if the input is an integer
    else:
        invalid_inputs += 1  # Increment invalid input count
        return False  # Return False if the input is not an integer

# Create labels and entry fields for input
label_bedrooms = tk.Label(window, text="Number of Bedrooms:", bg='#bedafa', fg='black')
label_bedrooms.pack()  # Place the label for bedrooms

entry_bedrooms = tk.Entry(window)  # Create entry field for bedrooms
entry_bedrooms.pack()  # Place the entry field for bedrooms

label_lounges = tk.Label(window, text="Number of Lounges:", bg='#bedafa', fg='black')
label_lounges.pack()  # Place the label for lounges

entry_lounges = tk.Entry(window)  # Create entry field for lounges
entry_lounges.pack()  # Place the entry field for lounges

label_bathrooms = tk.Label(window, text="Number of Bathrooms:", bg='#bedafa', fg='black')
label_bathrooms.pack()  # Place the label for bathrooms

entry_bathrooms = tk.Entry(window)  # Create entry field for bathrooms
entry_bathrooms.pack()  # Place the entry field for bathrooms

label_toilets = tk.Label(window, text="Number of Toilets:", bg='#bedafa', fg='black')
label_toilets.pack()  # Place the label for toilets

entry_toilets = tk.Entry(window)  # Create entry field for toilets
entry_toilets.pack()  # Place the entry field for toilets

label_pools = tk.Label(window, text="Number of Pools:", bg='#bedafa', fg='black')
label_pools.pack()  # Place the label for pools

entry_pools = tk.Entry(window)  # Create entry field for pools
entry_pools.pack()  # Place the entry field for pools

label_sqm = tk.Label(window, text="Square Meters:", bg='#bedafa', fg='black')
label_sqm.pack()  # Place the label for square meters

entry_sqm = tk.Entry(window)  # Create entry field for square meters
entry_sqm.pack()  # Place the entry field for square meters

# Create labels and radio buttons for selecting the risk factor
label_risk = tk.Label(window, text="Risk Factor:", bg='#bedafa', fg='black')
label_risk.pack()  # Place the label for risk factor

risk_options = [("High", "3"), ("Medium", "2"), ("Low", "1")]  # Define options for risk factor

# Create radio buttons using a loop
for text, value in risk_options:
    radio_button = tk.Radiobutton(window, text=text, variable=risk_var, value=value, bg='#bedafa')
    radio_button.pack()  # Place the radio button

# Create a button to calculate the total cost
submit_button = tk.Button(window, text="Calculate", command=submit_input, bg='#3366cc', fg='white')
submit_button.pack()  # Place the submit button

# Create a label to display the result
result_label = tk.Label(window, text="", bg='#bedafa', fg='black')
result_label.pack()  # Place the label for result

# Create a label to display the average cost
average_result_label = tk.Label(window, text="", bg='#bedafa', fg='black')
average_result_label.pack()  # Place the label for average result

# Create a label to display the average square meters
sqm_result_label = tk.Label(window, text="", bg='#bedafa', fg='black')
sqm_result_label.pack()  # Place the label for square meter result

# Create a function to clear all input fields and reset radiobuttons
def clear_input():
    """
    Function to clear all input fields and reset radio buttons.
    """
    entry_bedrooms.delete(0, tk.END)  
    entry_lounges.delete(0, tk.END)  
    entry_bathrooms.delete(0, tk.END)  
    entry_toilets.delete(0, tk.END)  
    entry_pools.delete(0, tk.END)  
    entry_sqm.delete(0, tk.END)  
    result_label.config(text="")  

    # Reset the risk variable
    risk_var.set("")  # Reset risk_var to None

# Create a button to clear all input fields
clear_button = tk.Button(window, text="Clear", command=clear_input, bg='#3366cc', fg='white')
clear_button.pack()  # Place the clear button

# Create a label to display the number of calculations
calculations_label = tk.Label(window, text="Number of Calculations: 0", bg='#bedafa', fg='black')
calculations_label.pack()  # Place the label for number of calculations

# Run the tkinter main loop
window.mainloop()  # Start the main event loop