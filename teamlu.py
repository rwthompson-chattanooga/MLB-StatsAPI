import statsapi

teams = statsapi.get('teams', params={'sportId': 1})['teams']
""" for team in teams:
    print(f"## Team: `{team['name']}`")
    print(f"### ID: `{team['id']}`") """

atlsched = statsapi.schedule(date="2026-05-19", team=144)
print(atlsched)