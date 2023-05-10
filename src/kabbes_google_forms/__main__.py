import kabbes_google_forms
c = kabbes_google_forms.Client()

form = c.Forms.get_random()
form.Items.load_items()
form.Responses.load_responses()
print ( form.Responses.get_df( include_email=False ) )
