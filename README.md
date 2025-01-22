# `Cycloid Curve Generator`

> [English](README.md) , [Korean](README.ko.md) 

This project is a Python-based tool designed to generate and visualize cycloid curves. A cycloid represents the trajectory traced by a point on the circumference of a circle as it rolls along a straight line. The code allows users to generate and visualize the curve by configuring various parameters.

## Key Features

- **Cycloid Curve Generation**: Calculates the curve based on the user-provided radius, range of \(t\), and the number of points.
- **Curve Visualization**: Visualizes the generated cycloid curve using Matplotlib.
- **Flexible Parameter Configuration**: Allows users to configure parameters such as radius, start and end values of \(t\), and the number of points via CLI.

## Code Structure

### `Cycloid` Class
- **Constructor (`__init__`)**
  - `radius`: Radius of the circle (default: 1)
  - `t_range`: Start and end range of \(t\) (default: 0 to [![equation](https://latex.codecogs.com/png.latex?%5C%284%5Cpi%5C%29)](#) )
  - `points`: Number of points to generate (default: 1000)
- **`calculate_points` Method**
  - Calculates the x and y coordinates of the cycloid curve.
- **`plot` Method**
  - Visualizes the generated curve using a plot.

### `main` Function
Receives CLI input, creates a `Cycloid` instance, and visualizes the curve.

### CLI Interface
Uses `argparse` to provide CLI options:
- `--radius`: Radius of the circle (default: 1)
- `--t_start`: Start value of \(t\) (default: 0)
- `--t_end`: End value of \(t\) (default: 4pi)
- `--points`: Number of points to generate (default: 1000)

## Usage

### Basic Execution
```bash
python cycloid.py
```

### Execution with Parameters
```bash
python cycloid.py --radius 2 --t_start 0 --t_end 2pi --points 500
```

## Requirements
This project requires the following Python libraries:
- `numpy`
- `matplotlib`

You can install them with the following command:
```bash
pip install numpy matplotlib
```

## Example Output

<img src="result.webp" />

<img src="cycloid.webp" />

The cycloid curve generated using this code can be visually inspected under various radii and ranges.


