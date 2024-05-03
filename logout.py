def logout(user, login):
    username = input("Masukan username yang akan logout: ")

    for user_id in user:
        if user[user_id]['username'] == username:
            if username in login:
                print("Logout berhasil!")
                login.remove(username)
                return False
            else:
                print("Logout gagal!")
                print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
                return False
    
    print("Logout gagal!")
    print("Username tidak ditemukan")
    return True