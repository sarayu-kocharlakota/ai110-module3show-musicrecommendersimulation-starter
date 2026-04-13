"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = [
        {"name": "High-Energy Pop",    "genre": "pop",  "mood": "happy",   "energy": 0.9},
        {"name": "Chill Lofi",         "genre": "lofi", "mood": "chill",   "energy": 0.3},
        {"name": "Deep Intense Rock",  "genre": "rock", "mood": "intense", "energy": 0.95},
        {"name": "Conflicting (edgy)", "genre": "edm",  "mood": "sad",     "energy": 0.9},
    ]

    for profile in profiles:
        user_prefs = {k: v for k, v in profile.items() if k != "name"}
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n🎵 Profile: {profile['name']}")
        print("-" * 45)

        for i, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            print(f"{i}. {song['title']} by {song['artist']}")
            print(f"   Score: {score:.2f} | {explanation}")

        print()

if __name__ == "__main__":
    main()