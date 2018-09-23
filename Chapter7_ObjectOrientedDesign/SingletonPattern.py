class Singleton:
    __instance = None
    @staticmethod 
    def get_instance():        
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __new__(self, *args, **kwargs):                
        if not self.__instance:
            self.__instance = super().__new__(self, *args, **kwargs)
        return self.__instance


if __name__ == "__main__":
    s = Singleton()
    print(s)    
    q = Singleton.get_instance()
    print(q)
    p = Singleton()
    print(p)
