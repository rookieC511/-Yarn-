#!/bin/bash
#firstjob
spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --queue first \
    --archives hdfs:///hadoop/hadoop_env.tar.gz#conda_env \
    /usr/WordCount.py&
# secondjob
spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --queue first \
    --archives hdfs:///hadoop/hadoop_env.tar.gz#conda_env \
    /usr/WordCountsecond.py&
# thirdjob
spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --queue first \
    --archives hdfs:///hadoop/hadoop_env.tar.gz#conda_env \
    /usr/WordCountthird.py&
# fourthjob
spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --queue first \
    --archives hdfs:///hadoop/hadoop_env.tar.gz#conda_env \
    /usr/WordCountfourth.py&
# fifthjob
spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --queue first \
    --archives hdfs:///hadoop/hadoop_env.tar.gz#conda_env \
    /usr/WordCount5.py&

# fifthjob
spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --queue second \
    --archives hdfs:///hadoop/hadoop_env.tar.gz#conda_env \
    /usr/WordCount6.py&
# fifthjob
spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --queue second \
    --archives hdfs:///hadoop/hadoop_env.tar.gz#conda_env \
    /usr/WordCount7.py&
# fifthjob
spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --queue second \
    --archives hdfs:///hadoop/hadoop_env.tar.gz#conda_env \
    /usr/WordCount8.py&
# fifthjob
spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --queue second \
    --archives hdfs:///hadoop/hadoop_env.tar.gz#conda_env \
    /usr/WordCount9.py&
# fifthjob
spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --queue second \
    --archives hdfs:///hadoop/hadoop_env.tar.gz#conda_env \
    /usr/WordCount10.py&
wait
