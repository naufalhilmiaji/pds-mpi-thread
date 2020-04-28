from mpi4py import MPI
import numpy as np

# buat fungsi dekomposisi bernama local_loop 
# local_loop akan menghitung setiap bagiannya
# gunakan 4/(1+x^2), perhatikan batas awal dan akhir untuk dekomposisi
# misalkan size = 4 maka proses 0 menghitung 0-25, proses 1 menghitung 26-50, dst
def local_loop(num_steps,begin,end):
    step = 1.0/num_steps
    summ = 0
    # 4/(1+x^2)
    for i in range(begin,end):
        x= (i+0.5)*step
        summ = summ + 4.0/(1.0+x*x)
    
    print(summ)
    return summ    

# fungsi Pi
def Pi(num_steps):
    
    # buat COMM
    comm = MPI.COMM_WORLD
    
    # dapatkan rank proses
    rank = comm.Get_rank()
    
    # dapatkan total proses berjalan
    size = comm.Get_size()
    
    # buat variabel baru yang merupakan num_steps/total proses
    nstp = int(num_steps/size) 

    for i in range(size):
        if rank == i:
            x = i+1
            begin = i*nstp
            end = x*nstp-1
        else:
            None
    
    # cari local_sum
    # local_sum merupakan hasil dari memanggil fungsi local_loop
    local_sum = local_loop(num_steps, begin, end)
    
    # lakukan penjumlahan dari local_sum proses-proses yang ada ke proses 0
    # bisa digunakan reduce atau p2p sum
    value = np.array(local_sum,'d')
    value_sum = np.array(0.0,'d')

    comm.Reduce(value, value_sum, op=MPI.SUM, root=0)
    
    # jika saya proses dengan rank 0  maka tampilkan hasilnya
    if rank == 0:
        pi = value_sum / num_steps
        print('---------------------- +')
        print('value_sum: '+str(value_sum))
        print ('Pi with '+str(num_steps)+' steps is '+str(pi))
    
# panggil fungsi utama    
if __name__ == '__main__':
    Pi(10000)