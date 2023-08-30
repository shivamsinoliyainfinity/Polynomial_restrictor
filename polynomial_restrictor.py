import tkinter as tk
from typing import List, Dict

class RestrictedPolyGUI:
    def __init__(self):
        self.coefficients = []
        self.partial_assignment = {}
        self.restricted_coeffs = []
        
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Restricted Polynomial")
        self.root.geometry("400x250")
        
        # Create the input widgets
        tk.Label(self.root, text="Coefficients:").grid(row=0, column=0, sticky="w")
        self.coefficients_entry = tk.Entry(self.root, width=40)
        self.coefficients_entry.grid(row=1, column=0, padx=10, pady=5)
        
        tk.Label(self.root, text="Partial Assignment:").grid(row=2, column=0, sticky="w")
        self.partial_assignment_entry = tk.Entry(self.root, width=40)
        self.partial_assignment_entry.grid(row=3, column=0, padx=10, pady=5)
        
        # Create the output widget
        tk.Label(self.root, text="Restricted Polynomial:").grid(row=4, column=0, sticky="w")
        self.restricted_coeffs_text = tk.Text(self.root, height=4, width=40)
        self.restricted_coeffs_text.grid(row=5, column=0, padx=10, pady=5)
        
        # Create the button widget
        self.button = tk.Button(self.root, text="Restrict Polynomial", command=self.restrict_poly)
        self.button.grid(row=6, column=0, padx=10, pady=5)
        
        # Start the main event loop
        self.root.mainloop()
    
    def eval_poly(self, coefficients: List[int], x: Dict[int, int]) -> int:
        """Evaluates a multilinear polynomial with given coefficients at a given point x."""
        result = 0
        for i, c in enumerate(coefficients):
            term_value = 1
            for j, v in x.items():
                if (i >> j) & 1:
                    term_value *= v
            result += c * term_value
        return result % 2
    
    def restrict_poly(self):
        """Restricts a multilinear polynomial with given coefficients to a given partial assignment."""
        self.coefficients = [int(c) for c in self.coefficients_entry.get().split()]
        self.partial_assignment = {int(v): int(x) for v, x in [p.split(":") for p in self.partial_assignment_entry.get().split()]}
        v = len(self.partial_assignment)
        self.restricted_coeffs = []
        for i in range(2**v):
            x = {j: self.partial_assignment[j] for j in range(v)}
            for j in range(v, len(self.coefficients)):
                x[j] = (i >> j-v) & 1
            self.restricted_coeffs.append(self.eval_poly(self.coefficients, x))
        self.restricted_coeffs_text.delete(1.0, tk.END)
        self.restricted_coeffs_text.insert(tk.END, " ".join(str(c) for c in self.restricted_coeffs))

RestrictedPolyGUI()
