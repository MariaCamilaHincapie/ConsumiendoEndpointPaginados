from time import sleep

import requests


class ClienteHttp():

    def __init__(self, url, retry=0, retry_codes=[]):
        self.url = url
        self.retry = retry
        self.retry_codes = retry_codes

    def get(self, payload={}, headers={}) -> dict:

        for i in range(self.retry + 1):

            titulo = str(input("Title:"))

            params = {
                'Title': titulo,
                'page': 1
            }

            response = requests.request("GET", self.url, headers=headers,
                                        data=payload, params=params)

            numPaginas = response.json().get('total_pages')


            if response.status_code == 200 \
                    or response.status_code not in self.retry_codes:

                peliculas = {}

                for pag in range(numPaginas):
                    params = {
                        'Title': titulo,
                        'page': pag + 1
                    }

                    response = requests.request("GET", self.url, headers=headers,
                                                data=payload, params=params)
                    peliculas.update(response.json())

                return peliculas
            sleep(0.00001 * (10 ** i))

    def peliculas_por_tiempo(self, peliculas):

            tiempo = {}

            for i in range(peliculas.get('total')):
                print("")

            print(peliculas)




if __name__ == '__main__':
    cliente = ClienteHttp('https://jsonmock.hackerrank.com/api/movies/search/', 50, [500, 503, 301])
    pelis = cliente.get()

    cliente.peliculas_por_tiempo(pelis)

