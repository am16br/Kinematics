#how memory is traded for moments in decision making process
#based on task (minimize/maximize/etc) - memory set to operating environment - solving rate&map rate

'''Law of Refraction/Snell's Law
medium1_refraction_index sin(incident_angle) = medium1_refraction_index sin(refracted_angle)
#speed of light varies by medium - similar to time/space complexity varying by algorithm
#sets observable space to complete some computation
    number of factors a computation can reliably consider for accurate predictions/time decay of accurate/score future insight
    Generalizing to relativity allows computer more time to explore mappings of unstructured data
'''
import numpy as np

class Wave:
    source = {"x": 0, "y": 0}
    distance_map = None
    def __init__(self, x, y):
        self.source = {"x": x, "y": y}
    def map_euclidean_distance(self, x, y):
        self.distance_map = np.sqrt((x - self.source["x"])**2 + (y - self.source["y"])**2)
    def map_cosine_similarity(self, x, y):
        #self.distance_map = np.sum(A*B, axis=1)/(norm(A, axis=1)*norm(B, axis=1))
        self.distance_map = np.sqrt((x - self.source["x"])**2 + (y - self.source["y"])**2)

    def law_of_refraction(self, incident_angle):  #determines # of factors decision maker can consider based on known accuracy to some future point
        refracted_angle=math.asin((medium1_refraction_index/medium2_refraction_index)*math.sin(incident_angle))
        #medium1_refraction_index sin(incident_angle) = medium2_refraction_index sin(refracted_angle)

def init_waves(offset,direction,slit_distance):
    return [Wave(0, offset * np.pi + direction * slit_distance / 2)
            for offset in (-1.5, -0.5, 0.5, 1.5)
            for direction in (-1, 1)]

def create_wave_pattern(waves, step, steps):
    return abs(sum([np.sin(wave.distance_map - 2 * np.pi * step / steps) for wave in waves]))


# Configuration of environment
slit_distance = 8 * np.pi       # Distance of the center of the two slits. Only relevant for double-slit scenarios.

projection = 40              #slit to wall, ... projection of future
space = 100                  # Breadth of wall.

steps = 10               # Steps for the simulation to take. Fast prototypes are OK at 10, good quality starts around 50.
quality = 20             # Controlling the stride of the 3d plots. Fast prototypes are OK at 20, great quality is 1.

waves = init_waves()

x, y = np.arange(0, projection, 0.05), np.arange(-space, space, 0.05)
x, y = np.meshgrid(x, y)

for wave in waves:
    wave.create_distance_map(x, y)

z_over_time = np.zeros((len(x), len(y[0]), steps))
for step in range(steps):
    z_over_time[:,:,step] = create_wave_pattern(waves, step, steps)

create_animated_3d_plot(x, y, z_over_time, type_of_simulation)
create_animated_wall_plot(breadth, z_over_time, type_of_simulation)
