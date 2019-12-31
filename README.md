# SF-Crime-Statistics-with-Spark-Streaming

How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

Changing values on the SparkSession property parameters may lead to changing throughput and latency of the data. We can check progress reporter to evaluate the impact. I use inputRowsPerSecond and processedRowsPerSecond to do this.

What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

I modified many parameters and observed the change of inputRowsPerSecond and processedRowsPerSecond. When I increase and decrease these parameters, the performance of inputRowsPerSecond and processedRowsPerSecond decreases, and these two values are the best performers

```python
"spark.streaming.kafka.maxRatePerPartition": 200
"spark.default.parallelism": 200
```
