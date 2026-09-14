import tkinter as tk
from tkinter import messagebox


class TextCaseConverter:

    def __init__(self, root):
        self.root = root

        self.root.title("🔄 Text Case Converter")
        self.root.geometry("650x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#10151c")

        self.create_ui()

    # =====================================================
    # CREATE UI
    # =====================================================

    def create_ui(self):

        # Title
        tk.Label(
            self.root,
            text="🔄 TEXT CASE CONVERTER",
            font=("Consolas", 24, "bold"),
            fg="#63e6be",
            bg="#10151c"
        ).pack(pady=(30, 5))

        tk.Label(
            self.root,
            text="Convert your text into different cases",
            font=("Consolas", 10),
            fg="#7d8794",
            bg="#10151c"
        ).pack()

        # Input label
        tk.Label(
            self.root,
            text="Enter Your Text",
            font=("Consolas", 11, "bold"),
            fg="white",
            bg="#10151c"
        ).pack(pady=(25, 7))

        # Input box
        self.input_text = tk.Text(
            self.root,
            height=7,
            width=58,
            font=("Consolas", 11),
            bg="#191f28",
            fg="white",
            insertbackground="white",
            relief="flat",
            wrap="word"
        )
        self.input_text.pack()

        # Buttons
        button_frame = tk.Frame(
            self.root,
            bg="#10151c"
        )
        button_frame.pack(pady=18)

        self.create_button(
            button_frame,
            "UPPERCASE",
            lambda: self.convert("upper"),
            0,
            0
        )

        self.create_button(
            button_frame,
            "lowercase",
            lambda: self.convert("lower"),
            0,
            1
        )

        self.create_button(
            button_frame,
            "Title Case",
            lambda: self.convert("title"),
            0,
            2
        )

        self.create_button(
            button_frame,
            "Sentence Case",
            lambda: self.convert("sentence"),
            1,
            0
        )

        self.create_button(
            button_frame,
            "sWAP cASE",
            lambda: self.convert("swap"),
            1,
            1
        )

        self.create_button(
            button_frame,
            "CLEAR",
            self.clear,
            1,
            2
        )

        # Result label
        tk.Label(
            self.root,
            text="Converted Text",
            font=("Consolas", 11, "bold"),
            fg="white",
            bg="#10151c"
        ).pack(pady=(5, 7))

        # Result box
        self.result_text = tk.Text(
            self.root,
            height=7,
            width=58,
            font=("Consolas", 11),
            bg="#191f28",
            fg="#63e6be",
            insertbackground="white",
            relief="flat",
            wrap="word"
        )
        self.result_text.pack()

        # Copy button
        tk.Button(
            self.root,
            text="📋 COPY RESULT",
            command=self.copy_result,
            font=("Consolas", 10, "bold"),
            bg="#63e6be",
            fg="#10151c",
            activebackground="#80f0ce",
            relief="flat",
            cursor="hand2",
            padx=25,
            pady=9
        ).pack(pady=15)

        # Statistics
        self.stats_label = tk.Label(
            self.root,
            text="Words: 0    Characters: 0",
            font=("Consolas", 10, "bold"),
            fg="#7d8794",
            bg="#10151c"
        )
        self.stats_label.pack()

    # =====================================================
    # CREATE BUTTON
    # =====================================================

    def create_button(
        self,
        parent,
        text,
        command,
        row,
        column
    ):

        tk.Button(
            parent,
            text=text,
            command=command,
            font=("Consolas", 9, "bold"),
            bg="#252e39",
            fg="white",
            activebackground="#344150",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=15,
            pady=7
        ).grid(
            row=row,
            column=column,
            padx=4,
            pady=4
        )

    # =====================================================
    # CONVERT TEXT
    # =====================================================

    def convert(self, case_type):

        text = self.input_text.get(
            "1.0",
            tk.END
        ).strip()

        if not text:

            messagebox.showwarning(
                "No Text",
                "Please enter some text first."
            )

            return

        if case_type == "upper":

            result = text.upper()

        elif case_type == "lower":

            result = text.lower()

        elif case_type == "title":

            result = text.title()

        elif case_type == "sentence":

            result = text.lower().capitalize()

        elif case_type == "swap":

            result = text.swapcase()

        else:

            result = text

        self.result_text.delete(
            "1.0",
            tk.END
        )

        self.result_text.insert(
            "1.0",
            result
        )

        self.update_stats(result)

    # =====================================================
    # UPDATE STATISTICS
    # =====================================================

    def update_stats(self, text):

        words = len(text.split())
        characters = len(text)

        self.stats_label.config(
            text=f"Words: {words}    "
                 f"Characters: {characters}"
        )

    # =====================================================
    # COPY RESULT
    # =====================================================

    def copy_result(self):

        result = self.result_text.get(
            "1.0",
            tk.END
        ).strip()

        if not result:

            messagebox.showwarning(
                "No Result",
                "There is no converted text to copy."
            )

            return

        self.root.clipboard_clear()
        self.root.clipboard_append(result)

        messagebox.showinfo(
            "Copied",
            "Result copied to clipboard!"
        )

    # =====================================================
    # CLEAR
    # =====================================================

    def clear(self):

        self.input_text.delete(
            "1.0",
            tk.END
        )

        self.result_text.delete(
            "1.0",
            tk.END
        )

        self.stats_label.config(
            text="Words: 0    Characters: 0"
        )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = TextCaseConverter(root)

    root.mainloop()