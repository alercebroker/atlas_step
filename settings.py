##################################################
#       atlas   Settings File
##################################################
import os
DB_CONFIG = {
    "PSQL": {
        "HOST": "18.211.226.219",
        "USER": "alerce",
        "PASSWORD": "ETgW4GTdR337gjP7",
        "PORT": 5432,
        "DB_NAME": "new_pipeline"
    }
}
"""
DB_CONFIG = {
    "PSQL": {
        "HOST": os.environ["DB_HOST"],
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASSWORD"],
        "PORT": int(os.environ["DB_PORT"]),
        "DB_NAME": os.environ["DB_NAME"]
    }
}
"""

CONSUMER_CONFIG = {
    "TOPICS": ["test_atlas"],
    "PARAMS": {
        'bootstrap.servers' : 'ec2-3-22-33-46.us-east-2.compute.amazonaws.com:9092',
        'auto.offset.reset' : 'earliest',
        'group.id': "atlas_step_3"
    }
}

PRODUCER_CONFIG = {
    "TOPIC": "atlas_output",
    "PARAMS": {
        'bootstrap.servers' : 'ec2-3-22-33-46.us-east-2.compute.amazonaws.com:9092',
        'message.max.bytes': 6291456
    },
    "SCHEMA": {
        'doc': 'Lightcurve',
        'name': 'lightcurve',
        'type': 'record',
        'fields': [
            {'name': 'oid', 'type': 'string'},
            {'name': 'candid', 'type': 'string'},
            {'name': 'detections', 'type': {
                'type': 'array',
                'items': {
                    'type': 'record',
                    'name': 'detection',
                    'fields': [
                        {'name': 'candid', 'type': 'string'},
                        {'name': 'mjd', 'type': 'float'},
                        {'name': 'fid', 'type': 'int'},
                        {'name': 'magpsf_corr', 'type': ['float', 'null'], 'default':None},
                        {'name': 'magap_corr', 'type': ['float', 'null'], 'default':None},
                        {'name': 'sigmapsf_corr', 'type': ['float', 'null'], 'default':None},
                        {'name': 'sigmagap_corr', 'type': ['float', 'null'], 'default':None},
                        {'name': 'ra', 'type': 'float'},
                        {'name': 'dec', 'type': 'float'},
                        {'name': 'rb', 'type': ['float', 'null'], 'default':None},
                        {'name': 'oid', 'type': 'string'},
                        {'name': 'alert',
                         'type': {
                             'type': 'map',
                             'values': ['int', 'float', 'string', 'null']
                         }}
                    ]
                }
            }},
            {'name': 'non_detections', 'type': {
                'type': 'array',
                'items': {
                    'type': 'map',
                    'values': ['float', 'int', 'string', 'null']
                }
            }}
        ],
    }
}

## Step Configuration
STEP_CONFIG = {
    "DB_CONFIG": DB_CONFIG,
    "PRODUCER_CONFIG": PRODUCER_CONFIG
}