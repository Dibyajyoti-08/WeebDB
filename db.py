import pymongo

class WeebDB:
    def __init__(self, db_name="WeebDB", collection_name="WeebCollection"):
        """Initialize MongoDB connection and set the database and collection"""
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_anime(self, anime_name, release_date, ott_platform):
        """Insert anime details into database"""
        data = {
            "Anime Name": anime_name,
            "Release Date": release_date,
            "OTT_platform": ott_platform
        }
        self.collection.insert_one(data)
    
    def get_all_anime(self):
        """Retrieve all anime data"""
        return list(self.collection.find({}, {"_id": 0}))