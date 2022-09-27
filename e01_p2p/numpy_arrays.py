from mpi4py import MPI

import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = np.arange(1000, dtype='i')
    comm.Send([data, MPI.INT], dest=1, tag=77)
elif rank == 1:
    data = np.empty(1000, dtype='i')
    comm.Recv([data, MPI.INT], source=0, tag=77)

print(rank, data[:10])
