import requests


class SuperHeroes:
    def __init__(self, token: str, *list_heroes):
        self.heroes = list_heroes
        self.URL = 'https://superheroapi.com/api'
        self.API_TOKEN = token
        self.id_heroes = self._search_id_heroes()

    def _search_id_heroes(self):
        id_ = []
        for hero in self.heroes:
            response = requests.get(url=f'{self.URL}/{self.API_TOKEN}/search/{hero}')
            data = response.json()
            id_ += [hero_['id'] for hero_ in data['results'] if hero_['name'] == hero]
        id_heroes = dict(zip(self.heroes, id_))
        return id_heroes

    def most_intelligent(self):
        intelligent_list = []
        for id_hero in self.id_heroes.values():
            res = requests.get(url=f'{self.URL}/{self.API_TOKEN}/{id_hero}/powerstats/')
            data = res.json()
            intelligent_list.append(int(data['intelligence']))
        int_heroes = list(zip(self.heroes, intelligent_list))
        most_intelligent = sorted(int_heroes, key=lambda x: x[1], reverse=True)[0]
        print(f'{most_intelligent[0]} имеет наибольший интеллект ({most_intelligent[1]})')


if __name__ == '__main__':
    heroes = SuperHeroes('2619421814940190', 'Hulk', 'Captain America', 'Thanos')
    heroes.most_intelligent()
