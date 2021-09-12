from octopus.logging.logging import LoguruHandler, logging_level_within

# Configuration
compression = 'zip'
log_format = '{level} {time} {message}'
rotation = '1 week'

HANDLERS: dict[str, list[LoguruHandler]] = {
    'plain': [
        LoguruHandler({
            'sink': 'logs/plain/debug.log',
            'format': '{time} {message}',
            'level': 'DEBUG',
            'rotation': rotation,
            'serialize': False,
            'compression': compression,
            'filter': lambda record: logging_level_within(record, ['DEBUG'])
        }),
        LoguruHandler({
            'sink': 'logs/plain/info.log',
            'format': log_format,
            'level': 'INFO',
            'rotation': rotation,
            'serialize': False,
            'compression': compression,
            'filter': lambda record: logging_level_within(record, ['INFO', 'WARNING'])
        }),
        LoguruHandler({
            'sink': 'logs/plain/error.log',
            'format': log_format,
            'level': 'ERROR',
            'rotation': rotation,
            'serialize': False,
            'compression': compression,
            'filter': lambda record: logging_level_within(record, ['ERROR', 'CRITICAL'])
        })
    ],
    'json': [
        LoguruHandler({
            'sink': 'logs/json/debug.log',
            'format': '{time} {message}',
            'level': 'DEBUG',
            'rotation': rotation,
            'serialize': True,
            'compression': compression,
            'filter': lambda record: logging_level_within(record, ['DEBUG'])
        }),
        LoguruHandler({
            'sink': 'logs/json/info.log',
            'format': log_format,
            'level': 'INFO',
            'rotation': rotation,
            'serialize': True,
            'compression': compression,
            'filter': lambda record: logging_level_within(record, ['INFO', 'WARNING'])
        }),
        LoguruHandler({
            'sink': 'logs/json/error.log',
            'format': log_format,
            'level': 'ERROR',
            'rotation': rotation,
            'serialize': True,
            'compression': compression,
            'filter': lambda record: logging_level_within(record, ['ERROR', 'CRITICAL'])
        })
    ]
}
