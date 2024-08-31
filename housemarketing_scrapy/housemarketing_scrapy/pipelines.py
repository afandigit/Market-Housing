from itemadapter import ItemAdapter
import mysql.connector

class HousemarketingScrapyPipeline:
    def process_item(self, item, spider):
        return item

class SaveToMySqlPipeline:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host	  = 'localhost',
            user 	  = 'root',
            password  = 'root',
            database  = 'real_estate_db'
        )

        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS real_estate_data(
            id int NOT NULL auto_increment,
            advertisement_url VARCHAR(255),
            advertisement_type enum("sell","rental","vacation_rental", "none"),
            title VARCHAR(255),
            publication_date VARCHAR(255),
            price VARCHAR(255),
            location VARCHAR(255),
            description TEXT,
            complete_description TEXT,
            features_list VARCHAR(255),
            insert_date TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
            website_name VARCHAR(255),
            PRIMARY KEY (id)
            )
        """)

    def process_item(self, item, spider):

        ## Define insert statement
        # self.cur.execute(""" insert into mubawab_rental (
        self.cur.execute(""" insert into real_estate_data (
            advertisement_url,
            advertisement_type,
            title,
            publication_date,
            price,
            location,
            description,
            complete_description,
            features_list,
            website_name
            ) values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )  
            """ , (
                item["advertisement_url"],
                item["advertisement_type"],
                item["title"],
                item["publication_date"],
                item["price"],
                item["location"],
                item["description"],
                item["complete_description"],
                item["features_list"],
                item["website_name"]
            ))
        
        ## Execute insert of data into database
        self.conn.commit()
        return item

    def close_spider(self, spider):

        ## Close cursor & connection to database
        self.cur.close()
        self.conn.close()
