
import math
import networkx as nx




def hoe_bound(i, m, n, delta, T):
    delta_p = 6 * delta / math.pi**2 / n / T**2
    return R*math.sqrt(math.log(1/delta_p)/2/m[i])


def is_neighbor(x, y, b, mean_reward, m, n, delta, T):
    if x == y:
        return 0
    dif = abs(mean_reward[x]-mean_reward[y])
    bound = b*(hoe_bound(x, m, n, delta, T) + hoe_bound(y, m, n, delta, T))
    if dif < bound:
        return 1
    else:
        return 0



def update_G(i, G, b, mean_reward, m, n, delta, T):
    neighbors = list(G[i])
    for j in neighbors:
        if not is_neighbor(i,j, b, mean_reward, m, n, delta, T):
            G.remove_edge(i,j)            
            


def update(T, D, S, communities, G):
    for com in ccommunities:
        if len(com)<= n*(1-rho):
            for j in com:
                D.add(j)
                G.remove_node(j)
                S[j] = T
    return D


def Gold(Psi, epsilon, rho, delta):
    R = 1
    n = len(Psi)
    T = 0
    N = set(range(0, n))
    m = [0 for i in range(n)]
    mean_reward= [0 for i in range(n)]
    S = [0 for i in range(len(N))]
    b = (1+math.e**(1/16)+epsilon)/(1-math.e**(1/16)+epsilon)
    for i in N:
        mean_reward[i] = Psi[i][m[i]]
        m[i]+=1
        T +=1
    G = nx.Graph()
    for i in N:
        for j in N:
            if i != j:
                G.add_edge(i, j)         
    D = set()
    while len(D) < n*(1-rho):
        M = N-D
        for i in M:
            mean_reward[i] = (mean_reward[i] * m[i] + Psi[i][m[i]])/(m[i]+1)
            m[i]+=1
            T += 1
            update_G(i, G, b, mean_reward, m, n, delta, T)
            communities = list(nx.connected_components(G))
            D = update(T, D, S, communities, G)
    Omega = sorted(N, key=lambda x:sus[x])
    return Omega


def main():
  Psi = [[]] #the list of arms with rewards. E.g., Psi[0][0] means the frist reward of arm $0$.
  epsilon = 2.5 #default value
  rho = 0.1 # the maximal percent of outlier arms in N
  delta = 0.1 #default value
  print( Gold(Psi, epsilon, rho, delta) )
  
if __name__== "__main__":
  main()

