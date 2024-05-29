# PySpark Setup and Integration with Jupyter Notebook

This repository contains instructions on setting up PySpark and integrating it with Jupyter Notebook for interactive data analysis.

## Prerequisites

Before starting, ensure you have the following installed:
- Python 3
- Java Development Kit (JDK) 8 or higher

## Installing Spark

1. Download Spark: Visit the [Spark downloads page](https://spark.apache.org/downloads.html) and select the latest release.
2. Extract Spark: Unzip the downloaded file and move it to the `/opt` folder:
```bash
   $ tar -xzf spark-1.2.0-bin-hadoop2.4.tgz
   $ mv spark-1.2.0-bin-hadoop2.4 /opt/spark-1.2.0
```
3. Create a symbolic link:
```bash
$ ln -s /opt/spark-1.2.0 /opt/spark
```
4. Set up environment variables:
Add the following lines to your ~/.bashrc or ~/.zshrc file:

```bash
export SPARK_HOME=/opt/spark
export PATH=$SPARK_HOME/bin:$PATH
```
## Installing Jupyter Notebook

1. Install Jupyter Notebook:
```bash
$ pip install jupyter
```
## Running PySpark in Jupyter Notebook
1. Update PySpark driver environment variables:
Add these lines to your ~/.bashrc or ~/.zshrc file:
```bash
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='notebook'
```
2. Restart your terminal.
3. Launch PySpark:
```bash
$ pyspark
```

4. PySpark should now start a Jupyter Notebook in your web browser.

## Additional Resources

- [Official Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/stable/)



