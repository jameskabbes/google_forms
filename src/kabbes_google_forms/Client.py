import kabbes_client
import kabbes_google_forms

class Client( kabbes_google_forms.Service ):

    _BASE_DICT = {}

    def __init__( self, dict={} ):

        d = {}
        d.update( Client._BASE_DICT )
        d.update( dict )

        self.Package = kabbes_client.Package( kabbes_google_forms._Dir, dict=d )
        self.cfg = self.Package.cfg

        kabbes_google_forms.Service.__init__( self )
