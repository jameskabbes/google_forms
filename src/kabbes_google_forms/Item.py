import kabbes_google_forms

class Item( kabbes_google_forms.Base ):

    _ONE_LINE_ATTS = ['title']

    ATTRIBUTE_KEYS = {
        "itemId": "id",
        "title": "title",
    }

    def __init__( self, Items, dict ):
        self.Items = Items
        kabbes_google_forms.Base.__init__( self, dict )

        self.has_Question = kabbes_google_forms.Question.check_item_for_question( self )
        if self.has_Question:
            self.load_Question()
        
    def load_Question( self ):
        new_Question = kabbes_google_forms.Question.get_question_from_item( self )
        self.Items.Form.Questions._add( new_Question.id, new_Question ) 



