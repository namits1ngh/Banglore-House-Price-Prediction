import json
import pickle
import numpy as np

# Global variables
__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, total_sqft, bhk, bath):
    """
    Predict house price based on location, area, BHK, and bathrooms.
    """

    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))

    x[0] = total_sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __locations


def load_saved_artifacts():
    print("Loading saved artifacts...")

    global __data_columns
    global __locations

    with open("columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]

    global __model

    with open("banglore_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)

    print("Artifacts loaded successfully.")


if __name__ == "__main__":
    load_saved_artifacts()

    print(get_location_names()[:10])

    print(
        get_estimated_price(
            "1st phase jp nagar",
            1000,
            2,
            2
        )
    )

    print(
        get_estimated_price(
            "indira nagar",
            1000,
            2,
            2
        )
    )