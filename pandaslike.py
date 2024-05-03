def load_users():
    users = {}
    file = open('user.csv', 'r')
    header_skipped = False  # Menandakan apakah header sudah dilewati
    user_data = []  # List untuk menampung data satu pengguna
    attribute = ""  # String untuk menampung nilai atribut saat ini
    for line in file:
        if not header_skipped:
            header_skipped = True
            # Lewati baris header pertama
        else:
            for char in line:
                if char == ';' or char == '\n':
                    # Jika karakter ';' atau karakter baris baru '\n' ditemukan, tambahkan nilai atribut ke dalam list data pengguna
                    user_data.append(attribute)
                    attribute = ""  # Reset string untuk nilai atribut berikutnya
                    if char == '\n':
                        # Jika karakter baris baru ditemukan, proses data pengguna dan tambahkan ke dalam dictionary
                        user_id = int(user_data[0])
                        username = user_data[1]
                        password = user_data[2]
                        role = user_data[3]
                        oc = int(user_data[4])
                        users[user_id] = {'username': username, 'password': password, 'role': role, 'oc': oc, 'login_status': False}
                        # Reset list untuk data pengguna berikutnya
                        user_data = []
                else:
                    # Tambahkan karakter ke nilai atribut saat ini
                    attribute += char
    return users


def load_monsters():
    monsters = {}
    file = open('monster.csv', 'r')
    header_skipped = False
    monster_data = []  # List untuk menampung data satu monster
    attribute = ""     # String untuk menampung nilai atribut saat ini
    for line in file:
        if not header_skipped:
            header_skipped = True
        # Lewati baris header pertama
        else:
            for char in line:
                if char == ';' or char == '\n':
                    # Jika karakter titik koma atau baris baru ditemukan, tambahkan nilai atribut ke dalam list data monster
                    monster_data.append(attribute)
                    attribute = ""  # Reset string untuk nilai atribut berikutnya
                else:
                    attribute += char  # Tambahkan karakter ke nilai atribut saat ini
            if len(monster_data) == 5:  # Pastikan panjang data sesuai dengan jumlah atribut yang diharapkan
                monster_id = int(monster_data[0])
                monster_type = monster_data[1]
                atk_power = int(monster_data[2])
                def_power = int(monster_data[3])
                hp = int(monster_data[4])
                monsters[monster_id] = {'type': monster_type, 'atk_power': atk_power, 'def_power': def_power, 'hp': hp}
                monster_data = []  # Reset list untuk data monster berikutnya
    return monsters


def save_users(users):
    file = open('user.csv', 'w')
    file.write("id;username;password;role;oc\n")
    for user_id in users:  # Iterasi langsung pada kunci-kunci dictionary
        user_data = users[user_id]  # Dapatkan nilai pengguna berdasarkan kunci
        # Tulis data pengguna ke dalam file
        file.write(f"{user_id};{user_data['username']};{user_data['password']};{user_data['role']};{user_data['oc']}\n")
    file.close()

# Fungsi untuk menyimpan pilihan monster ke dalam file monster_inventory.csv
def save_monster_inventory(user_id, monster_id):
    file = open('monster_inventory.csv', 'a')
    file.write(f"{user_id},{monster_id},1\n")
    print("Pilihan monster berhasil disimpan!")