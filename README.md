There are the following components

1) Manager Function: does start and manage all the rest
2) A collection of defined ETL function objects: these are the product factories
3) Executor Function: function that uses the right ETL object function to execute an ETL mission
4) Executor: set of 50-100 threads that all use the same above Executor Function to execute an etl mission 
5) ETL Missions Queue: A queue of missions to run concrete ETL function on as set of concrete ETL products  
6) ETL Operations Database: Database (index in elastic) that holds all production operations made by all ETL functions. 

