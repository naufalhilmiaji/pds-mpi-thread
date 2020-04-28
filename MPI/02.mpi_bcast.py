# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

pesan = 'HALO!'
data = comm.bcast(pesan, root=0)

# jika saya rank 0 maka saya akan melakukan broadscast
if rank == 0:
    print('Broadcast data:', data+'\n')
    
# jika saya bukan rank 0 maka saya menerima pesan
else:
    print('Received data: "'+ data+'"')