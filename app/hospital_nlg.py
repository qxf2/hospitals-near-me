"""
The Natural Language Generator for hospital data. The generator will:
a) Determine an opening line about the data
b) Follow up by verbalizing some choices
c) If there are more than 2 choices, it will also show tabular data
d) If your highest rated option is no the closest, it will mention that fact
e) Make a lexical choice (Highest, high, etc.) regarding the overall score
"""

class Hospital_NLG:
    "Class for generating natural language about hospitals"

    def __init__(self, hospital_data):
        "Initialize the class with a DataFrame about available hospitals"
        self.set_data(hospital_data)
        self.opening = '' # Human friendly first line
        self.hospital_choices = ''  # Top choices of hospitals
        self.aggregation = ''  # Tabular data
        self.lexical_mapping = {'5 overall rating': 'the highest overall rating', '4 overall rating': 'a high overall rating', '3 overall rating': 'a medium overall rating',
                                '2 overall rating': 'a low overall rating', '1 overall rating': 'the lowest overall rating', 'has a 0 overall rating': 'does not have an available rating'}  # Verbalize overall score
        self.msg = ''

    def set_data(self,data):
        "Set the NLG class's data attribute"
        self.data = data.sort_values(
            ['Hospital overall rating', 'Distance'], ascending=[False, True])
        self.data['Hospital overall rating'].replace(
            'Not Available', 0, inplace=True)
        self.rows, self.columns = self.data.shape

    def get_summary(self):
        "Return a summary of the hospital choices"
        self.determine_opening()
        self.get_hospital_summary()
        self.get_aggregated_table()
        self.msg = self.opening + self.hospital_choices + self.aggregation

        return self.msg

    def get_lexical_replacements(self, msg):
        "Replace strings with human words"
        new_message = msg
        for key, value in self.lexical_mapping.iteritems():
            new_message = new_message.replace(key, value)

        return new_message

    def get_aggregated_table(self):
        "Put the dataframe into HTML table data format"
        if self.rows > 0:
            self.aggregation = '<br><br><h3>Tabular summary:</h3><br>'
            self.aggregation += self.data[['Hospital Name', 'Hospital overall rating', 'Distance',
                                          'Phone Number', 'Hospital Type', 'Emergency Services', 'Hospital Ownership']].to_html(index=False)

    def get_hospital_summary(self):
        "Return a verbal summary for the hospitals provided"
        top_n_hospitals = self.data.head(3)
        rows, cols = top_n_hospitals.shape
        msg = ''
        count = 1
        for index, row in top_n_hospitals.iterrows():
            #$NAME: ~$MILES miles away <and has a $OVERALL_RATING rating/but does not have an overall rating>. Their listed phone number is: $PHONE. This hospital <has/does not have> emergency services. <This is a government hospital>
            msg += '<br>%d. <b>%s</b> is <b>%.2f miles</b> away and has %d overall rating. Their listed phone number is %s.' % (
                count, str(row['Hospital Name']), float(row['Distance']), int(row['Hospital overall rating']), str(row['Phone Number']))
            count += 1
            msg += '<br>'
        self.hospital_choices = self.get_lexical_replacements(msg)

    def determine_opening(self):
        "Determine the opening lines of the message"
        if self.rows == 0:
            self.opening = 'There are no hospitals within a 20-mile radius of your zip code.'
        elif self.rows == 1:
            self.opening = 'You have only one hospital within 20-mile radius of your zip code.<br>'
        else:
            sorted_data_distance = self.data.sort_values('Distance')
            closest_hospital = sorted_data_distance.head(
                1)['Hospital Name'].values[0]
            highest_rated_hospital = self.data.head(1)[
                'Hospital Name'].values[0]
            if highest_rated_hospital == closest_hospital:
                self.opening = 'You have more than one option near you. Consider one of the following:<br>'
            else:
                self.opening = '%s is the best rated hospital near you ... and %s is the closest to you. Your options are:<br>' % (
                    self.data.head(1)['Hospital Name'].values[0], sorted_data_distance.head(1)['Hospital Name'].values[0])
