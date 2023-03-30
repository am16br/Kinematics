# =======================================
# propagate system through time

propagation_time_history = []

for ti in time:
    ti_r = d2r(ti)

    # evaluate position
    r, r_mag = evaluate_vector(R, ti_r)

    # evaluate velocity
    v, v_mag = evaluate_vector(V, ti_r)

    # evaluate acceleration
    a, a_mag = evaluate_vector(A, ti_r)

    # velocity direction angles
    v_theta = [r2d(angle) for angle in direction_angles(v, v_mag)]

    # acceleration direction angles
    a_theta = [r2d(angle) for angle in direction_angles(a, a_mag)]

    # unit vector tanjent to trajectory
    ut = unit_vector(from_vector_and_magnitude=(v, v_mag))

    # unit binormal
    ub = unit_vector(from_othogonal_vectors=(v, a))

    # unit normal
    un = unit_vector(from_orthogonal_unit_vectors=(ub, ut))

    # tangential acceleration magnitude
    at = float(At.subs(t, ti_r).evalf())

    # normal acceleration
    an = np.dot(a, un)

    # radius of curvature
    rho = v_mag ** 2 / an

    # position vector of the center of curvature
    rc = r + (rho * un)

    # magnitude of the position vector of the center of curvature
    rc_mag = vector_magnitude(rc)

    iteration_results = {'t': ti, 'rx': r[0], 'ry': r[1], 'rz': r[2], 'r_mag': r_mag,
                         'vx': v[0], 'vy': v[1], 'vz': v[2], 'v_mag': v_mag,
                         'rcx': rc[0], 'rcy': rc[1], 'rcz': rc[2], 'rc_mag': rc_mag, 'rho': rho,
                         'ax': a[0], 'ay': a[1], 'az': a[2], 'a_mag': a_mag, 'an': an, 'at': at,
                         'ubx': ub[0], 'uby': ub[1], 'ubz': ub[2],
                         'utx': ut[0], 'uty': ut[1], 'utz': ut[2],
                         'unx': un[0], 'uny': un[1], 'unz': un[2]}

    propagation_time_history.append(iteration_results)

df = pd.DataFrame(propagation_time_history)
