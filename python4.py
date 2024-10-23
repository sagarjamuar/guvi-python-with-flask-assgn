import pickle
import os

def save_preferences(filename, preferences):
    with open(filename, 'wb') as file:
        pickle.dump(preferences, file)

def load_preferences(filename):
    if not os.path.isfile(filename):
        return None
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except:
        return None

preferences = {'theme': 'dark', 'language': 'English', 'notifications': True}
filename = 'user_preferences.pkl'

save_preferences(filename, preferences)
loaded_preferences = load_preferences(filename)

if loaded_preferences:
    print("Loaded Preferences:", loaded_preferences)
else:
    print("Preferences file is missing or corrupted.")
