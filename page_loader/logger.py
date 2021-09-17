import sys
import logging
import logging.config


class _ExcludeErrorsFilter(logging.Filter):
    def filter(self, record):
        """Filters log messages with log level ERROR (numeric value: 40)
           or higher."""
        return record.levelno < 40


logger_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'exclude_errors': {
            '()': _ExcludeErrorsFilter
        }
    },
    'formatters': {
        'std_format': {
            'format': '{asctime}:: {levelname}:: {name}:: {message} ::'
                      ' Module: {module} - Function: {funcName}',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'style': '{'
        }
    },
    'handlers': {
        'console_stdout': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'std_format',
            'filters': ['exclude_errors'],
            'stream': sys.stdout
        },
        'console_stderr': {
            'class': 'logging.StreamHandler',
            'level': 'ERROR',
            'formatter': 'std_format',
            'stream': sys.stderr
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'std_format',
            'filename': 'loging.log',
            'mode': 'w',
            'encoding': 'utf8'
        }
    },
    'loggers': {
        'page_loader': {
            'level': 'DEBUG',
            'handlers': ['file']
        },
    },
}


# Configure logging
logging.config.dictConfig(logger_config)

# Create Logger object
logger = logging.getLogger('page_loader')
