# Triangle Calculator

A Python application with a graphical user interface (GUI) that calculates various properties of triangles based on user inputs.

## Features

- Calculate triangle properties including:
  - Perimeter
  - Area
  - Type of triangle (equilateral, isosceles, scalene)
  - Internal angles
  - Angle type (acute, right, obtuse)
- Input triangle dimensions using three different methods:
  - Three sides
  - Two angles and one side
  - Base and height
- Visualize the triangle with a dynamic drawing
- Validate inputs to ensure they form a valid triangle

## Requirements

- Python 3.x
- Tkinter (included with most Python installations)
- NumPy
- Matplotlib
- Math library (standard Python library)

## Installation

1. Ensure you have Python installed on your system
2. Install required packages:
   ```
   pip install numpy matplotlib
   ```
3. Run the application:
   ```
   python main.py
   ```

## Usage

1. Choose a calculation method:
   - **Three Sides:** Enter the lengths of all three sides
   - **Angles and Side:** Enter two angles (in degrees) and one side length
   - **Base and Height:** Enter the base and height measurements

2. Click the "Calculate" button to compute the triangle properties

3. View the results in the output area and see the triangle visualization

## Input Validation

The application performs several validations:
- All sides and angles must be positive values
- For the three sides method, the sum of any two sides must be greater than the third side
- For the angles method, the sum of the two input angles must be less than 180 degrees

## License

This project is open source and available for educational and personal use.