# =======================================
# symbolic equations of motion

# Define symbolic variable t
t = sp.symbols('t')

# [x(t), y(t), z(t)] position as function of time
# R = [sp.sin(3 * t), sp.cos(t), sp.cos(2 * t)]
R = [sp.cos(t), sp.sin(t), t / 5]  # Helix: z=t
# R = [sp.cos(t), sp.sin(t), 0 * t]  # Circle: z=0*t

# velocity = dR/dt
V = vector_derivative(R, t)

# acceleration = dV/dt
A = vector_derivative(V, t)

# tangential acceleration = dV/dt (derivative of the magnitude of velocity)
At = vector_magnitude(V).diff(t)
