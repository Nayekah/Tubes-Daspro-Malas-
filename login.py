def login(users, login):
    username = input("Masukan username: ")
    password = input("Masukan password: ")

    for user_id in users:
        if users[user_id]['username'] == username:
            if users[user_id]['password'] == password:
                if users[user_id]['login_status'] == True:
                    print("Anda telah login dengan username", login[0], ", silahkan lakukan 'LOGOUT' sebelum melakukan login kembali.")
                    return False
                else:
                    users[user_id]['login_status'] = True
                    login.append(username)
                    print("Login berhasil!")
                    return False
            else:
                print("Password salah!")
                return False

    print("Username tidak ditemukan")
    return True