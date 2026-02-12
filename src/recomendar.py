def recommend_products(user, db):
    country = db.get_user_country(user)
    if country == 'Brazil':
        return db.get_brazilian_products()
    return []

def recommend_products_fair(user, db):
    return db.get_all_products()


