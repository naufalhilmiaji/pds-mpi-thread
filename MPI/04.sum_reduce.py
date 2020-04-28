# import mpi4py
from mpi4py import MPI
import random
import numpy as np

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

jumlah = 0
# generate angka integer secara random untuk setiap proses
rand = random.randint(1,20)
nilai = np.array(rand)

print('Rank: '+str(rank)+', nilai: '+str(nilai))

jumlah = np.array(0)
# lakukam penjumlahan dengan teknik reduce, root reduce adalah proses dengan rank 0
comm.Reduce(nilai, jumlah, op=MPI.SUM, root=0)

# jika saya proses dengan rank 0 maka saya akan menampilkan hasilnya
if rank==0:
    print('--------------------')
    print('Jumlah: '+str(jumlah))
