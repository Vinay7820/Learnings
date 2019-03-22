import sys, datetime, os
from pyspark.sql import SQLContext, SparkSession, Row, Column
from pyspark.sql.types import *
from pyspark.sql.functions import col
from pyspark.context import SparkContext


print ("Hi...!!!")
def main(args):
    try:
        table_name = args[1]
        input_location = args[2]
        output_location = args[3]
        table_type = args[4]
        sc = SparkContext()
        spark = SparkSession.builder \
            .appName("Data Conversion") \
            .enableHiveSupport() \
            .getOrCreate()
        sqlContext = SQLContext(spark)
        sqlContext.setConf("spark.sql.parquet.writeLegacyFormat", "true")
        #********* Check whether the Input and Output Location are ending with "/" or not ****************#
        if str(input_location).endswith("/"):
            print "Continue...!!!"
        else:
            input_location = input_location + "/"

        if str(output_location).endswith("/"):
            print "Continue...!!!"
        else:
            output_location = output_location + "/"

        #********************** Check for table type whether it's json or not **********************#
        if str(table_type.lower()) == 'json':
            print "It's Json Data"
            datardd = spark.read.json(input_location + "*")
            try:
                schemadf = sc.wholeTextFiles("s3://move-dataeng-edw-historicaldata-dev/MoveDM/Audit/Auditlog/table_spark_schema/" + table_name + ".sql")
            except Exception as err:
                print ("Hi....Error is...........")
                print (err)
            # ******************* Remove Blank Lines and create sql statement on semicoln seperator ******************#
            newschemadf = schemadf.map(lambda (k, v): v.replace('\n', '').replace('\r','').encode('utf-8').strip()) \
                .flatMap(lambda x: x.split(';')) \
                .filter(lambda x: x != '')

            print ("Hi......!!!!!!...................!!!!!!!!")

            tableschema = [x for x in newschemadf.toLocalIterator()]
            schemastmt = tableschema[0]
            print schemastmt
            caststmt = tableschema[1]

            #**************** Create the column cast statement for all the columns *****************#
            castlist = caststmt.split('^')
            castdict = dict((column_name.split(":")) for column_name in castlist)
            cast_columns = [col(key).cast(castdict[key]) for key in castdict]

            newdata = datardd.select(cast_columns)

            newdata.repartition(1).write.mode("Append").parquet(output_location)

        else:
            files_to_process = "s3://move-dataeng-edw-historicaldata-dev/MoveDM/Audit/Auditlog/last_processed_date_csv/" + table_name + "*"

            print ("Hi.........................!!!!!!!!")
            files_name = sc.textFile(files_to_process)
            filenames = [x for x in files_name.toLocalIterator()]
            num_files = len(filenames)
            npartition = num_files*10
            print ("Hi..........123...............!!!!!!!!")

            schemadf = sc.wholeTextFiles("s3://move-dataeng-edw-historicaldata-dev/MoveDM/Audit/Auditlog/table_spark_schema/" + table_name + ".sql")
            # ******************* Remove Blank Lines and create sql statement on semicoln seperator ******************#
            newschemadf = schemadf.map(lambda (k, v): v.replace('\n', '').replace('\r','').encode('utf-8').strip()) \
                .flatMap(lambda x: x.split(';')) \
                .filter(lambda x: x != '')

            print ("Hi......!!!!!!...................!!!!!!!!")

            tableschema = [x for x in newschemadf.toLocalIterator()]
            schemastmt = tableschema[0]
            print schemastmt
            caststmt = tableschema[1]

            print ("Hii...!!!!..........!")

            # **Create whether the table type is parition or non-partition and whether is there any active records file to process **#
            filenamepath = []
            active_file = ''
            if str(table_type.lower()) == 'partition':
                partition_column = filenames[0].split('=')[0]
                for file in filenames:
                    filenamepath.append(input_location + file + "/*")
            else:
                for file in filenames:
                    if "Active" in str(file):
                        active_file = (input_location + file)
                    else:
                        filenamepath.append(input_location + file)

            newfilenamepath = ",".join(filenamepath)

            datardd = sc.textFile(newfilenamepath).repartition(npartition)
            active_data_rdd = sc.textFile(active_file).repartition(50)
            print ("Hii........!!!.....!!!***")

            activedf = active_data_rdd.map(lambda x: x.split("^"))
            print("after active df")			
            listingdf = datardd.map(lambda x: x.split("^"))
            print("1")
            # **************** Create the Struct Type using all the columns *****************#
            fields = [StructField(field_name, StringType(), True) for field_name in schemastmt.split("^")]
            schema = StructType(fields)
            schemadata = spark.createDataFrame(listingdf, schema)
            activedata = spark.createDataFrame(activedf, schema)
            print("2")			
            # **************** Create the column cast statement for all the columns *****************#
            castlist = caststmt.split('^')
            castdict = dict((column_name.split(":")) for column_name in castlist)
            cast_columns = [col(key).cast(castdict[key]) for key in castdict]
            print("3")
            newdata = schemadata.select(cast_columns)
            newactivedata = activedata.select(cast_columns)
            print ("Hii........!!!***")

            # **************** Write the converted data to output location *****************#
            if str(table_type.lower()) == 'partition':
                newdata.repartition(partition_column).write.partitionBy(partition_column).mode("Append").parquet(output_location)
            else:
                newdata.repartition(num_files).write.mode("Append").parquet(output_location)
                if len(active_file) > 0:
                    newactivedata.repartition(10).write.mode("overwrite").parquet(output_location + "Active/")

            # **************** Delete the file from S3 Location which contains the input data files name *****************#
            cmd = "hdfs dfs -rm -r -skipTrash s3a://move-dataeng-edw-historicaldata-dev/MoveDM/Audit/Auditlog/last_processed_date_csv/" + table_name + "*"
            os.system(cmd)

    except Exception,err:
        print str(err)

if __name__ == "__main__":
    main(sys.argv)

