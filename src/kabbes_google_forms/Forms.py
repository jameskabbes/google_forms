from parent_class import ParentPluralDict
import kabbes_google_forms

class Forms( ParentPluralDict ):

    def __init__( self, Service ):
        ParentPluralDict.__init__( self, att='Forms' )
        self.Service = Service
        self.load_forms()

    def load_forms( self ):

        for form in self.Service.cfg['forms']:
            form_id = form['id']
            form_dict = self.Service.service.forms().get( formId=form_id ).execute() 

            self._add( form_id, kabbes_google_forms.Form( self, form_dict ) )
