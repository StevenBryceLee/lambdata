class MyBaseClass:
    '''An example of a base class'''
    MY_CONSTANT = 5

    def __init__(self, df=None):
        self.df = df

    def __repr__(self):
        '''print none or the head of the df'''

        return str(type(self.df))


class MyDerivedClass(MyBaseClass):
    '''An example of a derived class'''
    def __init__(self):
        super().__init__(self, df=None)

    def train_val_test(self, df):
        '''
        This function takes a dataframe
        and splits it into train/test/validate
        '''
        df_train = df.iloc[0:int(len(df) * 0.6), :]
        df_val = df.iloc[int(len(df) * 0.6):int(len(df) * 0.8), :]
        df_test = df.iloc[int(len(df) * 0.8):, :]

        return (df_train, df_val, df_test)

    def report_nulls(self, df=None):
        '''
        This function checks a dataframe for nulls, returning True
        If nulls are found along with the columns with nulls
        '''
        return (df.isnull().sum() > 0, df.isnull().sum())


if __name__ == '__main__':
    # demo code
    import pandas as pd
    import numpy as np
    df1 = pd.DataFrame(np.arange(10))
    df2 = pd.DataFrame(np.arange(10, 20))
    base = MyBaseClass()
    derived = MyDerivedClass()
    print(f'current df type:')
    print(base)
    print(derived)
    base.df = df1
    derived.df = df2
    print('after setting df:')
    print(base)
    print(derived)
