import numpy as np
import random, time, math
import matplotlib.pyplot as plt

def rand(value, parameters):
    if(value==-1):
        return value
    return round(random.uniform(parameters[0],parameters[1]),parameters[2])
def set(value, parameters):
    if(value==-1):
        return value
    return parameters

def activation(value, parameters):
    return 1

def distance(value, parameters):
    if(value==-1):
        return value
    x_coordinate=parameters[0]  #ambulance coordinates
    y_coordinate=parameters[1]
    x=parameters[2]             #position coordinates
    y=parameters[3]
    coefficient=parameters[4][x][y]     #parameters[4] is matrix of travel coefficients
    distance=abs(x_coordinate-x)+abs(y_coordinate-y)+coefficient    #euclidean/manhattan/cosine/options
    if(distance<value):
        return distance
    return value

def modify_layer(matrix, function, parameters):
    for index, value in enumerate(np.nditer(matrix)):
        x=int(index/matrix.shape[1])
        y=index%matrix.shape[1]
        matrix[x][y]=function(value, parameters)
    return matrix

def plot(layers, queue, title, xlabel, ylabel, zlabel):
    colors=['jet', 'Greens', 'Reds', 'RdYlGn']
    x = np.linspace(0, layers[0].shape[0], layers[0].shape[1])
    y = np.linspace(0, layers[0].shape[1], layers[0].shape[0])
    X, Y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    for index, matrix in enumerate(layers):
        ax.contour3D(X, Y, matrix, 50, cmap=colors[index])
    for i in queue:     #emergencies    [x,y,time_received,priority] time&priority affect growth rate of 'edge'
        ax.plot(i[0], i[1], "or")   #circle centered at position (i[0],i[1]) of radius i[3]-time@rate of acceptable service
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    plt.show()

def procedure(layers):
    reality=np.ones((layers[0].shape[0],layers[0].shape[1]))
    vars=[0.25, 2]  #some set of problem-specific variables(resources available) for activation function to decide if energy is worth spent on action
    for layer in layers:    #layers of environment - agent/event positions and their type's effect on surroundings
        reality=np.add(reality, layer)  #dot product or whatever
    return reality#modify_layer(reality, activation, vars)    #0 or 1 outline path of redeployments until next signal disturbance

rows=10       #length
columns=10    #width
number_of_agents=3

map=np.ones((rows,columns))
map=modify_layer(map,rand,(1.0,2.0,2))
print(map)

#matrix holds points agent can take action
distance=np.zeros((rows,columns))   #extract environment from world
distance=modify_layer(map,rand,(1.0,5.0,2))     #static
friction=np.zeros((rows,columns))   #'traffic' (beyond control... fed in)
friction=modify_layer(map,rand,(1.0,2.0,2))     #dynamic

locations=np.zeros((rows,columns))  #ambulance present ('intelligently' controlled)
locations=modify_layer(map,rand,(0,1,0))        #adaptive
events=[]                                       #reactive (force actions that impact environment by known factors)
'''
time=np.zeros((rows,columns))   #response time of nearest neighbor 'decomposes'@rate
force=np.zeros((rows,columns))  #exert force on locations(free agents) to minimize total response time

agent=[x_position,y_position,x_destination,y_destination,status,velocity]   #'intelligent'/controlled
wormhole=[x,y,agents_waiting,time2reentry]  #stationary
stations=[] #hospitals/wormholes
blackhole=[x,y,time,rate]                   #'unknown' events
events=[]   #emergencies/blackholes
#hidden_layer - 'wire' from blackhole[x,y] to wormhole[X,Y] (considering distance&traffic)
#active_layer - time for nearest responder - 'big' changes at steps agent(s) forced actions/enter blackhole/exit wormhole
'''
t=0
event_rate=0.25
#distances initialized
#agent locations initialized
#'base stations(key points/areas unique to base map and fleet size)' computed and placed
while(t<60):
    friction=modify_layer(map,rand,(1.0,2.0,2))     #'friction' updated on regular interval
    if(random.randint(0,t)<t*event_rate):           #events randomly occur over time@rate
        blackhole=[random.randint(0,rows-1),random.randint(0,columns-1),t,round(random.uniform(0,1),2)]
        events.append(blackhole)    #route nearest agent - compute time to pickup/drop-off & use to project future environment/concise optimization problem considering information at time step
        for e in events:
            c=2*math.pi*e[2]*e[3]
            print("blackhole spreading ["+str(e[0])+", "+str(e[1])+"]; circumference: "+str(c))
        #active_layer=modify_layer(active_layer, forced_response, events)
        #active_layer=modify_layer(active_layer, reaction, time2response)
        layers=[distance, friction, locations]
        map=procedure(layers)   #combine layers, apply activation function
        plot(layers, events, 'Layer', 'city length', 'city width', 'response time')
    #time.sleep(1)
    t+=1
