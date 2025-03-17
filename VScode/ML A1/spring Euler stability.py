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

dt_array = np.arange(0.005, 0.02, 0.001)   #Eukler method break down is dependent on sampling position, is generally unstable everywhere
V_Edif_array = np.zeros(len(dt_array))

x_list = []
v_list = []
e_list = []
p_list = []
E_list = []

t_max = 1000

for j in range(len(dt_array)):

    
    t_array = np.arange(0, t_max, dt_array[j])

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
        x = x + dt_array[j] * v
        v = v + dt_array[j] * a
        e = 0.5*m*v**2
        p = 0.5*k*x**2
        E = e + p


    # convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
    x_array = np.array(x_list)
    v_array = np.array(v_list)
    e_array = np.array(e_list)
    p_array = np.array(p_list)
    E_array = np.array(E_list)

    V_Edif_array[j] = E_array[-1] - E_array[0]


print("--- %s seconds ---" % (time.time() - start_time))
print(V_Edif_array)

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
#plt.plot(t_array, x_array, label='x (m)')
#plt.plot(t_array, v1_array,label='v1 (m/s)')
#plt.plot(t_array, v2_array,label='v2 (m/s)')
#plt.plot(t_array, E_array,label='E (J)')
#plt.plot(t_array, y,label='y (m)')
plt.plot(dt_array, V_Edif_array,label='Euler E')
plt.legend()
plt.show()