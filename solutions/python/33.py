def search_names(logins):
    return filter(lambda login: login and login[0].endswith('_'), logins)