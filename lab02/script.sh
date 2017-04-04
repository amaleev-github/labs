hadoop fs -rm -r -f /tmp/andrey.maleev/lab02

hadoop jar /usr/hdp/2.5.3.0-37/hadoop-mapreduce/hadoop-streaming.jar -D mapred.reduce.tasks=1 -input /labs/facetz_2015_02_15/part* -output /tmp/andrey.maleev/lab02 -mapper "python mapper.py" -reducer "python reducer.py" -file mapper.py -file reducer.py