import pandaslike as pd

# Implementasi fungsi-fungsi lainnya seperti pada implementasi sebelumnya
# Fungsi untuk melakukan registrasi pengguna baru
def register(users, login):
    username = input("Masukan username: ")
    password = input("Masukan password: ")
    Berhasil = False

    validate = True
    while validate :
        for user_id in users:
            if users[user_id]['username'] == username:
                if users[user_id]['login_status'] == True:
                    print("Anda telah login dengan username", login[0], ", silahkan lakukan 'LOGOUT' sebelum melakukan register.")
                    break

        username_taken = False
        for user_id in users:
            if users[user_id]['username'] == username:
                username_taken = True
                break
    
        while username_taken:
            print("Username sudah digunakan, silakan coba lagi.")
            username = input("Masukan username: ")
            password = input("Masukan password: ")
        
            # Ulangi validasi untuk username yang baru dimasukkan
            username_taken = False
            for user_id in users:
                if users[user_id]['username'] == username:
                    username_taken = True
                    break

        # Validasi apakah username sudah digunakan atau tidak valid
        while not is_valid_username(username, users):
            print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
            username = input("Masukan username: ")
            password = input("Masukan password: ")

        # Validasi jika password kosong
        if not password:
            print("Password tidak boleh kosong!")
            return False

    # Validasi jika password hanya terdiri dari spasi
        is_space_only = True
        for char in password:
            if char != ' ':
                is_space_only = False
                break

        if is_space_only:
            print("Password tidak boleh hanya terdiri dari spasi!")
            return False
        
        # Temukan ID pengguna yang belum digunakan
        user_id = 1
        while user_id in users:
            user_id += 1
    
        # Tambahkan pengguna baru ke dalam dictionary users
        users[user_id] = {'username': username, 'password': password, 'role': 'agent', 'oc': 0}
        print("Pendaftaran berhasil!")
        pd.save_users(users)
        Berhasil = True
        validate = False

        if Berhasil == True:
            monsters = pd.load_monsters()

            # Load data pengguna untuk mendapatkan user ID
            user = pd.load_users()

            print("Silahkan pilih salah satu monster sebagai monster awalmu.")
            for monster_id in monsters:  # Menggunakan loop langsung dari keys()
                monster_data = monsters[monster_id]
                print(f"{monster_id}. {monster_data['type']}")
            choice = int(input("\nMonster pilihanmu: "))

            user_id = len(user)  # Asumsi user baru akan memiliki user ID terakhir
            pd.save_monster_inventory(user_id, choice)

def is_valid_username(username, users):
    # Validasi apakah username hanya berisi alfabet, angka, underscore, dan strip
    if not username:
        return False
    
    valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_- '
    
    for char in username:
        if char not in valid_chars:
            return False
    
    # Validasi apakah username sudah digunakan
    for user_id in users:
        if users[user_id]['username'] == username:
            return False
    return True