# -*- coding: utf-8 -*- 
# cycloid.py

import numpy as np
import matplotlib.pyplot as plt

class Cycloid:
    def __init__(self, radius=1, t_range=(0, 4 * np.pi), points=1000):
        """
        Initializes the Cycloid class.

        :param radius: Radius of the circle
        :param t_range: Range of the parameter t (start, end)
        :param points: Number of points to generate the curve
        """
        self.radius = radius
        self.t_range = t_range
        self.points = points

    def calculate_points(self):
        """Calculates the points of the cycloid curve."""
        t = np.linspace(self.t_range[0], self.t_range[1], self.points)
        x = self.radius * (t - np.sin(t))
        y = self.radius * (1 - np.cos(t))
        return x, y

    def plot(self):
        """Plots the cycloid curve."""
        x, y = self.calculate_points()
        plt.figure(figsize=(10, 5))
        plt.plot(x, y, label=f'Cycloid (r={self.radius})', linewidth=2)
        plt.title("Cycloid Curve", fontsize=16)
        plt.xlabel("x", fontsize=12)
        plt.ylabel("y", fontsize=12)
        plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
        plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend(fontsize=12)
        plt.show()

# Implementation of the main function
def main(radius=1, t_start=0, t_end="4pi", points=1000):
    """
    Generates and plots a cycloid curve based on the input parameters.

    :param radius: Radius of the circle
    :param t_start: Start value of t
    :param t_end: End value of t (can use "pi" in the string)
    :param points: Number of points to generate the curve
    """
    try:
        if isinstance(t_end, str):
            t_end = t_end.lower().replace("pi", "*np.pi")
            t_end = eval(t_end)

        # Create Cycloid instance and plot the graph
        cycloid = Cycloid(radius=radius, t_range=(t_start, t_end), points=points)
        cycloid.plot()

    except (ValueError, SyntaxError):
        print("Invalid t_end value. Use a valid number or 'pi' format.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    import sys
    import argparse

    parser = argparse.ArgumentParser(description="Cycloid Curve Generator")
    parser.add_argument("--radius", type=float, default=1, help="Radius of the circle (default: 1)")
    parser.add_argument("--t_start", type=float, default=0, help="Start value of t (default: 0)")
    parser.add_argument("--t_end", type=str, default="4pi", help="End value of t (default: 4pi)")
    parser.add_argument("--points", type=int, default=1000, help="Number of points to generate the curve (default: 1000)")

    args = parser.parse_args()

    main(radius=args.radius, t_start=args.t_start, t_end=args.t_end, points=args.points)

