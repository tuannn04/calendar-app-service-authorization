from config.db import DbConfiguration
import pymongo

class ConnectionPool(object):
    @classmethod
    def getConnection(cls, databaseName):
        connectionName = 'connection_' + databaseName.lower()
        if not hasattr(cls, connectionName):
            setattr(cls, connectionName, cls.createConnection(databaseName))
        return getattr(cls, connectionName)

    @classmethod
    def createConnection(cls, databaseName):
        configuration = cls.getConnectionConfiguration(databaseName)
        print(configuration)
        params = [
            "mongodb://",
            configuration["username"],
            ":",
            configuration["password"],
            "@",
            configuration["host"],
            ":",
            configuration["port"],
            "/",
            configuration["database"]
        ]
        return pymongo.MongoClient("".join(params))

    @classmethod
    def getConnectionConfiguration(cls, databaseName):
        hostKey = getattr(DbConfiguration, databaseName.upper() + '_DB_HOST')
        portKey = getattr(DbConfiguration, databaseName.upper() + '_DB_PORT')
        databaseKey = getattr(DbConfiguration, databaseName.upper() + '_DB_DATABASE')
        usernameKey = getattr(DbConfiguration, databaseName.upper() + '_DB_USERNAME')
        passwordKey = getattr(DbConfiguration, databaseName.upper() + '_DB_PASSWORD')
        return {
            "host": hostKey,
            "port": portKey,
            "database": databaseKey,
            "username": usernameKey,
            "password": passwordKey
        }