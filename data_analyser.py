import user_def
import requests
import pandas as pd
import os

api_key = os.environ["api_key"]
sheety_endpoint = f"https://api.sheety.co/{api_key}/dopeStudy/sheet1"


class Data(user_def.UserDef):
    def __init__(self, user_name):
        super().__init__(user_name)

    def getdata(self):
        """retreives the user data from the database"""

        get = requests.get(url=sheety_endpoint)
        self.data = get.json()["sheet1"]
        print(self.data)
        # name = self.data["sheet1"][0]["name"]
        # total_study_time = self.data["sheet1"][0]["totalStudyHours"]
        # todo_topics = self.data["sheet1"][0]['todoTopics']
        # todo_topics = len(dict["todo_topics"])

    def useful_json(self):
        id = [n["day"] for n in self.data]
        # name = [n["name"] for n in self.data]
        todo_topics = [n["todoTopics"] for n in self.data]
        total_study_time = [n["totalStudyTime"] for n in self.data]

        return pd.DataFrame({
            "day": id,
            # "name": name,
            "todo_topics": todo_topics,
            "total_study_time": total_study_time
        })

    def make_graph(self):
        self.pie_data = self.useful_json()
        print(self.pie_data)

        import matplotlib.pyplot as plt

        plt.bar(self.pie_data["day"], self.pie_data["total_study_time"])

        plt.xlabel('DAY')
        plt.ylabel('TotalStudyTime')
        plt.show()

    def data_analyser(self):
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LinearRegression
        from sklearn.metrics import mean_squared_error

        lr_data = self.useful_json()
        X = lr_data[["day", "todo_topics"]]
        y = lr_data['total_study_time']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(X_train, y_train)

        predictor = model.predict(X_test)
        mse = mean_squared_error(y_test, predictor)

        print(predictor)
        print(mse)


pie = Data("x")
pie.getdata()
pie.data_analyser()
pie.make_graph()

# pie.useful_json()
