from parent_class import ParentPluralDict
import kabbes_google_forms
import pandas as pd
import datetime

class Responses( ParentPluralDict ):

    def __init__( self, Form ):
        self.Form = Form
        ParentPluralDict.__init__( self, att='Responses' )

    def load_responses( self ):

        # gets the responses of your specified form:
        responses = self.Form.Forms.Service.service.forms().responses().list(formId=self.Form.id).execute()

        for response_dict in responses['responses']:
            new_Reponse = kabbes_google_forms.Response( self, response_dict )
            self._add( new_Reponse.id, new_Reponse )

    def get_df( self, include_email=True, include_dt=True ):

        df = pd.DataFrame()

        if include_dt:
            dts = []
            for Response in self:
                dt = Response.dict[ Response._DT_COL ]
                dts.append( datetime.datetime.strptime( dt, Response._DT_FORMAT ) )
            df[ 'datetime' ] = dts

        if include_email:
            emails = []
            for Response in self:
                emails.append( Response.dict[ Response._EMAIL_COL ] )
            df[ Response._EMAIL_COL ] = emails

        for Question in self.Form.Questions:
            question_id = Question.id
            answers = []

            for Response in self:
                Answer = Response.Answers.Answers[ question_id ]
                answers.append( Answer.value )

            df[Question.Item.title] = answers


        if include_dt:
            df.sort_values( by='datetime', ascending=False, inplace=True )

        return df
            
