from ppf.pipeline.stage01_data_ingestion import DataIngestionPipeline
from ppf.pipeline.stage02_data_validation import DataValidationPipeline
from ppf.pipeline.stage03_model_trainer import ModelTrainerPipeline
from ppf.pipeline.stage04_model_evaluation import ModelEvaluationPipeline
from ppf.logging import logger

import warnings
warnings.filterwarnings('ignore')


STAGE_NAME = 'data_ingestion_training'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} has started <<<<<')
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f'>>>>> stage {STAGE_NAME} has completed <<<<<')
except Exception as e:
    logger.error(f'>>>>> stage {STAGE_NAME} has failed <<<<<')
    raise e
logger.info('----------------------------------------------------------------')


STAGE_NAME = 'data_validation_training'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} has started <<<<<')
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f'>>>>> stage {STAGE_NAME} has completed <<<<<')
except Exception as e:
    logger.error(f'>>>>> stage {STAGE_NAME} has failed <<<<<')
    raise e
logger.info('----------------------------------------------------------------')


STAGE_NAME = 'model_training'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} has started <<<<<')
    model_training = ModelTrainerPipeline()
    model_training.main()
    logger.info(f'>>>>> stage {STAGE_NAME} has completed <<<<<')
except Exception as e:
    logger.error(f'>>>>> stage {STAGE_NAME} has failed <<<<<')
    raise e
logger.info('----------------------------------------------------------------')

STAGE_NAME = 'model_evaluation'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} has started <<<<<')
    model_training = ModelEvaluationPipeline()
    model_training.main()
    logger.info(f'>>>>> stage {STAGE_NAME} has completed <<<<<')
except Exception as e:
    logger.error(f'>>>>> stage {STAGE_NAME} has failed <<<<<')
    raise e
logger.info('----------------------------------------------------------------')