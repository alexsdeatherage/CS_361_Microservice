import time

import requests
import random


def random_city():
    # Endpoint is the url that we will get a random city
    endpoint = 'https://countriesnow.space/api/v0.1/countries/capital'

    # Make a GET request to retrieve data from endpoint
    response = requests.get(endpoint)
    response.raise_for_status()
    # Will run following code if request was successful

    json = response.json()
    capitals_number = len(json['data'])
    capital_names = []

    for i in range(0, capitals_number - 1):
        capital_names.append(json['data'][i]['capital'])

    # Once we have all of the capital cities inside an array, we can pick one out at random, and write it into a text file

    # Note, with the api, some countries don't have capital cities, so we need to sort those out first
    while "" in capital_names:
        capital_names.remove("")

    random_city = random.choice(capital_names)
    return random_city


def main():
    print('Starting service')
    run = True
    while run:
        try:
            with open("randomCapital.txt") as file:
                lines = file.readlines()
                print(lines)
                file.close()
                if int(lines[0]) == 1:  # checks the txt file communication from UI
                    if lines[1] == 'quit':
                        print('Closing random city microservice')
                        with open("randomCapital.txt", "w") as file:
                            file.write("0\n")
                            file.write('waiting')
                            file.close()
                        run = False

                    else:
                        random_capital = random_city()
                        with open("randomCapital.txt", "w") as file:
                            file.write("0\n")
                            file.write(random_capital)
                            file.close()
                else:
                    file.close()
                    pass

        except:
            pass
    time.sleep(0.25)  # checks txt file every 0.25 seconds


if __name__ == "__main__":
    main()
