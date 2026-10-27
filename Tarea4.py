from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# 1. INICIALIZAR SPARK Y CARGAR DATOS (Procesamiento Batch)
spark = SparkSession.builder.appName("Tarea4_Simple").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df = spark.read.option("header", "true") \
               .option("sep", ";") \
               .csv("hdfs://localhost:9000/Tarea4/cobertura_movil.csv")

# 2. LIMPIEZA Y TRANSFORMACIÓN
# Eliminar duplicados y normalizar columna 4G (1 si es 'S', 0 si no)
df_clean = df.dropDuplicates() \
             .withColumn("ES_4G", F.when(F.col("COBERTUTA 4G") == "S", 1).otherwise(0))

# 3. ANÁLISIS EXPLORATORIO (EDA)
# Conteo por Proveedor
print("\n--- TOP PROVEEDORES ---")
df_clean.groupBy("PROVEEDOR").count().orderBy(F.col("count").desc()).show(5, False)

# Suma de cobertura 4G por Departamento
df_4g = df_clean.groupBy("DEPARTAMENTO") \
                .agg(F.sum("ES_4G").alias("TOTAL_4G")) \
                .orderBy(F.col("TOTAL_4G").desc())

# 4. VISUALIZACIÓN BATCH EN CONSOLA (Gráfico ASCII)
print("\n--- VISUALIZACIÓN: TOP 5 DEPARTAMENTOS CON 4G ---")
top_5 = df_4g.limit(5).collect()
max_val = top_5[0]["TOTAL_4G"]

for row in top_5:
    barra = "█" * int((row["TOTAL_4G"] / max_val) * 30)
    print(f"{row['DEPARTAMENTO']:<15} | {barra} ({row['TOTAL_4G']})")

spark.stop()
