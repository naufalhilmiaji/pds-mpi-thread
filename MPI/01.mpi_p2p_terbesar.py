# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# jika saya rank terbesar maka saya akan mengirimkan pesan ke proses yang mempunyai rank 0 s.d rank terbesar-1
if rank == size-1:
    for i in range(0, size-1):
        data = 'Hello, rank '+str(i)+'! A message from rank '+str(rank)
        comm.send(data, dest=i)

# jika saya bukan rank terbesar maka saya akan menerima pesan yang berasal dari proses dengan rank terbesar
else:
    data = comm.recv(source=size-1)
    print('Received data: "'+ data+'" -> (terbesar)')
