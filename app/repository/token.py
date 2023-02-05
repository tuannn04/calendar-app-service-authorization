from connection.mongodb import ConnectionPool

class TokenRepository:
    connectionPool = None
    databaseName = "authorization"
    collectionName = "token"

    def __init__(self):
        self.connectionPool = ConnectionPool

    def getCollection(self):
        connection = self.connectionPool.getConnection(self.databaseName)
        db = connection[self.databaseName]
        collection = db[self.collectionName]
        return collection

    def getByAccessToken(self, accessToken):
        collection = self.getCollection()
        query = {"access_token": accessToken}
        result = collection.find_one(query)
        if result is not None and "_id" in result:
            del result['_id']
        return result

