# import mpi4py
from mpi4py import MPI
import random

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

jumlah = 0
# generate angka integer secara random untuk setiap proses
nilai = random.randint(1,20)

print('Rank: '+str(rank)+', nilai: '+str(nilai))
# jika saya adalah proses dengan rank 0 maka:
# saya menerima nilai dari proses 1 s.d proses dengan rank terbesar
# menjumlah semua nilai yang didapat (termasuk nilai proses saya)

if rank == 0:
    jumlah += nilai
    for i in range(1, size):
        data = comm.recv(source=i)
        jumlah += data
    print('--------------------')
    print('Jumlah: '+str(jumlah))
    
# jika bukan proses dengan rank 0, saya akan mengirimkan nilai proses saya ke proses dengan rank=0
else:
    comm.send(nilai, dest=0)