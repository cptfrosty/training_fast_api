import  database_scripts as db_scripts

def get_items():
    return db_scripts.select_items()

def get_item(item_id):
    result = db_scripts.select_items(item_id)
    return result