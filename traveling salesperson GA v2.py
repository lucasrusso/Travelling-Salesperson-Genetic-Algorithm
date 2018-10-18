# GA for the TRAVELING SALESPERSON problem

import numpy as np
import matplotlib.pyplot as plt

# defining the functions: ------------------------------------------------------

def trav_slpers_model (distances_matrix, pop_size, kid_numb, epochs, progress=False):
    
    avg_route_cost = np.zeros(shape=(epochs+1,2))  
    e = 0
    while (e < epochs+1):
        #print('e =', e)
        if progress == True:
            print('progress =', e, '/', epochs)
        
        #defining population to be used
        
        if e == 0:
            #creating first population
            pop = np.zeros(shape=(pop_size,len(distances_matrix[0]))).astype(int, copy=False)
            for i in range (pop_size):
                route = np.arange(len(distances_matrix[0,:]))
                np.random.shuffle(route)
                pop[i] = route
            
        else:
            pop = new_pop
                  
        #creating kids
        #selecting parents
        parents = np.random.choice(pop_size, size = kid_numb, replace=False)
        #creating kids = parents
        kids = np.zeros(shape=(kid_numb,len(distances_matrix[0])))
        for i in range(kid_numb):
            kids[i,:] = pop[parents[i],:]
        #mutating kids
        kids_old_aux = np.zeros(shape=(1,len(distances_matrix[0])))
        for i in range(kid_numb):
            permutations = np.random.choice(len(distances_matrix[0]), size = 2, replace=False)
            kids_old_aux[:,:] = kids[i,:]
            kids[i, permutations[0]] = kids_old_aux[0, permutations[1]]
            kids[i, permutations[1]] = kids_old_aux[0, permutations[0]]
            
        #battling in pop+kids & eliminating the worse
        pop_tot = np.append(arr = pop, values = kids, axis = 0).astype(int, copy=False)
        #calculating the cost of each pop_element = route
        pop_ind_cost = np.zeros(shape=( len(pop_tot[:,1]) ) ).reshape(-1,1)
        for i in range (len(pop_tot[:,1])):
            t = 0
            for j in range (len(distances_matrix[0])-1):
                t = t + distances_matrix[pop_tot[i,j], pop_tot[i,j+1]]
            j = j+1
            t = t + distances_matrix[pop_tot[i,j], pop_tot[i,0]]
            pop_ind_cost[i,0] = t
       
        #merging the costs with the population
        pop_w_cost = np.append( pop_tot, pop_ind_cost, axis=1 ) 
        #order by cost
        pop_w_cost = pop_w_cost[pop_w_cost[:,-1].argsort(kind='mergesort')]
        
        #eliminating the worse pop_elements from the population
        new_pop = np.zeros(shape=(pop_size,len(distances_matrix[0])))
        new_pop = pop_w_cost[:pop_size, :len(distances_matrix[0])]
        
        #saving average pop cost
        a = np.sum(pop_w_cost[:pop_size, -1]) / pop_size
        avg_route_cost[e,0:2] = (a,e)
        
        #updating epoch
        e = e + 1
        
    return (new_pop, avg_route_cost)
    
 
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

#using the program: ------------------------------------------------------------

distances_matrix = random_sim_matrix(10)
nova_pop, custo_med_rotas = trav_slpers_model(
        distances_matrix, pop_size=500, kid_numb=100, epochs=1000, progress=True)

#SUGESTION: PASS A STARTING POINT TO THE FUNCTION

#ploting the graph:
plt.plot(custo_med_rotas[:,1], custo_med_rotas[:,0], color = 'blue') 
plt.title('AG para o problema do "caixero viajante"')
plt.xlabel('epocas')
plt.ylabel('custo medio da populacao')
plt.show()