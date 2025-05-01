import tkinter as tk
from tkinter import ttk, messagebox
import math
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class TriangleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Triangle Calculator")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create notebook for different calculation methods
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Create frames for different calculation methods
        self.sides_frame = ttk.Frame(self.notebook, padding="10")
        self.angle_side_frame = ttk.Frame(self.notebook, padding="10")
        self.base_height_frame = ttk.Frame(self.notebook, padding="10")
        
        self.notebook.add(self.sides_frame, text="Three Sides")
        self.notebook.add(self.angle_side_frame, text="Angles and Side")
        self.notebook.add(self.base_height_frame, text="Base and Height")
        
        # Create the three sides input frame
        self.create_sides_frame()
        
        # Create the angles and side input frame
        self.create_angle_side_frame()
        
        # Create the base and height input frame
        self.create_base_height_frame()
        
        # Create output frame
        output_frame = ttk.LabelFrame(main_frame, text="Results", padding="10")
        output_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Create output text area
        self.output_text = tk.Text(output_frame, height=8, width=60, wrap=tk.WORD)
        self.output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Add scrollbar to output text
        scrollbar = ttk.Scrollbar(output_frame, orient=tk.VERTICAL, command=self.output_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.output_text.config(yscrollcommand=scrollbar.set)
        
        # Create canvas for triangle visualization
        canvas_frame = ttk.LabelFrame(main_frame, text="Triangle Visualization", padding="10")
        canvas_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Use matplotlib for better drawing capabilities
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.plot = self.figure.add_subplot(111)
        self.plot.set_aspect('equal')
        
        self.canvas = FigureCanvasTkAgg(self.figure, master=canvas_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def create_sides_frame(self):
        # Create input fields for three sides
        ttk.Label(self.sides_frame, text="Side a:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.side_a_var = tk.StringVar()
        ttk.Entry(self.sides_frame, textvariable=self.side_a_var, width=10).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.sides_frame, text="Side b:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.side_b_var = tk.StringVar()
        ttk.Entry(self.sides_frame, textvariable=self.side_b_var, width=10).grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(self.sides_frame, text="Side c:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.side_c_var = tk.StringVar()
        ttk.Entry(self.sides_frame, textvariable=self.side_c_var, width=10).grid(row=2, column=1, padx=5, pady=5)
        
        # Calculate button
        ttk.Button(self.sides_frame, text="Calculate", command=self.calculate_from_sides).grid(row=3, column=0, columnspan=2, pady=10)

    def create_angle_side_frame(self):
        # Create input fields for two angles and one side
        ttk.Label(self.angle_side_frame, text="Angle A (degrees):").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.angle_A_var = tk.StringVar()
        ttk.Entry(self.angle_side_frame, textvariable=self.angle_A_var, width=10).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.angle_side_frame, text="Angle B (degrees):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.angle_B_var = tk.StringVar()
        ttk.Entry(self.angle_side_frame, textvariable=self.angle_B_var, width=10).grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(self.angle_side_frame, text="Side c (opposite to angle C):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.side_c_angle_var = tk.StringVar()
        ttk.Entry(self.angle_side_frame, textvariable=self.side_c_angle_var, width=10).grid(row=2, column=1, padx=5, pady=5)
        
        # Calculate button
        ttk.Button(self.angle_side_frame, text="Calculate", command=self.calculate_from_angles_side).grid(row=3, column=0, columnspan=2, pady=10)

    def create_base_height_frame(self):
        # Create input fields for base and height
        ttk.Label(self.base_height_frame, text="Base:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.base_var = tk.StringVar()
        ttk.Entry(self.base_height_frame, textvariable=self.base_var, width=10).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.base_height_frame, text="Height:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.height_var = tk.StringVar()
        ttk.Entry(self.base_height_frame, textvariable=self.height_var, width=10).grid(row=1, column=1, padx=5, pady=5)
        
        # Additional side input for complete triangle calculation
        ttk.Label(self.base_height_frame, text="Side length (optional):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.side_bh_var = tk.StringVar()
        ttk.Entry(self.base_height_frame, textvariable=self.side_bh_var, width=10).grid(row=2, column=1, padx=5, pady=5)
        
        # Calculate button
        ttk.Button(self.base_height_frame, text="Calculate", command=self.calculate_from_base_height).grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_from_sides(self):
        try:
            # Get and validate input
            a = float(self.side_a_var.get())
            b = float(self.side_b_var.get())
            c = float(self.side_c_var.get())
            
            if a <= 0 or b <= 0 or c <= 0:
                messagebox.showerror("Input Error", "Side lengths must be positive values.")
                return
            
            # Check if valid triangle
            if a + b <= c or a + c <= b or b + c <= a:
                messagebox.showerror("Invalid Triangle", "The given side lengths cannot form a triangle.")
                return
            
            # Calculate perimeter
            perimeter = a + b + c
            
            # Calculate area using Heron's formula
            s = perimeter / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            
            # Determine triangle type
            triangle_type = self.determine_triangle_type(a, b, c)
            
            # Calculate angles
            angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
            angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
            angle_C = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
            
            # Display results
            self.display_results(a, b, c, perimeter, area, triangle_type, angle_A, angle_B, angle_C)
            
            # Draw the triangle
            self.draw_triangle(a, b, c, angle_A, angle_B, angle_C)
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for all sides.")

    def calculate_from_angles_side(self):
        try:
            # Get and validate input
            angle_A = float(self.angle_A_var.get())
            angle_B = float(self.angle_B_var.get())
            side_c = float(self.side_c_angle_var.get())
            
            if angle_A <= 0 or angle_B <= 0 or side_c <= 0:
                messagebox.showerror("Input Error", "Angles and side length must be positive values.")
                return
            
            # Calculate angle C
            angle_C = 180 - angle_A - angle_B
            
            if angle_C <= 0:
                messagebox.showerror("Invalid Triangle", "The sum of angles must be less than 180 degrees.")
                return
            
            # Convert to radians for calculations
            angle_A_rad = math.radians(angle_A)
            angle_B_rad = math.radians(angle_B)
            angle_C_rad = math.radians(angle_C)
            
            # Calculate sides using Law of Sines
            side_a = side_c * math.sin(angle_A_rad) / math.sin(angle_C_rad)
            side_b = side_c * math.sin(angle_B_rad) / math.sin(angle_C_rad)
            
            # Calculate perimeter
            perimeter = side_a + side_b + side_c
            
            # Calculate area
            area = 0.5 * side_a * side_b * math.sin(angle_C_rad)
            
            # Determine triangle type
            triangle_type = self.determine_triangle_type(side_a, side_b, side_c)
            
            # Display results
            self.display_results(side_a, side_b, side_c, perimeter, area, triangle_type, angle_A, angle_B, angle_C)
            
            # Draw the triangle
            self.draw_triangle(side_a, side_b, side_c, angle_A, angle_B, angle_C)
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")

    def calculate_from_base_height(self):
        try:
            # Get and validate input
            base = float(self.base_var.get())
            height = float(self.height_var.get())
            
            if base <= 0 or height <= 0:
                messagebox.showerror("Input Error", "Base and height must be positive values.")
                return
            
            # Calculate area
            area = 0.5 * base * height
            
            # Try to get the side length for more calculations
            side = None
            try:
                if self.side_bh_var.get():
                    side = float(self.side_bh_var.get())
                    if side <= 0:
                        messagebox.showerror("Input Error", "Side length must be positive.")
                        return
            except ValueError:
                pass
            
            # If we have a side length, we can calculate more properties
            if side is not None:
                # Assuming this is side 'a', and 'base' is side 'c'
                # We need to find side 'b'
                # Using the height, we can calculate the location of the vertex
                # From the height, we can calculate where the perpendicular line meets the base
                # Let's call this point 'p' where 0 <= p <= base
                
                # Pythagorean theorem gives us: p² + height² = a²
                # So p = sqrt(a² - height²)
                if side**2 < height**2:
                    messagebox.showerror("Invalid Triangle", "The given side cannot form a triangle with the given height.")
                    return
                
                p = math.sqrt(side**2 - height**2)
                
                # Side b is the distance from the end of the base to the vertex
                side_b = math.sqrt((base - p)**2 + height**2)
                
                # Now we have all three sides
                side_a = side
                side_c = base
                
                # Check if valid triangle
                if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
                    messagebox.showerror("Invalid Triangle", "The given values cannot form a triangle.")
                    return
                
                # Calculate perimeter
                perimeter = side_a + side_b + side_c
                
                # Determine triangle type
                triangle_type = self.determine_triangle_type(side_a, side_b, side_c)
                
                # Calculate angles
                angle_A = math.degrees(math.acos((side_b**2 + side_c**2 - side_a**2) / (2 * side_b * side_c)))
                angle_B = math.degrees(math.acos((side_a**2 + side_c**2 - side_b**2) / (2 * side_a * side_c)))
                angle_C = math.degrees(math.acos((side_a**2 + side_b**2 - side_c**2) / (2 * side_a * side_b)))
                
                # Display complete results
                self.display_results(side_a, side_b, side_c, perimeter, area, triangle_type, angle_A, angle_B, angle_C)
                
                # Draw the triangle
                self.draw_triangle(side_a, side_b, side_c, angle_A, angle_B, angle_C)
            else:
                # Without a side length, we can only show partial results
                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(tk.END, f"Area: {area:.2f} square units\n")
                self.output_text.insert(tk.END, f"Base: {base:.2f} units\n")
                self.output_text.insert(tk.END, f"Height: {height:.2f} units\n")
                self.output_text.insert(tk.END, "\nNote: For complete calculations, provide an additional side length.")
                
                # Draw a simple triangle representation
                self.draw_simple_triangle(base, height)
                
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for all required fields.")

    def determine_triangle_type(self, a, b, c):
        # Determine if equilateral, isosceles, or scalene
        if abs(a - b) < 1e-9 and abs(b - c) < 1e-9:
            return "Equilateral"
        elif abs(a - b) < 1e-9 or abs(a - c) < 1e-9 or abs(b - c) < 1e-9:
            return "Isosceles"
        else:
            return "Scalene"
        
    def determine_angle_type(self, angle_A, angle_B, angle_C):
        # Determine if acute, right, or obtuse
        angles = [angle_A, angle_B, angle_C]
        
        if any(abs(angle - 90) < 1e-9 for angle in angles):
            return "Right"
        elif all(angle < 90 for angle in angles):
            return "Acute"
        else:
            return "Obtuse"

    def display_results(self, a, b, c, perimeter, area, triangle_type, angle_A, angle_B, angle_C):
        angle_type = self.determine_angle_type(angle_A, angle_B, angle_C)
        
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"Side a: {a:.2f} units\n")
        self.output_text.insert(tk.END, f"Side b: {b:.2f} units\n")
        self.output_text.insert(tk.END, f"Side c: {c:.2f} units\n\n")
        
        self.output_text.insert(tk.END, f"Perimeter: {perimeter:.2f} units\n")
        self.output_text.insert(tk.END, f"Area: {area:.2f} square units\n\n")
        
        self.output_text.insert(tk.END, f"Triangle type by sides: {triangle_type}\n")
        self.output_text.insert(tk.END, f"Triangle type by angles: {angle_type}\n\n")
        
        self.output_text.insert(tk.END, f"Angle A: {angle_A:.2f} degrees\n")
        self.output_text.insert(tk.END, f"Angle B: {angle_B:.2f} degrees\n")
        self.output_text.insert(tk.END, f"Angle C: {angle_C:.2f} degrees\n")

    def draw_triangle(self, a, b, c, angle_A, angle_B, angle_C):
        # Clear previous plot
        self.plot.clear()
        
        # Convert angles to radians
        angle_A_rad = math.radians(angle_A)
        angle_B_rad = math.radians(angle_B)
        angle_C_rad = math.radians(angle_C)
        
        # Calculate coordinates for the triangle vertices
        # Place point A at the origin
        A = np.array([0, 0])
        
        # Place point B at (c, 0)
        B = np.array([c, 0])
        
        # Calculate coordinates for point C
        C_x = b * math.cos(angle_A_rad)
        C_y = b * math.sin(angle_A_rad)
        C = np.array([C_x, C_y])
        
        # Draw the triangle
        self.plot.plot([A[0], B[0]], [A[1], B[1]], 'b-')
        self.plot.plot([B[0], C[0]], [B[1], C[1]], 'b-')
        self.plot.plot([C[0], A[0]], [C[1], A[1]], 'b-')
        
        # Add labels for vertices
        self.plot.text(A[0] - 0.1, A[1] - 0.1, "A", fontsize=12)
        self.plot.text(B[0] + 0.1, B[1] - 0.1, "B", fontsize=12)
        self.plot.text(C[0], C[1] + 0.1, "C", fontsize=12)
        
        # Add labels for sides
        self.plot.text((B[0] + C[0]) / 2, (B[1] + C[1]) / 2, f"a = {a:.2f}", fontsize=10)
        self.plot.text((A[0] + C[0]) / 2, (A[1] + C[1]) / 2, f"b = {b:.2f}", fontsize=10)
        self.plot.text((A[0] + B[0]) / 2, (A[1] + B[1]) / 2, f"c = {c:.2f}", fontsize=10)
        
        # Set the axis limits with some padding
        padding = max(a, b, c) * 0.2
        self.plot.set_xlim(-padding, max(B[0], C[0]) + padding)
        self.plot.set_ylim(-padding, C[1] + padding)
        
        self.plot.grid(True)
        self.plot.set_aspect('equal')
        self.plot.set_title('Triangle Visualization')
        
        # Update the canvas
        self.canvas.draw()

    def draw_simple_triangle(self, base, height):
        # Clear previous plot
        self.plot.clear()
        
        # Simple triangle with the base on the x-axis and height going up
        A = np.array([0, 0])          # Left base point
        B = np.array([base, 0])       # Right base point
        C = np.array([base/2, height]) # Top point
        
        # Draw the triangle
        self.plot.plot([A[0], B[0]], [A[1], B[1]], 'b-')
        self.plot.plot([B[0], C[0]], [B[1], C[1]], 'b-')
        self.plot.plot([C[0], A[0]], [C[1], A[1]], 'b-')
        
        # Add labels
        self.plot.text(A[0] - 0.1, A[1] - 0.1, "A", fontsize=12)
        self.plot.text(B[0] + 0.1, B[1] - 0.1, "B", fontsize=12)
        self.plot.text(C[0], C[1] + 0.1, "C", fontsize=12)
        
        # Add height indicator
        self.plot.plot([base/2, base/2], [0, height], 'r--')
        self.plot.text(base/2 + 0.1, height/2, f"h = {height:.2f}", fontsize=10)
        
        # Add base label
        self.plot.text(base/2, -0.1, f"base = {base:.2f}", fontsize=10)
        
        # Set the axis limits with some padding
        padding = max(base, height) * 0.2
        self.plot.set_xlim(-padding, base + padding)
        self.plot.set_ylim(-padding, height + padding)
        
        self.plot.grid(True)
        self.plot.set_aspect('equal')
        self.plot.set_title('Triangle Visualization')
        
        # Update the canvas
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = TriangleCalculator(root)
    root.mainloop()