from parent_class import ParentPluralDict
import kabbes_google_forms

class Items( ParentPluralDict ):

    ID_KEY = 'items'

    def __init__( self, Form ):
        ParentPluralDict.__init__( self, att='Items' )
        self.Form = Form

    def load_items( self ):

        for item_dict in self.Form.dict[ self.ID_KEY ]:
            new_Item = kabbes_google_forms.Item( self, item_dict )
            self._add( new_Item.id, new_Item )

