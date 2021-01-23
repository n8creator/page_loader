import logging.config
from page_loader.settings.logger_config import logger_config


# Configure logging
logging.config.dictConfig(logger_config)

# Create Logger object
logger = logging.getLogger('page_loader')
