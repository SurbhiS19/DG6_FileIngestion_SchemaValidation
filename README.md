# DG6_FileIngestion_SchemaValidation
File ingestion and schema validation: Different ways of reading large data files (pandas, dask, chunksize, dictread, datatables, pyspark) have been explored and the most optimal way is suggested. 
The data file is then converted to YAML file and further compressed to gzip. Two different ways of creating yaml file has been explored using dataframes directly and second after coverting to array
