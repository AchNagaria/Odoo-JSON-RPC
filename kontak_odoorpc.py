from odoorpc import ODOO

"""
Class kontakAPI ini berfungsi sebagai koneksi server ke Odoo, dan untuk mengimplementasikan objek Model dan Recordset, 
untuk modelnya menggunakan res.partner yang disimpan dalam atribut self.model
"""
class kontakAPI():

    """
    def__init__ adalah konstruktor, 
    konstruktor sendiri adalah method khusus yang akan dijalankan secara otomatis pada saat sebuah objek dibuat
    """
    def __init__(self, srv, port, db, user, pwd): 
        """
        self dalam bahasa pemrograman python dapat diartikan sebagai "class itu sendiri"
        fungsi dari self adalah memanggil sebuah metode di dalam sebuah class
        """
        self.api = ODOO(srv, port=port)
        self.api.login(db, user, pwd)
        self.uid = self.api.env.uid
        self.model = 'res.partner'
        self.Model = self.api.env[self.model]

    def execute(self, method, arg_list, kwarg_dict=None):
        return self.api.execute(
            self.model,
            method, *arg_list, **kwarg_dict)

    def search_read(self, text=None): #Fungsinya : agar metode ini dapat menerima ID/nama kontak yang dicari
        domain = [('name','ilike', text)] if text else []
        fields = ['id', 'name']
        return self.Model.search_read(domain or [], fields)

    
    def create(self, name):   #Fungsinya :agar metode ini dapat membuat kontak baru dengan nama yang diberikan
        vals = {'name': name}
        return self.Model.create(vals)
    
    
    def write(self, name, id):  #Fungsinya : untuk dapat melakukan aktivitas/menulis didalam kontak
        vals = {'name': name}
        self.Model.write(id, vals)

   
    def unlink(self, id): #Fungsinya : untuk menghapus ID dari kontak
        return self.Model.unlink(id)
   


if __name__ == '__main__':
    srv, port, db = '192.168.56.105', 8012, 'Nagaria'
    user, pwd = 'ach.nagaria@gmail.com', 'agam12345'
    api = LibraryAPI(srv, port, db, user, pwd)
    from pprint import pprint
    pprint(api.search_read())
