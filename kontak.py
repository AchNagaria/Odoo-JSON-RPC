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
Di sini kami menggunakan metode kontakAPI.search_read () untuk mengambil daftar catatan kontak dari server, 
kami kemudian mengulangi setiap elemen dalam daftar dan mencetaknya, 
kita gunakan Python string formatting untuk menyajikan setiap catatan kontak kepada pengguna.
"""
if args.command == 'list':
    text = args.params[0] if args.params else None
    kontak = api.search_read(text)
    for k in kontak:
        print('%(id)d %(name)s' % k)

"""
Di sini kita hanya perlu memanggil metode write dan menunjukkan hasilnya  kepada end user.
"""
if args.command == 'add':
    for name in args.params:
        new_id = api.create(name)
        print('k added with ID %d.' % new_id)


if args.command == 'set':
    if len(args.params) != 2:
        print("set command requires a name and ID.")
    else:
        k_id, name = int(args.params[0]), args.params[1]
        api.write(name, k_id)
        print('name set for k ID %d.' % k_id)

if args.command == 'del':
    for param in args.params:
        api.unlink(int(param))
        print('k with ID %s was deleted.' % param)
