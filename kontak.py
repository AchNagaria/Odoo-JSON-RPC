from argparse import ArgumentParser #fungsinya : untuk memanggil argumen yang sudah dibuat dan diexecute oleh user
from kontak_odoorpc import kontakAPI #fungsinya : memanggil Class kontakAPI didalam file kontak_odoorpc


"""
args.command adalah perintah yang disediakan, dan args.params adalah parameter tambahan untuk perintah.
"""
parser = ArgumentParser()
parser.add_argument(
    'command',
    choices=['list', 'add', 'set', 'del'])
parser.add_argument('params', nargs='*')
args = parser.parse_args() 

"""
Di bagian ini kalian harus menyesuaikannya dengan settingan instalisasi Odoo masing-masing. 
Perintah dari tujuan ini agar dapat terhubung ke dalam Odoo menggunankan 
localhost, port, dan db yang kita pakai.
"""
srv, port, db = '192.168.56.105', 8012, 'Nagaria'
user, pwd = 'ach.nagaria@gmail.com', 'agam12345'
api = kontakAPI(srv, port, db, user, pwd)


"""
Di sini kami menggunakan metode kontakAPI.search_read() untuk 
mengambil daftar catatan kontak dari server, kami kemudian mengulangi 
setiap elemen dalam daftar dan mencetaknya, kita gunakan Python string formatting 
untuk menyajikan setiap catatan kontak kepada pengguna.
"""
if args.command == 'list':
    text = args.params[0] if args.params else None
    kontak = api.search_read(text)
    for k in kontak:
        print('%(id)d %(name)s' % k)

"""
Untuk menambahkan kontak kita menggunakan method api.create()
"""
if args.command == 'add':
    for name in args.params:
        new_id = api.create(name)
        print('Contact added with ID %d.' % new_id)

"""
Untuk men-set/edit nama kontak yang sudah ada kita menggunakan method api.write()
"""
if args.command == 'set':
    if len(args.params) != 2:
        print("Set command requires a name and ID.")
    else:
        k_id, name = int(args.params[0]), args.params[1]
        api.write(name, k_id)
        print('Name set for ID %d.' % k_id)
"""
Untuk menghapus kontak yang sudah ada kita menggunakan method api.unlink()
"""
if args.command == 'del':
    for param in args.params:
        api.unlink(int(param))
        print('Contact with ID %s was deleted.' % param)
