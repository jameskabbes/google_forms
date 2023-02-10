import kabbes_google_forms

class Response( kabbes_google_forms.Base ):

    _ONE_LINE_ATTS = ['id']

    _DT_COL = 'createTime'
    _DT_FORMAT = '%Y-%m-%dT%H:%M:%S.%f%z'
    #2023-01-27T21:17:51.967Z
    _EMAIL_COL = 'respondentEmail'

    ATTRIBUTE_KEYS = {
        "responseId": "id"
    }

    def __init__( self, Responses, dict ):
        self.Responses = Responses
        kabbes_google_forms.Base.__init__( self, dict )

        self.Answers = kabbes_google_forms.Answers( self )

