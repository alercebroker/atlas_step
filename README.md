# ATLAS

## Description

Light curve correction from detections of ATLAS data stream. 

#### Previous steps: 
- None

#### Next steps:
- None

## Database interactions

This step interact with some tables of `new_pipeline` database. 

### Select:
- The function [`get_ligthcurve`](https://github.com/alercebroker/correction_step/blob/master/correction/step.py#L202) select detections and non-detections of an object. 

### Insert:
- New detection.
- New non-detection(s).

## Previous conditions

No special conditions, only connection to kafka, database and elasticsearch.

## Libraries used
- APF
- Numpy
- Astropy

## Environment variables

### Database setup

- `DB_HOST`: Database host for connection.
- `DB_USER`: Database user for read/write (requires these permission).
- `DB_PASSWORD`: Password of user.
- `DB_PORT`: Port connection.
- `DB_NAME`: Name of database.

### Consumer setup

- `CONSUMER_TOPICS`: Some topics. String separated by commas. e.g: `topic_one` or `topic_two,topic_three`
- `CONSUMER_SERVER`: Kafka host with port. e.g: `localhost:9092`
- `CONSUMER_GROUP_ID`: Name for consumer group. e.g: `atlas`

### Producer setup

- `PRODUCER_TOPIC`: Name of output topic. e.g: `atlas_output`
- `PRODUCER_SERVER`: Kafka host with port. e.g: `localhost:9092`


## Stream

This step require a consumer and producer.

### Input schema

[Documentation of ATLAS avro files schema.](https://github.com/alercebroker/atlas-avro/blob/master/schema/alert.avsc) 


### Output schema
```Python
{
  "doc": "Lightcurve",
  "name": "lightcurve",
  "type": "record",
  "fields": [
    {
      "name": "oid",
      "type": "string"
    },
    {
      "name": "candid",
      "type": "string"
    },
    {
      "name": "fid",
      "type": "int"
    }
    {
      "name": "detections",
      "type": {
        "type": "array",
        "items": {
          "type": "record",
          "name": "detection",
          "fields": [
            {
              "name": "candid",
              "type": "string"
            },
            {
              "name": "mjd",
              "type": "float"
            },
            {
              "name": "fid",
              "type": "int"
            },
            {
              "name": "magpsf_corr",
              "type": [
                "float",
                "null"
              ],
              "default": None
            },
            {
              "name": "magap_corr",
              "type": [
                "float",
                "null"
              ],
              "default": None
            },
            {
              "name": "sigmapsf_corr",
              "type": [
                "float",
                "null"
              ],
              "default": None
            },
            {
              "name": "sigmagap_corr",
              "type": [
                "float",
                "null"
              ],
              "default": None
            },
            {
              "name": "ra",
              "type": "float"
            },
            {
              "name": "dec",
              "type": "float"
            },
            {
              "name": "rb",
              "type": [
                "float",
                "null"
              ],
              "default": None
            },
            {
              "name": "oid",
              "type": "string"
            },
            {
              "name": "alert",
              "type": {
                "type": "map",
                "values": [
                  "int",
                  "float",
                  "string",
                  "null"
                ]
              }
            }
          ]
        }
      }
    },
    {
      "name": "non_detections",
      "type": {
        "type": "array",
        "items": {
          "type": "map",
          "values": [
            "float",
            "int",
            "string",
            "null"
          ]
        }
      }
    }
  ]
}
```

## Run step

You can run the step by using a simple python command: ``python run_step.py``.
