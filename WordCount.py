from pyspark import SparkContext
import os

if __name__ == "__main__":
    os.system("source conda_env/bin/activate")
    sc = SparkContext(appName="WordCountfirst")

    # 输入和输出路径
    input_path = "hdfs:///hadoop/input/wordcount.txt"
    output_path = "hdfs:///hadoop/outputfirst"

    # 从 HDFS 读取输入文件
    text_file = sc.textFile(input_path)


    word_counts = (
        text_file.flatMap(lambda line: line.split(" "))  # 拆分每一行的单词
                 .map(lambda word: (word, 1))           # 每个单词映射为键值对 (word, 1)
                 .reduceByKey(lambda a, b: a + b)       # 按键 (word) 聚合频率
    )


    word_counts.saveAsTextFile(output_path)


    sc.stop()
