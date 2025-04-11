several use cases:
- internal  - fit predict for timeseries - we wanted to be able to fit many series at once and predict them using UDF - I researched spark as a way to scale computation on many time-series at once => afterwards I decided that for our data set we don't need spark to do this.
- external client: Hilo - their architecture included spark and databricks - https://github.com/stepinski/notes/blob/75c77c7fdf11f80a5aa293e3e9bee93351df38ee/projects/hilo/hilo-architecture.jpeg - also airflow and  pyspark jobs - we considered fitting into their pipeline - kubeflow / spark
internal - fit predict vs tesler:
fit predict in tesler vs spark
in spark we can easily fit a 1 time massive model - we won't be able to run this many times
- [ ]  how we can call predict using pyspark job - many series at once

this is my pyspark training:
https://github.com/stepinski/machinelearning/tree/master/spark-train/pyspark



------------------
my projects:
time--series
data imputation with flint
example in scala ( interesting method):
https://www.jowanza.com/blog/time-series-missing-data-imputation-in-apache

example in pyspark:
https://www.databricks.com/blog/2018/09/11/introducing-flint-a-time-series-library-for-apache-spark.html
https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/1281142885375883/1566406256250190/7729323681064935/latest.html

- [ ] find sp500 dataset
- [ ] try to rewrite it in my own notebook using multiple timeseries indexed by name
- [ ] try find other tutorials, examples, walkthroughs -> everything is there  https://www.databricks.com/blog/2018/09/11/introducing-flint-a-time-series-library-for-apache-spark.html
put them on the checklist to try


 