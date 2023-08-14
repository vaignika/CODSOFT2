import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# GUI setup
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x550")
root.configure(bg="black")  # Set the background color to black

entry = tk.Entry(root, font=("Arial", 30), bd=0, relief=tk.FLAT, justify=tk.RIGHT)
entry.pack(pady=20, padx=10, ipadx=8, ipady=8)

button_frame = tk.Frame(root, bg="black")  # Set the frame background color to black
button_frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

for i in range(len(buttons)):
    if buttons[i] == "=":
        button = tk.Button(button_frame, text=buttons[i], font=("Arial", 20), padx=30, pady=30, bd=0, relief=tk.GROOVE, bg="#FFA500", activebackground="#FF8C00")
    else:
        button = tk.Button(button_frame, text=buttons[i], font=("Arial", 20), padx=30, pady=30, bd=0, relief=tk.GROOVE, bg="#D8D8D8", activebackground="#B0B0B0")
    button.grid(row=i // 4, column=i % 4, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", on_button_click)

button_frame.columnconfigure((0, 1, 2, 3), weight=1)
button_frame.rowconfigure((0, 1, 2, 3, 4), weight=1)

root.mainloop
