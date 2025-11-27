class Fone:
    def __init__(self, id: str, number: str):
        self.id = id
        self.number = number
    
    def isValid(self) -> bool:
        valido = "0123456789()-."
        for i in self.number:
            if i not in valido:
                return False
        return True

    def getId(self) -> str:
        return self.id
    def getNumber(self) -> str:
        return self.number
    
    def __str__(self) -> str:
        return f"{self.id}:{self.number}"
    
class Contact:
    def __init__(self, name: str):
        self.name = name
        self.favorited = False
        self.fones: list[Fone] =[] 

    def addFone(self, id: str, number: str) -> None:
        fone = Fone(id, number)
        if fone.isValid():
            self.fones.append(fone)
        else:
            print("fail: invalid number")

    def rmFone(self, index: int) -> None:
        if 0 <= index < len(self.fones):
            self.fones.pop(index)
        else:
            print("fail: indice invalido")
    
    def toogleFavorited(self) -> None:
        self.favorited = not self.favorited
    
    def isFavorited(self) -> bool:
        return True
    
    def getFones(self) -> list:
        return self.fones
    def getName(self) -> str:
        return self.name
    def setName(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        fav = "@" if self.favorited else "-"
        fones_str = ", ".join(str(f) for f in self.fones)
        return f"{fav} {self.name} [{fones_str}]"
    
def main():
    contact: Contact | None = None
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            contact = Contact(args[1])
        elif args[0] == "show":
            print(contact)
        elif args[0] == "add":
            contact.addFone(args[1], args[2])
        elif args[0] == "rm":
            contact.rmFone(int(args[1]))
        elif args[0] == "tfav":
            contact.toogleFavorited()

main()