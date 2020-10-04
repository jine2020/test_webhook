from public.public import Base
class Search(Base):
    def search(self,value):
        self._params = {}
        self._params["value"] = value
        self.steps('./element.yml')
        return self