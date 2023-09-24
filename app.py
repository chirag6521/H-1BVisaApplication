import os
import sys
import logging
from src.visaproject.exception import CustomException
from src.visaproject.components.data_ingestion import DataIngestion, DataIngestionConfig

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        # Define the data ingestion configuration
        ingestion_config = DataIngestionConfig()

        # Create an instance of DataIngestion and initiate data ingestion
        data_ingestion = DataIngestion(ingestion_config)
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        # Uncomment and add code for data transformation and model training here
        # data_transformation_config = DataTransformationConfig()
        # data_transformation = DataTransformation()
        # train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)

        # Model Training
        # model_trainer = ModelTrainer()
        # print(model_trainer.initiate_model_trainer(train_arr, test_arr))

    except Exception as e:
        logging.error(f"An exception occurred: {str(e)}")
        raise CustomException(e, sys)
