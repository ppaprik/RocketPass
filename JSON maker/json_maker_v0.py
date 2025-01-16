import json
import customtkinter as ctk
from tkinter import messagebox

class JSONBuilderApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Indented Text to JSON Converter")
        self.geometry("800x600")

        # Input and Output
        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=750, height=550)
        self.scrollable_frame.pack(pady=10)

        # Input Textbox
        self.input_label = ctk.CTkLabel(self.scrollable_frame, text="Enter Indented Text:", font=("Arial", 16))
        self.input_label.pack(pady=5)

        self.input_textbox = ctk.CTkTextbox(self.scrollable_frame, height=200, width=700)
        self.input_textbox.pack(pady=10)

        # Convert Button
        self.convert_button = ctk.CTkButton(self.scrollable_frame, text="Convert to JSON", command=self.convert_to_json)
        self.convert_button.pack(pady=10)

        # Output Textbox
        self.output_label = ctk.CTkLabel(self.scrollable_frame, text="Generated JSON:", font=("Arial", 16))
        self.output_label.pack(pady=5)

        self.output_textbox = ctk.CTkTextbox(self.scrollable_frame, height=200, width=700, state="disabled")
        self.output_textbox.pack(pady=10)

    def parse_text_to_json(self, text):
        lines = text.splitlines()
        stack = [{}]
        current_indent = -1

        for line in lines:
            if not line.strip():
                continue

            indent = len(line) - len(line.lstrip())
            line = line.strip()

            # Adjust stack based on indentation
            while indent <= current_indent:
                stack.pop()
                current_indent = stack[-1][1]

            current_object = stack[-1][0]

            if ':' in line:
                key, value = map(str.strip, line.split(':', 1))

                if value == "[]":
                    new_object = []
                    current_object[key] = new_object
                    stack.append((new_object, indent))
                elif value == "{}":
                    new_object = {}
                    current_object[key] = new_object
                    stack.append((new_object, indent))
                else:
                    try:
                        value = json.loads(value)
                    except json.JSONDecodeError:
                        pass
                    current_object[key] = value
            else:
                if line.startswith('-'):
                    line = line[1:].strip()

                try:
                    value = json.loads(line)
                except json.JSONDecodeError:
                    value = line

                if isinstance(current_object, list):
                    current_object.append(value)
                else:
                    raise ValueError("Invalid format: List item outside a list")

            current_indent = indent
            stack[-1] = (current_object, current_indent)

        return stack[0][0]

    def convert_to_json(self):
        """
        Convert the input indented text into JSON.
        """
        input_text = self.input_textbox.get("1.0", "end").strip()
        if not input_text:
            messagebox.showwarning("Warning", "Input cannot be empty!")
            return

        try:
            json_data = self.parse_text_to_json(input_text)
            formatted_json = json.dumps(json_data, indent=4)

            # Display in the output textbox
            self.output_textbox.configure(state="normal")
            self.output_textbox.delete("1.0", "end")
            self.output_textbox.insert("1.0", formatted_json)
            self.output_textbox.configure(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to parse text to JSON:\n{e}")

# Run the application
if __name__ == "__main__":
    app = JSONBuilderApp()
    app.mainloop()
