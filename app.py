"""
A320 QRH Abnormal/Emergency Procedure Trainer
--------------------------------------------
Educational tool for practising Airbus A320 abnormal and emergency procedures.
This script provides a minimal interactive interface to view procedure steps.

DISCLAIMER: This program is for educational demonstration only. It is not a
replacement for official Airbus documentation or certified training. Always
consult the official QRH and a qualified instructor.
"""

import json
import os
import tkinter as tk
from tkinter import ttk
from pathlib import Path

DATA_FILE = Path(__file__).with_name("procedures.json")


def load_procedures(path: Path = DATA_FILE):
    """Load procedures from a JSON file."""
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


class ProcedureTrainer(tk.Tk):
    """Tkinter application to browse procedure steps one by one."""

    def __init__(self, procedures):
        super().__init__()
        self.title("A320 QRH Trainer - Educational Use Only")
        self.geometry("700x400")
        self.procedures = procedures
        self.selected_proc = None
        self.current_step = 0
        self._create_widgets()

    def _create_widgets(self):
        # List of procedures on the left
        self.proc_list = tk.Listbox(self)
        for proc in self.procedures:
            self.proc_list.insert(tk.END, proc["name"])
        self.proc_list.bind("<<ListboxSelect>>", self._show_steps)
        self.proc_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

        # Right side for procedure content
        right = ttk.Frame(self)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.proc_label = ttk.Label(right, text="Select a procedure", font=("TkDefaultFont", 12, "bold"))
        self.proc_label.pack(pady=5)

        self.step_text = tk.Text(right, wrap=tk.WORD, height=10, state=tk.DISABLED)
        self.step_text.pack(fill=tk.BOTH, expand=True)

        nav = ttk.Frame(right)
        nav.pack(pady=5)
        self.prev_btn = ttk.Button(nav, text="Previous", command=self._prev_step, state=tk.DISABLED)
        self.prev_btn.pack(side=tk.LEFT, padx=5)
        self.next_btn = ttk.Button(nav, text="Next", command=self._next_step, state=tk.DISABLED)
        self.next_btn.pack(side=tk.LEFT, padx=5)

    def _show_steps(self, event):
        selection = event.widget.curselection()
        if not selection:
            return
        idx = selection[0]
        self.selected_proc = self.procedures[idx]
        self.current_step = 0
        self.proc_label.config(text=self.selected_proc["name"])
        self._update_step_display()

    def _update_step_display(self):
        step = self.selected_proc["steps"][self.current_step]
        self.step_text.configure(state=tk.NORMAL)
        self.step_text.delete("1.0", tk.END)
        self.step_text.insert(
            tk.END,
            f"Step {self.current_step + 1} of {len(self.selected_proc['steps'])}\n\n{step}",
        )
        self.step_text.configure(state=tk.DISABLED)

        self.prev_btn.config(state=tk.NORMAL if self.current_step > 0 else tk.DISABLED)
        self.next_btn.config(
            state=tk.NORMAL
            if self.current_step < len(self.selected_proc["steps"]) - 1
            else tk.DISABLED
        )

    def _next_step(self):
        if self.current_step < len(self.selected_proc["steps"]) - 1:
            self.current_step += 1
            self._update_step_display()

    def _prev_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            self._update_step_display()


def main():
    if not os.environ.get("DISPLAY"):
        print("This application requires a graphical display (X11).")
        return

    procedures = load_procedures()
    app = ProcedureTrainer(procedures)
    app.mainloop()


if __name__ == "__main__":
    main()
