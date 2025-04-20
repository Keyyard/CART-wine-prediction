import pandas as pd
import config 
class DataLoader:
    DATA = config.DATA_PATH
    @staticmethod
    def load_data():
        data = pd.read_csv(DataLoader.DATA, sep=';', header=0)
        data.columns = data.columns.str.strip()
        return data
