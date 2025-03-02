from sklearn.ensemble import IsolationForest

def detect_fraud(X, contamination=0.01):
    """
    Mendeteksi kecurangan menggunakan Isolation Forest.
    
    Parameter:
    - X (ndarray): Matriks fitur yang sudah diproses.
    - contamination (float): Proporsi outliers dalam data (default: 0.01).
    
    Return:
    - fraud_indices (list): Daftar indeks transaksi yang terdeteksi sebagai kecurangan.
    """
    model = IsolationForest(contamination=contamination, random_state=42)
    model.fit(X)
    predictions = model.predict(X)
    # Predictions: 1 = normal, -1 = anomali
    fraud_indices = [i for i, p in enumerate(predictions) if p == -1]
    return fraud_indices