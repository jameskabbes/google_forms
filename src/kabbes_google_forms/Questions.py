from parent_class import ParentPluralDict
import kabbes_google_forms

class Questions( ParentPluralDict ):

    def __init__( self, Form ):
        self.Form = Form
        ParentPluralDict.__init__( self, att='Questions' )
