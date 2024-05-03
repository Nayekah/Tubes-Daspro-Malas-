import pandaslike as pd; import rng; import register; import login; import logout; import MenuandHelp as mh

users = pd.load_users()
logged_in_users = []

lobby = True    
while lobby:
    print("\n>>> REGISTER / LOGIN / LOGOUT")
    choice = input("Pilih aksi: ").upper()
    if choice == "REGISTER":
        register.register(users, logged_in_users)
    elif choice == "LOGIN":
        login.login(users, logged_in_users)
    elif choice == "LOGOUT":
        logout.logout(users, logged_in_users)
    elif choice == "HELP":
        mh.help(users, logged_in_users)
    else:
        print("Pilihan tidak valid!")