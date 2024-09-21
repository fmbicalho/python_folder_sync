# Folder Synchronization Tool

This Python program synchronizes files between a source folder and a replica folder. It ensures that the replica folder matches the source folder by copying new or modified files from the source and deleting files that no longer exist in the source. The synchronization runs at a regular interval defined by the user and maintains a log of all operations.

## Features  

- **One-way synchronization:** Keeps the replica folder in sync with the source folder.
- **File copying:** Automatically copies new or updated files from the source to the replica.
- **File deletion:** Removes files from the replica folder that are no longer present in the source.
- **Logging:** Logs synchronization activity, including file copying and deletion, for easy tracking.

## Requirements  

- Python 3.x
- Standard Python libraries: `os`, `shutil`, `hashlib`, `time`, `argparse`, and `logging`

## How to Use

### Step 1: Clone the Repository
First, clone the repository to your local machine:  

```git clone https://github.com/fmbicalho/python_folder_sync.git```  

### Step 2: Ensure Python is Installed: Make sure Python 3 is installed on your system. You can check the version with:  

```python3 --version```  

### Step 3: Run the Program: To start the synchronization process, open a terminal and run the following command:  

```python3 sync.py <source_folder> <replica_folder> <sync_interval> <log_file>```  

<source_folder>: The path to the folder whose contents you want to sync.  
<replica_folder>: The path to the folder that will be updated.  
<sync_interval>: The time interval (in seconds) between syncs.  
<log_file>: The path where the log file will be saved.```  

Example:

```python3 sync.py /Users/yourname/source /Users/yourname/replica 10 /Users/yourname/sync.log```  

### Step 4: Check the Log: All synchronization actions, including file copies and deletions, are recorded in the log file specified in the command. Open the log file to see what changes were made during each synchronization cycle.  

### Step 5: Stop the Program: The program will keep running, syncing the folders at the specified interval. To stop it, simply press CTRL+C in the terminal window where it is running or control+c on MacOS.  

## Logs:  

The tool generates detailed logs, recording every operation performed during synchronization.  

You can use the log file to verify what files were copied or deleted and monitor the synchronization process. You can check the logs by running the following command:

```cat /Users/yourname/replica/sync.log```


## License:  

This tool is open-source.