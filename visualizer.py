import plotly.express as px

def plot_time_series(df, fraud_indices):
    """
    Membuat scatter plot waktu vs. jumlah transaksi, menyoroti transaksi kecurangan.
    
    Parameter:
    - df (DataFrame): DataFrame asli.
    - fraud_indices (list): Indeks transaksi kecurangan.
    
    Return:
    - fig: Objek Plotly untuk scatter plot.
    """
    df = df.copy()
    df['is_fraud'] = False
    df.loc[fraud_indices, 'is_fraud'] = True
    fig = px.scatter(df, x='date', y='amount', color='is_fraud',
                     title='Transaction Amounts Over Time',
                     labels={'is_fraud': 'Fraudulent'},
                     color_discrete_map={True: 'red', False: 'blue'})
    return fig

def plot_amount_histogram(df, fraud_indices):
    """
    Membuat histogram distribusi jumlah transaksi, menyoroti transaksi kecurangan.
    
    Parameter:
    - df (DataFrame): DataFrame asli.
    - fraud_indices (list): Indeks transaksi kecurangan.
    
    Return:
    - fig: Objek Plotly untuk histogram.
    """
    df = df.copy()
    df['is_fraud'] = False
    df.loc[fraud_indices, 'is_fraud'] = True
    fig = px.histogram(df, x='amount', color='is_fraud',
                       title='Distribution of Transaction Amounts',
                       labels={'is_fraud': 'Fraudulent'},
                       color_discrete_map={True: 'red', False: 'blue'})
    return fig

def plot_description_bar(df, fraud_indices):
    """
    Membuat bar chart transaksi kecurangan berdasarkan deskripsi.
    
    Parameter:
    - df (DataFrame): DataFrame asli.
    - fraud_indices (list): Indeks transaksi kecurangan.
    
    Return:
    - fig: Objek Plotly untuk bar chart.
    """
    df_fraud = df.loc[fraud_indices]
    fig = px.bar(df_fraud, x='description', title='Fraudulent Transactions by Description')
    return fig