from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.logging._init_ import logger



class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_transfrormation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transfrormation_config)
        data_transformation.convert()