

class MyBaseClass:
    '''An example of a base class'''
    MY_CONSTANT = 5
    def __init__(self,df):
        self.df = df

class MyDerivedClass(MyBaseClass):
    '''An example of a derived class'''
    def __init__(self):
        super().__init__(df=None)

    def train_val_test(self,df):
        '''This function takes a dataframe and splits it into train/test/validate'''
        df_train = df.iloc[0:int(len(df) * 0.6),:]
        df_val = df.iloc[int(len(df) * 0.6):int(len(df) * 0.8),:]
        df_test = df.iloc[int(len(df) * 0.8):,:]

        return (df_train,df_val,df_test)

    def report_nulls(self,df):
        '''
        This function checks a dataframe for nulls, returning True
        If nulls are found along with the columns with nulls
        '''
        return (df.isnull().sum() > 0, df.isnull().sum())
