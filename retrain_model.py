import pickle

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.tree import DecisionTreeClassifier


def main() -> None:
    data = pd.read_csv("Crop_recommendation.csv")

    x = data[["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]]
    y = data["label"]

    x_train, _, y_train, _ = train_test_split(
        x, y, test_size=0.2, random_state=42, stratify=y
    )

    minmax_scaler = MinMaxScaler()
    standard_scaler = StandardScaler()

    x_train_minmax = minmax_scaler.fit_transform(x_train)
    x_train_scaled = standard_scaler.fit_transform(x_train_minmax)

    model = DecisionTreeClassifier(random_state=42)
    model.fit(x_train_scaled, y_train)

    with open("model.pkl", "wb") as model_file:
        pickle.dump(model, model_file)

    with open("standscaler.pkl", "wb") as standard_scaler_file:
        pickle.dump(standard_scaler, standard_scaler_file)

    with open("minmaxscaler.pkl", "wb") as minmax_scaler_file:
        pickle.dump(minmax_scaler, minmax_scaler_file)

    print("Saved model.pkl, standscaler.pkl, minmaxscaler.pkl")


if __name__ == "__main__":
    main()
