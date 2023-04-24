from requests import post


def generating_user(username, token):
    # Only used once to create new user.
    endpoint = 'https://pixe.la/v1/users'

    data = {
        'token': token,
        'username': username,
        'agreeTermsOfService': "yes",
        'notMinor': 'yes'
    }
    response = post(url=endpoint, json=data)
    print(response.text)

    # {"message":"Success. Let's visit https://pixe.la/@viviane69 , it is your profile page!","isSuccess":true}


def generating_new_graph(username, token, graph_name, graph_id):
    # Only used once to create new graph.
    endpoint = f'https://pixe.la/v1/users/{username}/graphs'

    headers = {"X-USER-TOKEN": token}

    parameters = {'id': graph_id,
                  'name': graph_name,
                  'unit': 'kilometers',
                  'type': 'int',
                  'color': 'sora'
                  }

    response = post(url=endpoint,
                    headers=headers,
                    json=parameters)
    print(response.text)


# {"message":"Success.","isSuccess":true}
# https://pixe.la/v1/users/viviane69/graphs/cyclingcycle69.html


def generating_a_pixel(username, token, graph_id, date, quantity):
    # Used to add date to the graph.
    endpoint = f'https://pixe.la//v1/users/{username}/graphs/{graph_id}'
    headers = {"X-USER-TOKEN": token}
    parameters = {'date': date,
                  'quantity': quantity
                  }
    response = post(url=endpoint,
                    headers=headers,
                    json=parameters)
    print(response.text)


