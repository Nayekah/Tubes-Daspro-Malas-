def help(user, login):
    if len(login) == 0:
        print("Kamu harus login dulu")
    else:
        for user_id in user:
            if user[user_id]['username'] == login[0]:
                if user[user_id]['role'] == "agent":
                    print("Halo", login[0])
                elif user[user_id]['role'] == 'admin':
                    print("Halo Admin", login[0])