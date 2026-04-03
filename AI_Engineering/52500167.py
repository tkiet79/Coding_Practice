import math
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

A = 70
x, x0 = sp.symbols('x x0')
f = x**2 - 2*A*x - A**2
g = -x**2 + 4*A*x + A**3
f_num = sp.lambdify(x, f, 'numpy')
g_num = sp.lambdify(x, g, 'numpy')

pts_1a = sp.solve(f - g, x)
for i, p in enumerate(pts_1a):
    print(f"1a. Intersection point {i+1} : ( {float(p):.12f} , {float(f.subs(x, p)):.12f} )")
x_vals_1a = np.linspace(float(min(pts_1a)) - 300, float(max(pts_1a)) + 300, 400)
plt.figure()
plt.plot(x_vals_1a, f_num(x_vals_1a), 'b', label='f(x)')
plt.plot(x_vals_1a, g_num(x_vals_1a), 'r', label='g(x)')
for p in pts_1a:
    plt.plot(float(p), float(f.subs(x, p)), 'go')
plt.title('Question 1a')
plt.legend()
plt.show()

df = sp.diff(f, x)
T = df.subs(x, 0) * x - A**2
print(f"\nEquation of the tangent line to the curve f(x) : {T}")
f_shift = f - 4 * A**3
pts_1b = sp.solve(f_shift - T, x)
for i, p in enumerate(pts_1b):
    print(f"1b. Intersection point {i+1} : ( {float(p):.12f} , {float(f_shift.subs(x, p)):.12f} )")
f_shift_num = sp.lambdify(x, f_shift, 'numpy')
T_num = sp.lambdify(x, T, 'numpy')
x_vals_1b = np.linspace(float(min(pts_1b)) - 300, float(max(pts_1b)) + 300, 400)
plt.figure()
plt.plot(x_vals_1b, f_num(x_vals_1b), 'b', label='f(x)')
plt.plot(x_vals_1b, f_shift_num(x_vals_1b), 'r', label='shifted f(x)')
plt.plot(x_vals_1b, T_num(x_vals_1b), 'orange', label='tangent line to f(x)')
plt.plot(0, -A**2, 'go')
for p in pts_1b:
    plt.plot(float(p), float(f_shift.subs(x, p)), 'ko')
plt.title('Question 1b')
plt.legend()
plt.show()


eq_1c = (f.subs(x, x0) - (-4 * A**3)) / (x0 - 0) - df.subs(x, x0)
pts_1c = sp.solve(eq_1c, x0)
T_lines = []
print()
for i, p in enumerate(pts_1c):
    m_i = df.subs(x, p)
    T_i = sp.expand(m_i * (x - p) + f.subs(x, p)).evalf()
    T_lines.append((float(p), float(f.subs(x, p)), T_i))
    print(f"1b. Equation of the tangent line {i+1} to the curve f(x) : {T_i}")
x_vals_1c = np.linspace(float(min(pts_1c)) - 300, float(max(pts_1c)) + 300, 400)
plt.figure()
plt.plot(x_vals_1c, f_num(x_vals_1c), 'b', label='f(x)')
colors = ['blue', 'orange']
for i, t in enumerate(T_lines):
    t_num = sp.lambdify(x, t[2], 'numpy')
    plt.plot(x_vals_1c, t_num(x_vals_1c), color=colors[i], label=f'tangent line {i+1}')
    plt.plot(t[0], t[1], 'ko')
plt.plot(0, -4 * A**3, 'go')
plt.title('Question 1c')
plt.legend()
plt.show()