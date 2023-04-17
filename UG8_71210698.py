class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
     
    def getNamaPelanggan(self):
        return self._namaPelanggan
    
    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru
        

class Kasir:
    DEFAULT_CAPACITY = 3 #isi sesuai dengan ketentuan soal
    def __init__(self): #konstruktor
       pass
       self._data = [None] * Kasir.DEFAULT_CAPACITY
       self._size = 0
       
    def __len__(self): #mengembalikan ukuran Queue
        pass
        return self._size

    def is_empty(self): #mengecek apakah Queue kosong ?
        pass
        return self._size == 0

    def dequeue(self): #menghapus data paling depan (front)
        pass
        if self.is_empty():
            print("Kasir kosong.")
            return None
        else:
            front = self._data[0]
            for i in range(self._size - 1):
                self._data[i] = self._data[i + 1]
            self._data[self._size - 1] = None
            self._size -= 1
            return front

    def enqueue(self, namaPelanggan): #menambah data ke list
        pass
        if self._size == len(self._data):
            self.resize(2 * len(self._data))
        self._data[self._size] = NodePelanggan(namaPelanggan)
        self._size += 1

    def resize(self, cap): #mengubah ukuran queue pada list
        pass
        old_data = self._data
        self._data = [None] * cap
        for i in range(self._size):
            self._data[i] = old_data[i]
    
    def printAll(self): #menampilkan daftar pelanggan dalam sebuah kasir
        pass
        print("=== Kasir ===")
        for i in range(self._size):
            print(f"{i + 1}. {self._data[i].getNamaPelanggan()}")
        for i in range(self._size, len(self._data)):
            print(f"{i + 1}. Kosong")
        print("")
        

# test case program
tempatKasir = Kasir()
tempatKasir.enqueue("Haniif")
tempatKasir.enqueue("Sindu")
tempatKasir.enqueue("Dedi")
tempatKasir.printAll()

tempatKasir.enqueue("Beatrix")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

tempatKasir.enqueue("Shalom")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

