import kabbes_google_forms

class Form( kabbes_google_forms.Base ):

    _ONE_LINE_ATTS = ['id']

    ATTRIBUTE_KEYS = {
        "formId": "id"
    }

    def __init__( self, Forms, dict ):
        self.Forms = Forms
        kabbes_google_forms.Base.__init__( self, dict )

        self.Items = kabbes_google_forms.Items( self )
        self.Responses = kabbes_google_forms.Responses( self )
        self.Questions = kabbes_google_forms.Questions( self )
