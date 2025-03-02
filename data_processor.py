import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_process_data(file_path):
    """
    Membaca dan memproses data dari file CSV.
    
    Parameter:
    - file_path (str): Lokasi file CSV.
    
    Return:
    - df (DataFrame): DataFrame asli.
    - X_scaled (ndarray): Matriks fitur yang sudah diproses dan diskalakan.
    """
    # Membaca file CSV dan memparsing kolom date
    df = pd.read_csv(file_path, parse_dates=['date'])
    
    # Mengekstraksi fitur dari kolom date
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['day_of_week'] = df['date'].dt.dayofweek
    
    # Frequency encoding untuk kolom kategorikal
    for col in ['description', 'account']:
        freq = df[col].value_counts(normalize=True)
        df[col + '_freq'] = df[col].map(freq)
    
    # Memilih fitur untuk model
    features = ['amount', 'year', 'month', 'day', 'day_of_week', 'description_freq', 'account_freq']
    X = df[features].values
    
    # Menskalakan fitur
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return df, X_scaled