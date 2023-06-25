
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
import time

start = time.time()
melbourne_file_path = 'melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
melbourne_data.columns

melbourne_data = melbourne_data.dropna(axis=0)
y = melbourne_data.Price

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

print(time.time()-start, "s of preperation")

"""start = time.time()
model = DecisionTreeRegressor(max_leaf_nodes=700, random_state=0)
model.fit(train_X, train_y)
preds_val = model.predict(val_X)
print(time.time()-start, "s for", mean_absolute_error(val_y, preds_val))"""

"""
Max_leaf_nodes upravuje, kolik dat to používá (under/over fitting) --> efektne převážně přesnost, prochu rychlost
n_estimators = dělá víckrát a půměruje --> mnohem přesnější, ale zabírá mnohem více času (n_est... = 5 --> 5x déle)
"""

for i in range(50):
    start = time.time()
    forest_model = RandomForestRegressor(random_state=1, max_leaf_nodes=700, n_estimators=i+1) 
    forest_model.fit(train_X, train_y)
    melb_preds = forest_model.predict(val_X)
    took = time.time()-start
    error = mean_absolute_error(val_y, melb_preds)
    print(f"{took} s for {error} with {i+1}")

"""print("\n-----")
start = time.time()
forest_model = RandomForestRegressor(random_state=1, n_estimators=5, max_leaf_nodes=300)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(time.time()-start, "s for", mean_absolute_error(val_y, melb_preds), f"with {i+1}")"""