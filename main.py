import json
from items.league import League


if __name__ == "__main__":
    league_id = 87

    league = League(league_id)

    with open('results/resultados.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(league.to_json(), indent=4))
