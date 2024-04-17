# Simple Job recommendation system

The project is split into 2 parts:
Backend - Flask server that serves 3 endpoins
Frontend - index.html and scripts.js that fetches and communicates with server

### The knowledge base has been web scraped from "hipo.ro"

Before feeding data to sklearn.DecisionTreeClassifier it has been lightly preprocessed, translated, and split 

### To use this Expert System you need to:

1. Download Python dependencies (bs4, joblib, sklearn, pandas, flask)
Note: if you want to run the server you will only need joblib and flask
2. Run the server.py file using your Python@3 environmnet
3. Access index.html from web directory