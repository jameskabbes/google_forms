from parent_class import ParentPluralDict
import kabbes_google_forms

class Answers( ParentPluralDict ):

    ID_KEY = "answers"

    def __init__( self, Response ):
        self.Response = Response
        ParentPluralDict.__init__( self, att='Answers' )
        self.load_answers()

    def load_answers( self ):

        for question_id in self.Response.dict[ self.ID_KEY ]:

            answer_dict = self.Response.dict[self.ID_KEY][question_id]
            new_Answer = kabbes_google_forms.Answer( self, answer_dict )
            self._add( new_Answer.id, new_Answer )
