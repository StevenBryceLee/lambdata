def train_val_test(df):
    '''
    This function takes a dataframe and splits it into train/test/validate
    '''
    df_train = df.iloc[0:int(len(df) * 0.6),:]
    df_val = df.iloc[int(len(df) * 0.6):int(len(df) * 0.8),:]
    df_test = df.iloc[int(len(df) * 0.8):,:]

    return (df_train,df_val,df_test)

def reportNulls(df):
    '''
    This function checks a dataframe for nulls, returning True
    if nulls are found along with the columns with nulls
    '''
    return (df_test.isnull().sum() > 0, df_test.isnull().sum())