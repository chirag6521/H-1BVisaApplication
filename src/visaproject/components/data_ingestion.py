import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.visaproject.exception import CustomException
from dataclasses import dataclass



@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'Visadataset.csv')

class DataIngestion:
    def __init__(self, config: DataIngestionConfig) -> None:
        self.config = config

    def initiate_data_ingestion(self):
        try:
            # Load the raw data from the 'artifacts' folder
            Visadataset_data_path = self.config.raw_data_path
            df = pd.read_csv(Visadataset_data_path)

            # Perform train-test split
            train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

            # Save train and test data to CSV files
            train_df.to_csv(self.config.train_data_path, index=False)
            test_df.to_csv(self.config.test_data_path, index=False)

            return self.config.train_data_path, self.config.test_data_path

        except Exception as e:
            raise CustomException(e,sys)
