class Tool:
    def __init__(self, id:int, name: str, link: str, description: str, tag: str):
        self._id = id
        self._name = name
        self._link = link
        self._description = description
        self._tag = tag
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def link(self):
        return self._link
    
    @link.setter
    def link(self, value):
        self._link = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    
    @property
    def tag(self):
        return self._tag
    
    @tag.setter
    def tag(self, value):
        self._tag = value

    def toDict(self):
        return{
            "id": self._id,
            "name": self._name,
            "link": self._link,
            "description": self._description,
            "tag": self._tag
        }