There are the following components

1) Manager application to manage everything
2) A collection of defined ETL function objects
3) A queue of missions - missions to run concrete ETL function on concrete product partitions to create a new product partition.
4) Executor: Bunch of 50-100 threads that take ETL missions and run then on the mission inputs to create the output
5) Database table (index in elastic) that hold all production operations made by ETL function. This is the meta data
holding tall the production operations not the data itself, namely data control.
