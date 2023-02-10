from parent_class import ParentClass

class Base( ParentClass ):

    ATTRIBUTE_KEYS = {
    }

    def __init__( self, dict ):
        ParentClass.__init__( self )

        self.dict = dict
        self._load()

    def _load( self ):
        for key in self.ATTRIBUTE_KEYS:
            self.set_attr( self.ATTRIBUTE_KEYS[key], self.dict[key] )

