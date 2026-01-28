# Spring Oscillator Simulation

Numerical simulation of a classical harmonic oscillator using Python.
The project demonstrates basic physical modeling, numerical integration,
and data visualization.

---

## Overview

This repository contains a numerical simulation of a mass–spring system
based on Newtonian mechanics. The system is solved using the explicit
Euler method and visualized with Matplotlib.

The project was created as part of learning computational physics
and numerical methods in Python.

---

## Physical Model

The motion of a mass attached to a spring is governed by Hooke’s law:

F = −k · x

Using Newton’s second law:

m · d²x/dt² = −k · x

The equation is rewritten as a first-order system:

dx/dt = v  
dv/dt = −(k/m) · x

---

## Implementation

- Numerical integration: Explicit Euler method
- Language: Python
- Libraries: NumPy, Matplotlib
- Output: Displacement vs time plot

---

## Project Structure

```text
spring-oscillator-simulation/
├── src/
│   └── spring_oscillator.py
├── .gitignore
├── README.md
└── requirements.txt

