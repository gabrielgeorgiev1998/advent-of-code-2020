input_str = """##.#####
#.##..#.
.##...##
###.#...
.#######
##....##
###.###.
.#.#.#.."""


import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

def evolve_cube(state, i, j, k, p):
  alive_around = np.sum(state[
    (i-1 if i>0 else 0):(i+2 if (i+1)<state.shape[0] else state.shape[0]-1),
    (j-1 if j>0 else 0):(j+2 if (j+1)<state.shape[1] else state.shape[1]-1),
    (k-1 if k>0 else 0):(k+2 if (k+1)<state.shape[2] else state.shape[2]-1),
    (p-1 if p>0 else 0):(p+2 if (p+1)<state.shape[3] else state.shape[3]-1)]) - state[i,j,k,p]
  if((state[i,j,k,p]==1 and (alive_around==2 or alive_around==3)) or (state[i,j,k,p]==0 and alive_around==3)):
    return 1
  return 0



def expand_dims(state):
  new_state = np.zeros((state.shape[0]+2, state.shape[1]+2, state.shape[2]+2, state.shape[3]+2))
  for i in range(1, state.shape[0]+1):
    for j in range(1, state.shape[1]+1):
      for k in range(1, state.shape[2]+1):
        new_state[i, j, k, 1:-1] = state[i-1,j-1, k-1]
  return new_state

def evolve_state(state):
  expanded_state = expand_dims(state)
  new_state = np.zeros(expanded_state.shape)
  x,y,z,w = new_state.shape
  for i in range(x):
    for j in range(y):
      for k in range(z):
        for p in range(w):
          new_state[i,j,k,p] = evolve_cube(expanded_state, i, j, k, p)

  return new_state
  




dims = (len(input_str.splitlines()), len(input_str.splitlines()[0]))
state = np.zeros(dims)

for i in range(8):
  for j in range(8):
    if input_str.splitlines()[i][j]=="#":
      state[i, j] = 1
    else:
      state[i,j] = 0


state = np.stack((
  np.zeros((8,8)),
  state,
  np.zeros((8,8))), axis=0)

state = np.stack((
  np.zeros((3,8,8)),
  state,
  np.zeros((3,8,8))
), axis=0)


for i in range(6):
  state = evolve_state(state)

print(state.sum())
