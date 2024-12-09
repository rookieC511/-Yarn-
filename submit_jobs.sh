#!/bin/bash
#firstjob
spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --queue second \
    --archives hdfs:///hadoop/hadoop_env.tar.gz#conda_env \
    /usr/WordCount.py&


# secondjob
spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --queue second \
    --archives hdfs:///hadoop/hadoop_env.tar.gz#conda_env \
    /usr/WordCountsecond.py&

# thirdjob
spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --queue second \
    --archives hdfs:///hadoop/hadoop_env.tar.gz#conda_env \
    /usr/WordCountthird.py&

#fourth job
spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --queue second \
    --archives hdfs:///hadoop/hadoop_env.tar.gz#conda_env \
    /usr/WordCountfourth.py&

wait

