import random
import pandas as pd

#Load winners from CSV files into pandas DataFrames
league_winners_df = pd.read_csv(r"C:\Users\hbuzzacott001\OneDrive - PwC\Uni work\YR2\DAT5501_Portfolio\personal projects\league winners.csv")
champions_league_winners_df = pd.read_csv(r"C:\Users\hbuzzacott001\OneDrive - PwC\Uni work\YR2\DAT5501_Portfolio\personal projects\champions league winners.csv")
world_cup_winners_df = pd.read_csv(r"C:\Users\hbuzzacott001\OneDrive - PwC\Uni work\YR2\DAT5501_Portfolio\personal projects\world cup winners.csv")
euros_winners_df = pd.read_csv(r"C:\Users\hbuzzacott001\OneDrive - PwC\Uni work\YR2\DAT5501_Portfolio\personal projects\euros winners.csv")

#Convert DataFrames into dictionaries for easy lookup
league_winners = dict(zip(league_winners_df["Year"], league_winners_df["Winning Team"]))
champions_league_winners = dict(zip(champions_league_winners_df["Year"], champions_league_winners_df["Winning Team"]))
world_cup_winners = dict(zip(world_cup_winners_df["Year"], world_cup_winners_df["Winning Team"]))
euros_winners = dict(zip(euros_winners_df["Year"], euros_winners_df["Winning Team"]))

#find which competitionsactually occured in a given year
def get_possible_competitions(year):
    competitions = []
    if year >= 1930 and ((year+2) % 4 == 0) and year not in [1942, 1946]:
        competitions.append("World Cup")
    if year >= 1956:
        competitions.append("Champions League")
    if year >= 1960 and (year % 4 == 0):
        competitions.append("Euros")
    if year >= 1889 and year not in [
        1916, 1917, 1918, 1919, 1940, 1941, 1942, 1943, 1944, 1945, 1946
    ]:
        competitions.append("League")
    return competitions

#find the winner of a given competition in a given year
def get_winner(year, competition):
    if competition == "League":
        return league_winners.get(year, "Unknown")
    elif competition == "Champions League":
        return champions_league_winners.get(year, "Unknown")
    elif competition == "World Cup":
        return world_cup_winners.get(year, "Unknown")
    elif competition == "Euros":
        return euros_winners.get(year, "Unknown")
    return "Unknown"

#Quiz user on winnor of a randomly generated competion in a randomly generated year
def main():
    year = random.randint(1889, 2025)
    possible_competitions = get_possible_competitions(year)
    if not possible_competitions:
        return  # Skip years with no possible competitions

    competition = random.choice(possible_competitions)

    print(f"Year: {year}, Competition: {competition}")
    user_input = input("Who won? ")

    correct_winner = get_winner(year, competition)
    if user_input.strip().lower() == correct_winner.strip().lower():
        print("Correct!")
    else:
        print(f"Wrong! The winner was {correct_winner}.")

if __name__ == "__main__":
    for i in range(10):
        main()