class Fone:
    def __init__(self, id: str, number: str):
        self.id: str
        self.number: str
    
    def getId(self) -> str:
        return self.id
    def getNumber(self) -> str:
        return self.number
    
    def __str__(self) -> str:
        return f"{self.id}:{self.number}"
    
class Contact:
    def __init__(self, name: str):
        self.name: str
        self.favorited: bool
        self.fones: list[Fone] =[] 

    def addFone(id: str, number: str) -> None:
        self.fones.append(Fone(id, number))


    def getName(self) -> str:
        return self.name
    

    def __str__(self) -> str:
        return f""