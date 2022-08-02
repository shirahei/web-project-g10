from utilities.db.db_manager import dbManager

class Items:
    @staticmethod
    def insert_item(owner_id,title ,category,condition,description,image):
        return dbManager.commit(
            f"INSERT INTO items (owner_id,name, category,condition_status,description,png_url) VALUES ({owner_id},'{title}', '{category}','{condition}','{description}', '{image}')")

    def search_item(category,condition):
        return dbManager.fetch(f"SELECT * FROM items inner join "
                               f" customers cus on items.owner_id=cus.customer_id"
                               f"  WHERE category='{category}' AND condition_status='{condition}' ")

    def get_my_items(ownerID):
        return dbManager.fetch(f"SELECT * FROM items WHERE owner_id={ownerID}")

    def get_item_by_id(itemID,ownerID):
        return dbManager.fetch(f"SELECT * FROM items WHERE owner_id={ownerID} and item_id={itemID}")

    def remove_item(itemID,ownerID):
        return dbManager.commit(
            f"DELETE FROM items WHERE owner_id={ownerID} AND item_id={itemID}")

    def edit_item(itemID,category,condition,description,name):
        return dbManager.commit(
            f"UPDATE items SET condition_status='{condition}',category='{category}',name='{name}',description='{description}' "
            f"WHERE item_id={itemID}")

