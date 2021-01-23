logger_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'std_format': {
            'format': '{asctime}:: {levelname}:: {name}:: {message} ::'
                      'Module: {module} - Function: {funcName}',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'style': '{'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'std_format'
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'std_format',
            'filename': 'records.log',
            'mode': 'a',
        }
    },
    'loggers': {
        'page_loader': {
            'level': 'DEBUG',
            'handlers': ['console']
        },
    },
}