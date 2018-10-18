# GA for the TRAVELING SALESPERSON problem

import numpy as np

# defining the functions: -----------------------------
def random_sim_matrix(n):
    d = np.arange(1, n*n+1)
    np.random.shuffle(d)
    d = d.reshape(n,n)
    for i in range (n):
        for j in range (n):
            if i == j:
                d[i,j]=0
            else:
                d[i,j]=d[j,i]
    return d

def create_route (distances_matrix):
    route = np.arange(len(distances_matrix[0,:]))
    np.random.shuffle(route)
    return route

def route_cost (routes, distances_matrix):
    t = 0
    for i in range(len(routes)-1):
        #print('i =', i, 't =', t, d[r[i],r[i+1]])
        t = t + distances_matrix[routes[i],routes[i+1]]
    i = i+1
    #print('i =', i, 't =', t, d[r[i],0])
    t = t + distances_matrix[routes[i],routes[0]]
    return t

#creating the arrays: ----------------------------------

distances = random_sim_matrix(10)

route = create_route(distances)

tot_cost = route_cost(route, distances)

#creating a population of routes: ----------------------

def pop(element, amount):
    pop = []
    for i in range (amount):
        pop = np.append(pop, element)
    pop = pop.reshape(amount,amount)
    return pop

population = pop(element=create_route(distances), amount=10)

