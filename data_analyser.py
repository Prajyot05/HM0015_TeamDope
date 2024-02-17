import user_def
import requests
import pandas as pd

sheety_endpoint = "https://api.sheety.co/d052d61d7647c0b06fbfc305f5f515e1/sponsorshipsMails/balsaWood"

class Data(user_def.UserDef):
    def __init__(self, user_name):
        super().__init__(user_name)

    def getdata(self):
        """retreives the user data from the database"""

        get = requests.get(url=sheety_endpoint)
        self.data = get.json()
        print(self.data)
        # name = self.data["sheet1"][0]["name"]
        # total_study_time = self.data["sheet1"][0]["totalStudyHours"]
        # todo_topics = self.data["sheet1"][0]['todoTopics']
        # todo_topics = len(dict["todo_topics"])

    def make_graph(self):
        pie_data = pd.read_json(self.data)
        pd.DataFrame(pie_data)
        import seaborn



    def data_analyser(self):
        pass
        # import numpy as np
        # from sklearn.model_selection import train_test_split
        # from sklearn.linear_model import LinearRegression
        # from sklearn.metrics import mean_squared_error


pie = Data("x")
pie.getdata()
