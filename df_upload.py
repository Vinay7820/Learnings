from urllib.parse import quote_plus  # PY2: from urllib import quote_plus
from sqlalchemy.engine import create_engine
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import Table, MetaData
from sqlalchemy import create_engine
import pandas as pd
import sqlalchemy

conn_str = 'awsathena+rest://{aws_access_key_id}:{aws_secret_access_key}@athena.{region_name}.amazonaws.com:443/'\
           '{schema_name}?s3_staging_dir={s3_staging_dir}'
engine = create_engine(conn_str.format(
    aws_access_key_id=quote_plus(''),
    aws_secret_access_key=quote_plus(''),
    region_name='us-west-2',
    schema_name='informatica_testing',
    s3_staging_dir=quote_plus('s3://')))


df = pd.read_csv('/home/centos/niranjan/Book1.csv')
print(df)
#df.to_sql('calistings', con=engine,if_exists='replace')
#print(df)
#engine.execute("SELECT * FROM informatica_testing.calistings").fetchall()
#print(select(df.to_sql('calistings', con=engine,if_exists='replace'), from_obj=many_rows).scalar())
#many_rows = Table('calistings', MetaData(bind=engine), autoload=True)
#print(select([select * from informatica_testing limit 10], from_obj=many_rows).scalar())
metadata = MetaData(bind=engine)
lists = df.to_dict(orient='records')
print(lists)
table = sqlalchemy.Table('calistings', metadata)
metadata.create_all()
engine.execute(table.insert().values(lists))
print("Completed")
