
from sql_connection import get_sql_connection
import mysql.connector

def get_all_products(connection):
    cnx=connection

    cursor=cnx.cursor()

    query = ('''SELECT products.product_id,products.name,products.uom_id,products.price_per_unit, uom.uom_name
              FROM grocery_store.products 
              inner join uom on products.uom_id=uom.uom_id;''')

    cursor.execute(query)

    response=[]

    for (product_id, name,uom_id,price_per_unit,uom_name) in cursor:
        response.append(
            {
                'product_id':product_id,
                'name':name,
                'uom_id':uom_id,
                'price_per_unit':price_per_unit,
                'uom_name':uom_name
            }
        )

    return response


def insert_new_product(connection,product):
    cursor=connection.cursor()
    query=('INSERT INTO grocery_store.products (name,uom_id,price_per_unit,product_id) VALUES (%s, %s, %s, %s)')
    data=(product['name'],product['uom_id'],product['price_per_unit'],product['product_id'])
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection,product_id):
    cursor=connection.cursor()
    query=('DELETE FROM grocery_store.products WHERE product_id=' + str(product_id))
    cursor.execute(query)
    connection.commit()

if __name__=='__main__':
     connection=get_sql_connection()
     print(delete_product(connection,14))



