# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import time
start_time = time.time()

# mass, spring constant, initial position and velocity
m = 1
k = 1
'''x = 0
v = 1
e = 0.5*m*v**2
p = 0.5*k*x**2
E = e + p'''

# simulation time, timestep and time
t_max = 1000
dt = 2    #Verlet method breaks down using values of dt>1, 100 times higher than Euler
t_array = np.arange(0, t_max, dt)

#analytical values
w = (k/m)**0.5
y = np.cos(w*t_array - np.pi/2)

# initialise 0 arrays to record trajectories
x_array = np.zeros(len(t_array))
v1_array = np.zeros(len(t_array))
v2_array = np.zeros(len(t_array))

E_array = np.zeros(len(t_array))

#first iteration
x_array[0] = 0
v1_array[0] = 1
v2_array[0] = 1

e = 0.5*m*v2_array[0]**2
p = 0.5*k*x_array[0]**2
E_array[0] = e + p

#second iteration
a = -k * x_array[0] / m
x_array[1] = np.cos(w*t_array[1] - np.pi/2)
v1_array[1] = (0.5/dt)*(x_array[0])
v2_array[1] = (1/dt)*(x_array[1] - x_array[0])

e = 0.5*m*v2_array[1]**2
p = 0.5*k*x_array[1]**2
E_array[1] = e + p


# Verlet integration
for i in range(2, len(t_array)):
    a = -k * x_array[i-1] / m
    x_array[i] = 2*x_array[i-1] - x_array[i-2] + dt**2*a
    v1_array[i-1] = (0.5/dt)*(x_array[i] - x_array[i-2])
    v2_array[i] = (1/dt)*(x_array[i] - x_array[i-1])
    e = 0.5*m*v2_array[i]**2
    p = 0.5*k*x_array[i]**2
    E_array[i] = e + p

v1_array[-1] = v1_array[-2] #easy fix for simplicity and aesthetics

print("--- %s seconds ---" % (time.time() - start_time))

E_dif = E_array[-1] - E_array[0]
print(E_dif)

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, x_array, label='x (m)')
plt.plot(t_array, v1_array,label='v1 (m/s)')
#plt.plot(t_array, v2_array,label='v2 (m/s)')
plt.plot(t_array, E_array,label='E (J)')
#plt.plot(t_array, y,label='y (m)')
plt.legend()
plt.show()
