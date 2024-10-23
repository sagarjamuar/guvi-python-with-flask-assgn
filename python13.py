import pickle
import os

def save_tasks(filename, tasks):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(tasks, file)
    except Exception as e:
        print("Error saving tasks:", e)

def load_tasks(filename):
    if not os.path.isfile(filename):
        return []
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except Exception:
        print("Error loading tasks. The file may be corrupted.")
        return []

filename = 'tasks.pkl'
tasks = ['Buy groceries', 'Complete project report', 'Call plumber']

save_tasks(filename, tasks)
loaded_tasks = load_tasks(filename)

print("Loaded Tasks:", loaded_tasks)
