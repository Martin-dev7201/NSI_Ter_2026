class File :
    def __init__(self) :
        self.__f = []
        
    def __repr__(self):
        return str(self.__f)
    
    def enfiler(self, e) :
        self.__f.append(e)
        
        
    def defiler(self) :
        return self.__f.pop(0)
        
    
    def est_vide(self) :
        return len(self.__f)==0
