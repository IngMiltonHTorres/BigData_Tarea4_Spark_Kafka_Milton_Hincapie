# BigData_Tarea4_Spark_Kafka_Milton_Hincapie
Procesamiento Batch y Streaming con PySpark, Apache Kafka y HDFS fase 3 materia Big Data UNAD

# Tarea 4: Procesamiento Batch y Real-Time Streaming con Apache Spark, Kafka y HDFS

Este repositorio contiene la solución técnica para el procesamiento de datos masivos (Batch) e ingesta en tiempo real (Streaming) utilizando el ecosistema Big Data en un entorno Linux (Ubuntu).

Tecnologías Utilizadas
* **Apache Hadoop (HDFS):** Almacenamiento distribuido.
* **Apache Spark (PySpark):** Motor de procesamiento Batch y Structured Streaming.
* **Apache Kafka & Zookeeper:** Transmisión y mensajería de eventos en tiempo real.
* **Python 3:** Desarrollo de scripts de producción y procesamiento (`kafka-python`, `pyspark`).


Estructura del Proyecto
* `Tarea4.py`: Script para el procesamiento Batch de datos de cobertura móvil desde HDFS.
* `kafka_producer.py`: Script generador de eventos JSON en tiempo real hacia el topic `sensor_data` de Kafka.
* `spark_streaming_consumer.py`: Consumidor Spark Streaming que agrupa y calcula promedios por ventanas de tiempo de 1 minuto.

## Instrucciones de Ejecución programas


================ Procesamiento Batch (PySpark + HDFS) ================

1. Iniciar los servicios de HDFS:

      $HADOOP_HOME/sbin/start-dfs.sh

2. Ejecutar la tarea Batch
   
      python3 Tarea4.py

======================================================================

======== Procesamiento Streaming en Tiempo Real (Kafka + Spark Streaming) =========

Para ejecutar el procesamiento se requieren conexion por 4 terminales distintas por putty y en cada una ejecutar los siguientes comandos:

Terminal 1 - Iniciar Zookeeper:

  /opt/Kafka/bin/zookeeper-server-start.sh /opt/Kafka/config/zookeeper.properties

Terminal 2 - Iniciar Broker de Kafka:

  /opt/Kafka/bin/kafka-server-start.sh /opt/Kafka/config/server.properties

Terminal 3 - Iniciar el Productor de datos:

  python3 kafka_producer.py

Terminal 4 - Iniciar el Consumidor Spark Streaming:

$SPARK_HOME/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 spark_streaming_consumer.py

=====================================================================================
   
