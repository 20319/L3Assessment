# Import the necessary module
import tkinter as tk

# Define the function to handle input submission
def submit_input():
    # Get the number of bedrooms, lounges, bathrooms, toilets, and pools from the input fields
    bedrooms = int(entry_bedrooms.get())
    lounges = int(entry_lounges.get())
    bathrooms = int(entry_bathrooms.get())
    toilets = int(entry_toilets.get())
    pools = int(entry_pools.get()
    
    # Print the information entered by the user
    print(f"Number of Bedrooms: {bedrooms}")
    print(f"Number of Lounges: {lounges}")
    print(f"Number of Bathrooms: {bathrooms}")
    print(f"Number of Toilets: {toilets}")
    print(f"Number of Pools: {pools}")

# Create the main window
window = tk.Tk()
window.title("House Rental Company")
window.geometry("400x300")

# Create labels and entry fields for bedrooms, lounges, bathrooms, toilets, and pools
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

# Create a Submit button to trigger the submission function
submit_button = tk.Button(text="Submit", command=submit_input)
submit_button.pack()

# Start the GUI main loop
window.mainloop()