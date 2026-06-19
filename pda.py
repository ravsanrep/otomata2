import tkinter as tk
from tkinter import ttk, messagebox

class PDASimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("PDA Simulator - aⁿbⁿ")
        self.root.geometry("700x500")
        self.root.configure(bg="#1e1e1e")

        self.stack = []

        title = tk.Label(
            root,
            text="Pushdown Automata Simulator",
            font=("Arial", 22, "bold"),
            bg="#1e1e1e",
            fg="white"
        )
        title.pack(pady=15)

        desc = tk.Label(
            root,
            text="Bahasa: L = { aⁿbⁿ | n ≥ 1 }",
            font=("Arial", 12),
            bg="#1e1e1e",
            fg="#cccccc"
        )
        desc.pack()

        input_frame = tk.Frame(root, bg="#1e1e1e")
        input_frame.pack(pady=20)

        tk.Label(
            input_frame,
            text="Input String:",
            font=("Arial", 12),
            bg="#1e1e1e",
            fg="white"
        ).grid(row=0, column=0, padx=10)

        self.input_entry = tk.Entry(
            input_frame,
            width=30,
            font=("Arial", 14)
        )
        self.input_entry.grid(row=0, column=1)

        btn_frame = tk.Frame(root, bg="#1e1e1e")
        btn_frame.pack()

        process_btn = tk.Button(
            btn_frame,
            text="Process",
            command=self.process_string,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold"),
            width=12
        )
        process_btn.grid(row=0, column=0, padx=10)

        reset_btn = tk.Button(
            btn_frame,
            text="Reset",
            command=self.reset,
            bg="#f44336",
            fg="white",
            font=("Arial", 12, "bold"),
            width=12
        )
        reset_btn.grid(row=0, column=1, padx=10)

        self.result_label = tk.Label(
            root,
            text="",
            font=("Arial", 18, "bold"),
            bg="#1e1e1e"
        )
        self.result_label.pack(pady=15)

        stack_title = tk.Label(
            root,
            text="Stack:",
            font=("Arial", 14, "bold"),
            bg="#1e1e1e",
            fg="white"
        )
        stack_title.pack()

        self.stack_label = tk.Label(
            root,
            text="[]",
            font=("Arial", 14),
            bg="#2d2d2d",
            fg="#00ffcc",
            width=30,
            height=2
        )
        self.stack_label.pack(pady=5)

        history_title = tk.Label(
            root,
            text="Process History:",
            font=("Arial", 14, "bold"),
            bg="#1e1e1e",
            fg="white"
        )
        history_title.pack(pady=5)

        self.history_box = tk.Text(
            root,
            height=10,
            width=70,
            font=("Consolas", 10),
            bg="#2d2d2d",
            fg="white"
        )
        self.history_box.pack(pady=5)

    def process_string(self):
        self.history_box.delete(1.0, tk.END)
        self.stack = []

        string = self.input_entry.get()

        if not string:
            messagebox.showwarning("Warning", "Input string terlebih dahulu!")
            return

        state = "q0"

        for i, char in enumerate(string):

            if state == "q0":
                if char == 'a':
                    self.stack.append('A')
                    self.history_box.insert(
                        tk.END,
                        f"Read 'a' -> PUSH A | Stack: {self.stack}\n"
                    )

                elif char == 'b':
                    state = "q1"

                    if len(self.stack) == 0:
                        self.reject()
                        return

                    self.stack.pop()

                    self.history_box.insert(
                        tk.END,
                        f"Read 'b' -> POP A | Stack: {self.stack}\n"
                    )

                else:
                    self.reject()
                    return

            elif state == "q1":

                if char == 'b':

                    if len(self.stack) == 0:
                        self.reject()
                        return

                    self.stack.pop()

                    self.history_box.insert(
                        tk.END,
                        f"Read 'b' -> POP A | Stack: {self.stack}\n"
                    )

                else:
                    self.reject()
                    return

        self.stack_label.config(text=str(self.stack))

        if state == "q1" and len(self.stack) == 0:
            self.accept()
        else:
            self.reject()

    def accept(self):
        self.result_label.config(
            text="ACCEPTED",
            fg="#00ff00"
        )

    def reject(self):
        self.result_label.config(
            text="REJECTED",
            fg="#ff4444"
        )

    def reset(self):
        self.input_entry.delete(0, tk.END)
        self.history_box.delete(1.0, tk.END)
        self.result_label.config(text="")
        self.stack_label.config(text="[]")
        self.stack = []


root = tk.Tk()
app = PDASimulator(root)
root.mainloop()