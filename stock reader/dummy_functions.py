import customtkinter as ctk

app = ctk.CTk()
app.geometry("300x200")
app.title("Login (pack)")
################################# USER NAME LOGIN START ###############################
# frame = ctk.CTkFrame(app)
# frame.pack(padx=20, pady=20, fill="both", expand=True)

# label_user = ctk.CTkLabel(frame, text="Username:")
# label_user.pack(pady=5)

# entry_user = ctk.CTkEntry(frame, placeholder_text="Enter username")
# entry_user.pack(pady=5)

# label_pass = ctk.CTkLabel(frame, text="Password:")
# label_pass.pack(pady=5)

# entry_pass = ctk.CTkEntry(frame, placeholder_text="Enter password", show="*")
# entry_pass.pack(pady=5)

# button_login = ctk.CTkButton(frame, text="Login")
# button_login.pack(pady=10)



################################# USER NAME LOGIN ENDS ###############################

frame = ctk.CTkFrame(app)
frame.grid(padx=20, pady=20, sticky="nsew")

# Configure grid columns for better resizing
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=2)

ctk.CTkLabel(frame, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_user = ctk.CTkEntry(frame, placeholder_text="Enter username")
entry_user.grid(row=0, column=1, padx=10, pady=5, sticky="we")

ctk.CTkLabel(frame, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_pass = ctk.CTkEntry(frame, placeholder_text="Enter password", show="*")
entry_pass.grid(row=1, column=1, padx=10, pady=5, sticky="we")

button_login = ctk.CTkButton(frame, text="Login")
button_login.grid(row=2, column=0, columnspan=2, pady=10)















app.mainloop()