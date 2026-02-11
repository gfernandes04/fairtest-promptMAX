def listar_produtos(db):
    return db.get_all_products()

def listar_produtos_por_categoria(db, categoria):
    return db.get_products_by_category(categoria)

def listar_produtos_por_marca(db, marca):
    return db.get_products_by_brand(marca)
