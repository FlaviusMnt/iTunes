from dataclasses import dataclass

@dataclass
class Album:
    AlbumId:int
    Title:str
    ArtistId:int
    durataTotale: float

    def __hash__(self):
        return hash(self.AlbumId)

    def __str__(self):
        return f"CODICE_ALBUM->{self.AlbumId:^5}   NOME->{self.Title:^95}  DURATA TOTALE->{self.durataTotale}"

    def __eq__(self, other):
        return self.AlbumId == other.AlbumId
