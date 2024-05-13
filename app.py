import tkinter as tk
import subprocess

def execute_code():
    user_input = input_text.get("1.0", tk.END)

    with open("plsCode.txt", 'w') as f:
        f.write(user_input)

    # Wykonaj kod w terminalu
    result = subprocess.run("python Driver.py", shell=True, capture_output=True, text=True)

    # Wyświetl wyniki w terminalu
    terminal_output.config(state=tk.NORMAL)
    terminal_output.delete("1.0", tk.END)
    terminal_output.insert(tk.END, f"${result.stdout}{result.stderr}")
    terminal_output.config(state=tk.DISABLED)

def on_tab_pressed(event):
    input_text.insert(tk.INSERT, "    ")
    return 'break'

root = tk.Tk()
root.title("PLScript")

top_frame = tk.Frame(root)
top_frame.pack(fill=tk.BOTH, expand=True)

top_frame.grid_rowconfigure(0, weight=1)  # Wiersz 0 - input_text
top_frame.grid_columnconfigure(0, weight=1)  # Kolumna 0 - input_text
top_frame.grid_columnconfigure(1, weight=0)  # Kolumna 1 - input_scroll

input_text = tk.Text(top_frame, bg="black", fg="white", insertbackground="white")
input_text.grid(row=0, column=0, sticky="nsew")

input_scroll = tk.Scrollbar(top_frame, orient=tk.VERTICAL, command=input_text.yview, width=20)
input_scroll.grid(row=0, column=1, sticky="ns")

# Przypisz pasek przewijania do pola tekstowego
input_text.config(yscrollcommand=input_scroll.set)

input_text.bind("<Tab>", on_tab_pressed)

# Utwórz przycisk do wykonania kodu
execute_button = tk.Button(top_frame, text="Wykonaj kod", command=execute_code)
execute_button.grid(row=1, column=0, sticky="s")

# Utwórz ramkę dla dolnego obszaru aplikacji (gdzie jest terminal)
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill=tk.BOTH, expand=True)

# Utwórz terminal (pole tekstowe tylko do odczytu)
terminal_output = tk.Text(bottom_frame, state=tk.DISABLED)
terminal_output.pack(fill=tk.BOTH, expand=True)

# Uruchom pętlę główną aplikacji
root.mainloop()
