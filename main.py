# Import the necessary module
import tkinter as tk
from tkinter import messagebox

def submit_input():
  if not entry_bedrooms.get() or not entry_lounges.get() or not entry_bathrooms.get() or not entry_toilets.get() or not entry_pools.get() or not entry_sqm.get() or not risk_var.get():
      messagebox.showerror("Error", "Please fill in all the input fields")
  elif not risk_var.get():
      messagebox.showerror("Error", "Please select a risk factor")
  else:
      bedrooms = int(entry_bedrooms.get())
      lounges = int(entry_lounges.get())
      bathrooms = int(entry_bathrooms.get())
      toilets = int(entry_toilets.get())
      pools = int(entry_pools.get())
      sqm = int(entry_sqm.get())
    
  # Calculate the total cost based on the inputs
  initial_cost = 50
  total = initial_cost + (bedrooms * 50) + (lounges * 25) + (bathrooms * 50) + (toilets * 25) + (pools * 150)

  # Calculate the price based on square meters
  if sqm > 200:
      sqm = sqm * 2.75
  elif sqm > 150:
      sqm = sqm * 2
  
  total = total + sqm
  
  # Calculate the risk factor based on the selected option
  risk = risk_var.get()
  if risk == "3":
      riskpercent = total * 0.04
  elif risk == "2":
      riskpercent = total * 0.03
  else:
      riskpercent = total * 0.02
  
  total = total + riskpercent
  
  # Calculate GST (Goods and Services Tax)
  gst = total * 0.15
  total = total + gst
  
  # Display the results in the tkinter window
  result_label.config(text=f"Total Cost (including GST): {total}")
  
# Create the main window
window = tk.Tk()
window.title("House Rental Company")
window.geometry("400x500")

# Create labels and entry fields for bedrooms, lounges, bathrooms, toilets, pools, and square meters
label_bedrooms = tk.Label(text="Enter number of Bedrooms")
label_bedrooms.pack()
entry_bedrooms = tk.Entry()
entry_bedrooms.pack()

label_lounges = tk.Label(text="Enter number of Lounges")
label_lounges.pack()
entry_lounges = tk.Entry()
entry_lounges.pack()

label_bathrooms = tk.Label(text="Enter number of Bathrooms")
label_bathrooms.pack()
entry_bathrooms = tk.Entry()
entry_bathrooms.pack()

label_toilets = tk.Label(text="Enter number of Toilets")
label_toilets.pack()
entry_toilets = tk.Entry()
entry_toilets.pack()

label_pools = tk.Label(text="Enter number of Pools")
label_pools.pack()
entry_pools = tk.Entry()
entry_pools.pack()

label_sqm = tk.Label(text="Enter square meters")
label_sqm.pack()
entry_sqm = tk.Entry()
entry_sqm.pack()

# Create a label and radio buttons for selecting the risk factor
label_risk = tk.Label(text="Select the risk factor:")
label_risk.pack()

risk_var = tk.StringVar(value=None)  # Initialize risk_var as None
radio_high = tk.Radiobutton(window, text="High", variable=risk_var, value="3")
radio_high.pack()
radio_medium = tk.Radiobutton(window, text="Medium", variable=risk_var, value="2")
radio_medium.pack()
radio_low = tk.Radiobutton(window, text="Low", variable=risk_var, value="1")
radio_low.pack()

# Create a Submit button to trigger the submission function
submit_button = tk.Button(text="Submit", command=submit_input)
submit_button.pack()

# Create a label to display the output
result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI main loop
window.mainloop()