#import socket, sys, traceback dan threading
import socket, sys, traceback
from threading import Thread

# jalankan server
def main():
    start_server()

# fungsi saat server dijalankan
def start_server():
    # tentukan IP server
    ip_server = "192.168.43.115"
    
    # tentukan port server
    port = 60000

    # buat socket bertipe TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # option socket
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket dibuat")

    # lakukan bind
    try:
      s.bind((ip_server, port)) 
    except:
        # exit pada saat error
        print("Bind gagal. Error : " + str(sys.exc_info()))
        sys.exit()

    # listen hingga 5 antrian
    s.listen(5)
    print("Socket mendengarkan")


    # infinite loop, jangan reset setiap ada request
    while True:
        # terima koneksi
        connection, address = s.accept()
        
        # dapatkan IP dan port
        ip, port = str(address[0]), str(address[1])
        print("")
        print("Connected dengan " + ip + ":" + port)

        # jalankan thread untuk setiap koneksi yang terhubung
        try:
            Thread(target=clientThread, args=(connection, ip, port)).start()
        except:
            # print kesalahan jika thread tidak berhasil dijalankan
            print("Thread tidak berjalan.")
            traceback.print_exc()

    # tutup socket
    s.close()


def clientThread(connection, ip, port, max_buffer_size = 4096):
    # flag koneksi
    is_active = True

    # selama koneksi aktif
    while is_active:

        # terima pesan dari client
        data = connection.recv(max_buffer_size)
        
        # dapatkan ukuran pesan
        client_input_size = sys.getsizeof(data)
        
        # print jika pesan terlalu besar
        if client_input_size > max_buffer_size:
            print("The input size is greater than expected {}")

        # dapatkan pesan setelah didecode
        client_input = data.decode()

        # jika "quit" maka flag koneksi = false, matikan koneksi
        if "quit" in client_input:
            # ubah flag
            is_active = False
            print("")
            print("Client meminta keluar")
            
            # matikan koneksi
            connection.close()
            print("Connection " + ip + ":" + port + " ditutup")
            
        else:
            # tampilkan pesan dari client
            print("Pesan dari client: {}".format(client_input))
            connection.sendall("-".encode("utf8"))
            
# panggil fungsi utama
if __name__ == "__main__":
    main()
