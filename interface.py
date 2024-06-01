import shutil
import tkinter as tk
from tkinter import filedialog
import os
from main import run
from seperate import split_logs

global analyst_logs, researcher_logs, recommender_logs

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        # Predefined name for the file
        predefined_name = "blood_report.pdf"
        
        # Destination directory
        destination_dir = "src\chatapp_crew\data"
        
        # Construct the destination path
        destination_path = destination_dir + "\\" + predefined_name

        print(f"Selected file: {file_path}")
        print(f"Destination path: {destination_path}")
        # Copy the selected file to the destination path
        shutil.copy(file_path, destination_path)

        browse_button.config(background="green")
        start_button.config(state=tk.NORMAL)
    else:
        # Show a pop-up box with the message
        tk.messagebox.showinfo("File Not Selected", "Please select a file before proceeding.")

def start_process():
    global analyst_logs, researcher_logs, recommender_logs
    # delete the logs file if it exists
    try:
        os.remove("logs.txt")
    except FileNotFoundError:
        pass

    # Run the main function
    run()

    # Split the logs
    analyst_logs, researcher_logs, recommender_logs = split_logs('logs.txt')

    # Clear the text area
    process_text.delete(1.0, tk.END)
    process_text.insert(tk.END, f"Parsing complete. Please select an agent to view their findings.")

    # Enable the buttons
    analyst_button.config(state=tk.NORMAL)
    researcher_button.config(state=tk.NORMAL)
    recommender_button.config(state=tk.NORMAL)

def show_analyst_logs():
    process_text.delete(1.0, tk.END)  # Clear the text area
    process_text.insert(tk.END, f"\n\nAnalyst Findings:\n\n{analyst_logs}")

def show_researcher_logs():
    process_text.delete(1.0, tk.END)  # Clear the text area
    process_text.insert(tk.END, f"\n\nResearcher Findings:\n\n{researcher_logs}")

def show_recommender_logs():
    process_text.delete(1.0, tk.END)  # Clear the text area
    process_text.insert(tk.END, f"\n\nRecommender Findings:\n\n{recommender_logs}")

# Create the main window
window = tk.Tk()

# Create a button to browse for a file
browse_button = tk.Button(window, text="Browse", command=browse_file)
browse_button.pack()

# Create a button to start the process
start_button = tk.Button(window, text="Start", command=start_process, state=tk.DISABLED)
start_button.pack()

# Create buttons for each agent's findings
analyst_button = tk.Button(window, text="Analyst", command=show_analyst_logs, state=tk.DISABLED)
analyst_button.pack()

researcher_button = tk.Button(window, text="Researcher", command=show_researcher_logs, state=tk.DISABLED)
researcher_button.pack()

recommender_button = tk.Button(window, text="Recommender", command=show_recommender_logs, state=tk.DISABLED)
recommender_button.pack()

# Create a text area to display the selected agent's findings
process_text = tk.Text(window)
process_text.pack()

# Run the GUI
window.mainloop()