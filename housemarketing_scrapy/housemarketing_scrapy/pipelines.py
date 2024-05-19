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
            database  = 'mubawab'
        )

        self.cur = self.conn.cursor()
        # self.cur.execute("""
        #     DROP TABLE IF EXISTS house_advertisements
        # """)
        # house_advertisements_cleaned_data
        # avito_house_advertisements_cleaned_data
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS house_advertisements_cleaned_data(
            id int NOT NULL auto_increment,
            advertisement_url VARCHAR(255),
            title VARCHAR(255),
            publication_date VARCHAR(255),
            price VARCHAR(255),
            location VARCHAR(255),
            description TEXT,
            complete_description TEXT,
            features_list VARCHAR(255),
            insert_date DATE DEFAULT (CURRENT_DATE),
            PRIMARY KEY (id)
            )
        """)

    def process_item(self, item, spider):

        ## Define insert statement
        self.cur.execute(""" insert into house_advertisements_cleaned_data (
            advertisement_url,
            title,
            publication_date,
            price,
            location,
            description,
            complete_description,
            features_list
            ) values ( %s, %s, %s, %s, %s, %s, %s, %s )  
            """ , (
                item["advertisement_url"],
                item["title"],
                item["publication_date"],
                item["price"],
                item["location"],
                item["description"],
                item["complete_description"],
                item["features_list"]
            ))
        
        ## Execute insert of data into database
        self.conn.commit()
        return item

    def close_spider(self, spider):

        ## Close cursor & connection to database
        self.cur.close()
        self.conn.close()
