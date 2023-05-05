from gathering_date import question_date,question_kilom
from requests import put, delete
class ManagingData:
    def __init__(self, USER_NAME, USER_TOKEN, GRAPH_ID):
        self.user_id = USER_NAME
        self.graph_id = GRAPH_ID
        self.user_token = USER_TOKEN

    def updating_graph(self):

        header = {'X-USER-TOKEN': self.user_token}
        date = question_date()
        amount = question_kilom()
        endpoint = f'https://pixe.la/v1/users/{self.user_id}/graphs/{self.graph_id}/{date}'
        parameters = {'quantity': amount}
        response = put(url=endpoint, headers=header, json=parameters)
        print(response.text)

    def delete_graph(self):
        date = question_date()
        endpoint = f'https://pixe.la/v1/users/{self.user_id}/graphs/{self.graph_id}/{date}'
        header = {"X-USER-TOKEN": self.user_token}
        response = delete(url=endpoint, headers=header)
        print(response.text)
