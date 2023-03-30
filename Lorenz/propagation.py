# ==============================================================
# simulation harness

# discrete time step size
dt = 0.01
# simulation time range
time = np.arange(0.0, 8.0, dt)
# lorenz initial conditions (x, y, z) at t = 0
y0 = np.array([-7, 8, 26])

# ==============================================================
# propagate state
# simulation results
state_history = []
# initialize yk
yk = y0
# intialize time
t = 0
# iterate over time
for t in time:
    # save current state
    state_history.append(yk)
    # update state variables yk to yk+1
    yk = rk4(lorenz, t, yk, dt)
# convert list to numpy array
state_history = np.array(state_history)
