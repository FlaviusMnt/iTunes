from mysql.connector import cursor
#from pathlib.uri_validate import query

from database.DB_connect import DBConnect
from model.album import Album

class DAO():
    def __init__(self):
        pass

    # @staticmethod
    # def getAllAlbums():
    #     cnx = DBConnect.get_connection()
    #     risultato = []
    #     if cnx is not None:
    #         cursor = cnx.cursor(dictionary=True)
    #         query = """SELECT * FROM ALBUM a"""
    #
    #         cursor.execute(query)
    #
    #         for row in cursor:
    #             risultato.append(Album(**row))
    #
    #         cursor.close()
    #         cnx.close()
    #         return risultato
    #     else:
    #         print("ERRORE NELLA CONNESSIONE")
    #         return None

    @staticmethod
    def getAllNodes(durataMin):
        cnx = DBConnect.get_connection()
        risultato = []
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = """select a.AlbumId ,a.Title ,a.ArtistId , sum(t.Milliseconds)/1000/60 as durataTotale
                        from album a ,track t 
                        where a.AlbumId = t.AlbumId
                        group by a.AlbumId 
                        having durataTotale  > %s"""

            cursor.execute(query,(durataMin,))

            for row in cursor:
                risultato.append(Album(**row))

            cursor.close()
            cnx.close()
            return risultato
        else:
            print("ERRORE NELLA CONNESSIONE")
            return None

    @staticmethod
    def getAllEdges(mappaNodiId):
        cnx = DBConnect.get_connection()
        risultato = []
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT t1.AlbumId as a1, t2.AlbumId as a2 
                    FROM track t1, track t2, playlisttrack p1, playlisttrack p2
                    WHERE t2.TrackId = p2.TrackId 
                    and t1.TrackId = p1.TrackId
                    and p2.PlaylistId = p1.PlaylistId
                    and t1.AlbumId < t2.AlbumId """

            cursor.execute(query)

            for row in cursor:
                if row["a1"] in mappaNodiId and row["a2"] in mappaNodiId:
                    risultato.append( (mappaNodiId[row["a1"]],mappaNodiId[row["a2"]]) )

            cursor.close()
            cnx.close()
            return risultato
        else:
            print("ERRORE NELLA CONNESSIONE")
            return None




if __name__ == "__main__":
    # for album in DAO.getAllAlbums():
    #     print(album)

    for nodo in DAO.getAllNodes(1000):
        print(nodo)




