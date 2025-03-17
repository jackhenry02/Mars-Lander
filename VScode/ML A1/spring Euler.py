# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import time
start_time = time.time()

# mass, spring constant, initial position and velocity
m = 1
k = 1
x = 0
v = 1
e = 0.5*m*v**2
p = 0.5*k*x**2
E = e + p

# simulation time, timestep and time
t_max = 100
dt = 0.01 #Euler method breaks down more seriously using values of dt>0.01. Could possibly model using E_dif against dt
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
x_list = []
v_list = []
e_list = []
p_list = []
E_list = []

# Euler integration
for t in t_array:

    # append current state to trajectories
    x_list.append(x)
    v_list.append(v)
    e_list.append(e)
    p_list.append(p)
    E_list.append(E)

    # calculate new position and velocity
    a = -k * x / m
    x = x + dt * v
    v = v + dt * a
    e = 0.5*m*v**2
    p = 0.5*k*x**2
    E = e + p


# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array = np.array(x_list)
v_array = np.array(v_list)
e_array = np.array(e_list)
p_array = np.array(p_list)
E_array = np.array(E_list)


print("--- %s seconds ---" % (time.time() - start_time))

E_dif = E_list[-1] - E_list[0]
print(E_dif)

#analytical values
w = (k/m)**0.5
y = np.cos(w*t_array - np.pi/2)

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, x_array, label='x (m)')
plt.plot(t_array, v_array,label='v (m/s)')
#plt.plot(t_array, e_array,label='e (J)')
#plt.plot(t_array, p_array,label='p (J)')
plt.plot(t_array, E_array,label='E (J)')
plt.plot(t_array, y,label='y (m)')
plt.legend()
plt.show()
