class Node:
    def __init__(self, data, priority):
        self._data = data
        self._priority = priority # 1 (tertinggi), 2, 3, 4, ...
        self._next = None

class PriorityQueueUnsorted:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False

    def __len__(self):
        return self._size
        
    def add(self, data, priority):
        baru = Node(data, priority)
        if self.is_empty(): # kosong
            self._head = baru
            self._tail = baru
        else: # insert belakang
            self._tail._next = baru
            self._tail = baru
        self._size = self._size + 1

    def remove(self): # implementasi ini tidak return
        if not self.is_empty():
            if self._size == 1:
                bantu = self._head
                self._head = None
                self._tail = None
                del bantu
            else:
                # ambil prioritas pada head sebagai prioritas tertinggi yang diketahui
                min_priority = self._head._priority
                # cek dari head sampai tail, berapa prioritas tertinggi
                hapus = self._head
                while hapus != None:
                    if hapus._priority < min_priority:
                        min_priority = hapus._priority
                    hapus = hapus._next
                # prioritas tertinggi sudah diketahui, letakkan hapus di node tersebut
                hapus = self._head
                while hapus._priority != min_priority:
                    hapus = hapus._next
                # cek yang akan dihapus itu head, tail, atau tengah?
                if hapus == self._head:
                    # hapus head
                    self._head = self._head._next
                    del hapus
                else:
                    # hapus tail atau tengah caranya sama saja
                    # letakkan bantu di posisi sebelum hapus
                    bantu = self._head
                    while bantu._next != hapus:
                        bantu = bantu._next
                    # hapus node
                    bantu._next = hapus._next
                    del hapus
                    # pastikan tail di posisi paling belakang
                    self._tail = self._head
                    while self._tail._next != None:
                        self._tail = self._tail._next
        self._size = self._size - 1
    
    def peek(self): # return dalam bentuk tuple (data, priority)
        if self.is_empty() == True:
            return None
        else:
            if self._size == 1:
                return tuple([self._head._data, self._head._priority])
            else:
                min_priority = self._head._
