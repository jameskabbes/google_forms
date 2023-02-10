import kabbes_google_forms

class Answer( kabbes_google_forms.Base ):

    _ONE_LINE_ATTS = ['value']

    ATTRIBUTE_KEYS = {
        "questionId": "id"
    }

    def __init__( self, Answers, dict ):
        self.Answers = Answers
        kabbes_google_forms.Base.__init__( self, dict )
        self.load_value()

    def load_value( self ):
        self.value = self.dict[ 'textAnswers' ]['answers'][0]['value'] 




