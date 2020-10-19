import json


class CountryWiki:
    def __init__(self):
        self.data_index = 0
        self.data = []
        self.countries_dict = {}

    def __next__(self):
        if self.data_index == len(self.data):
            raise StopIteration
        item = self.data[self.data_index]
        country = item['name']['common']
        self.data_index += 1
        self.countries_dict[country] = 'en.wikipedia.org/wiki/' + country

    def __iter__(self):
        return self

    def open_file(self):
        with open('files/countries.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.data = data

    def write_country_wiki(self):
        with open('files/wiki.json', 'w', encoding='utf-8') as f:
            json.dump(self.countries_dict, f, ensure_ascii=False, indent=2)


def main():
    country = CountryWiki()
    country.open_file()
    for item in country:
        pass
    country.write_country_wiki()


if __name__ == '__main__':
    main()