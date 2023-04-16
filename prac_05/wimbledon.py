import csv

def read_data(wimbledon):
    champions = []
    countries = set()
    with open(wimbledon, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for row in reader:
            name, country, wins = row
            champions.append([name, int(wins)])
            countries.add(country)
    return champions, countries

def get_champions_info(champions):
    champions_dict = {}
    for champion in champions:
        name, wins = champion
        if name not in champions_dict:
            champions_dict[name] = 0
        champions_dict[name] += wins
    return champions_dict

def main():
    champions, countries = read_data("wimbledon.csv")
    champions_info = get_champions_info(champions)
    print("Wimbledon Champions:")
    for name, wins in sorted(champions_info.items()):
        print(f"{name} {wins}")
    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

if __name__ == "__main__":
    main()
