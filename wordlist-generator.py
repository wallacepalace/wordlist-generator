import tkinter as tk
from tkinter import ttk, scrolledtext, font
from itertools import product
from tkinter import messagebox

class BootstrapStyle(ttk.Style):
    def __init__(self):
        super().__init__()
        self.theme_create("bootstrap", parent="alt", settings={
            "TButton": {
                "configure": {"padding": 10, "borderwidth": 5, "relief": "flat", "background": "#007BFF", "foreground": "#FFFFFF", "font": ("Ubuntu", 12), "anchor": "center"},
                "map": {"background": [("active", "#0056b3"), ("pressed", "#0056b3")]}
            }
        })
        self.theme_use("bootstrap")

class WordlistGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("GERADOR DO PAPAI")
        master.geometry("457x638")
        master.configure(bg="#1E1E1E")
        master.resizable(False, False)
        master.tk_setPalette(background="#1E1E1E", foreground="#FFFFFF", activeBackground="#4CAF50", activeForeground="#FFFFFF")

        font.nametofont("TkDefaultFont").configure(family="Ubuntu", size=12)
        BootstrapStyle()

        self.label = ttk.Label(master, text="DIGITE A PALAVRA DEFAULT:", font=("Ubuntu", 12), foreground="#FFFFFF", background="#1E1E1E")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry = ttk.Entry(master, font=("Ubuntu", 12))
        self.entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.generate_button = ttk.Button(master, text="GERAR WORDLIST", command=self.generate_wordlist, style="TButton")
        self.generate_button.grid(row=1, column=0, padx=(10, 5), pady=10, sticky="we")

        self.copy_button = ttk.Button(master, text="COPIAR A LISTA", command=self.copy_to_clipboard, style="TButton")
        self.copy_button.grid(row=1, column=1, padx=(5, 10), pady=10, sticky="we")

        self.wordlist_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=80, height=18, font=("Ubuntu", 12), background="#1E1E1E", foreground="#FFFFFF")
        self.wordlist_text.grid(row=2, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="nsew")

        self.footer_label = ttk.Label(master, text="Duvidas mande mensagem no LinkedIn (linkedin.com/in/wallves)", font=("Ubuntu", 10), foreground="#FFFFFF", background="#1E1E1E")
        self.footer_label.grid(row=3, column=0, columnspan=2, pady=5, sticky="s")

        self.footer_label.bind("<Button-1>", lambda e: self.open_link("https://www.linkedin.com/in/wallves/"))

        master.grid_rowconfigure(2, weight=1)
        master.grid_columnconfigure(0, weight=1)

    def generate_wordlist(self):
        base_word = self.entry.get()
        symbols = ['@', '!', '#', '$']
        numbers = ['123', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']

        variations = [''.join(p) for p in product(*zip(base_word.lower(), base_word.upper()))]
        variations_with_symbols = [variation + symbol for variation in variations for symbol in symbols]
        variations_with_numbers = [variation + num for variation in variations_with_symbols for num in numbers]

        wordlist = variations + variations_with_symbols + variations_with_numbers

        self.wordlist_text.delete(1.0, tk.END)
        self.wordlist_text.insert(tk.END, "\n".join(wordlist))

    def copy_to_clipboard(self):
        wordlist_content = self.wordlist_text.get(1.0, tk.END)
        self.master.clipboard_clear()
        self.master.clipboard_append(wordlist_content)
        self.master.update()

        popup = tk.Toplevel(self.master)
        popup.title("WORDLIST COPIADA COM SUCESSO")
        popup.geometry("415x125")
        popup.configure(bg="#1E1E1E")

        label = ttk.Label(popup, text="A WORDLIST FOI COPIADA \nPARA A AREA DE TRANSFERENCIA.", font=("Ubuntu", 12), justify="center", foreground="#FFFFFF", background="#1E1E1E")
        label.pack(padx=12, pady=12)

        ok_button = ttk.Button(popup, text="FECHAR", command=popup.destroy, style="TButton")
        ok_button.pack(pady=8)

        style = ttk.Style()
        style.configure("TButton", font=("Ubuntu", 12), foreground="#FFFFFF", background="#007BFF", padding=10, borderwidth=5, relief="flat")
        style.map("TButton", background=[("active", "#0056b3"), ("pressed", "#0056b3")])

    def open_link(self, link):
        import webbrowser
        webbrowser.open(link)

if __name__ == "__main__":
    root = tk.Tk()
    app = WordlistGeneratorApp(root)
    root.mainloop()
