# ==============================
# vector equations

def vector_derivative(vector, wrt):
    """
    differentiate vector components wrt a symbolic variable
    param v: vector to differentiate
    param wrt: symbolic variable
    return V: velcoity vector and components in x, y, z
    """
    return [component.diff(wrt) for component in vector]


def vector_magnitude(vector):
    """
    compute magnitude of a vector
    param vector: vector with components of Cartesian form
    return magnitude: magnitude of vector
    """
    # NOTE: np.linalg.norm(v) computes Euclidean norm
    magnitude = 0
    for component in vector:
        magnitude += component ** 2
    return magnitude ** (1 / 2)


def unit_vector(from_vector_and_magnitude=None, from_othogonal_vectors=None, from_orthogonal_unit_vectors=None):
    """
    Calculate a unit vector using one of three input parameters.
    1. using vector and vector magnitude
    2. using orthogonal vectors
    3. using orthogonal unit vectors
    """

    if from_vector_and_magnitude is not None:
        vector_a, magnitude = from_vector_and_magnitude[0], from_vector_and_magnitude[1]
        return [component / magnitude for component in vector_a]

    if from_othogonal_vectors is not None:
        vector_a, vector_b = from_othogonal_vectors[0], from_othogonal_vectors[1]
        vector_normal = np.cross(vector_a, vector_b)
        return unit_vector(from_vector_and_magnitude=(vector_normal, vector_magnitude(vector_normal)))

    if from_orthogonal_unit_vectors is not None:
        u1, u2 = from_orthogonal_unit_vectors[0], from_orthogonal_unit_vectors[1]
        return np.cross(u1, u2)


def evaluate_vector(vector, time_step):
    """
    evaluate numerical vector components and magnitude @ti
    param numerical_vector: symbolic vector expression to evaluate @ti
    param ti: time step for evaluation
    return magnitude, numerical_vector: magnitude of vector and components evaluated @ti
    """
    numerical_vector = [float(component.subs(t, time_step).evalf()) for component in vector]
    magnitude = vector_magnitude(numerical_vector)
    return numerical_vector, magnitude
