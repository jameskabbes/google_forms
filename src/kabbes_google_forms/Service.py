from parent_class import ParentClass
from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools
import kabbes_google_forms

class Service( ParentClass ):

    def __init__( self ):
        ParentClass.__init__( self )

    def __init__( self ):

        store = file.Storage( self.cfg['token.Path'].path)

        self.creds = None
        if not self.creds or self.creds.invalid:
            flow = client.flow_from_clientsecrets( self.cfg['client_secrets.Path'].path, self.cfg['SCOPES'])
            self.creds = tools.run_flow(flow, store)

        self.service = discovery.build('forms', 'v1', http=self.creds.authorize(
            Http()), discoveryServiceUrl=self.cfg['DISCOVERY_DOC'], static_discovery=False)

        self.Forms = kabbes_google_forms.Forms( self )


