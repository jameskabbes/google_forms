import kabbes_google_forms

class Question( kabbes_google_forms.Base ):

    _ONE_LINE_ATTS = ['Item','id']

    ITEM_KEY = 'questionItem'
    QUESTION_KEY = 'question'

    ATTRIBUTE_KEYS = {
        "questionId": "id"
    }

    def __init__( self, Item, dict ):
        self.Item = Item
        kabbes_google_forms.Base.__init__( self, dict )

    @staticmethod
    def check_item_for_question( Item ):
        return Question.ITEM_KEY in Item.dict

    @staticmethod
    def get_question_from_item( Item ):
        return Question( Item, Item.dict[ Question.ITEM_KEY ][ Question.QUESTION_KEY ] )


