import os
import shutil
import hashlib
import time
import argparse
import logging
from datetime import datetime

# Function to calculate MD5:
def get_file_hash(file_location):
    md5_hash = hashlib.md5()
    with open(file_location, "rb") as opened_file:
        for data_chunk in iter(lambda: opened_file.read(4096), b""):
            md5_hash.update(data_chunk)
    return md5_hash.hexdigest()

# Function to synchronize files:
def synchronize_directories(source_dir, replica_dir, log):
    if not os.path.exists(replica_dir):
        os.makedirs(replica_dir)
        log.info(f"Replica folder '{replica_dir}' created.")
        
        # To add the files in the copy folder:
    for dir_path, sub_dirs, file_list in os.walk(source_dir):
        relative_path = os.path.relpath(dir_path, source_dir)
        current_replica_path = os.path.join(replica_dir, relative_path)

        if not os.path.exists(current_replica_path):
            os.makedirs(current_replica_path)
            log.info(f"Created directory: {current_replica_path}")

        for file_name in file_list:
            source_file_path = os.path.join(dir_path, file_name)
            replica_file_path = os.path.join(current_replica_path, file_name)

            if not os.path.exists(replica_file_path):
                shutil.copy2(source_file_path, replica_file_path)
                log.info(f"Copied file: {source_file_path} -> {replica_file_path}")

    # To remove the files if not in the original folder:
    for dir_path, sub_dirs, file_list in os.walk(replica_dir):
        relative_path = os.path.relpath(dir_path, replica_dir)
        corresponding_source_path = os.path.join(source_dir, relative_path)

        for directory in sub_dirs:
            source_sub_dir = os.path.join(corresponding_source_path, directory)
            replica_sub_dir = os.path.join(dir_path, directory)
            if not os.path.exists(source_sub_dir):
                shutil.rmtree(replica_sub_dir)
                log.info(f"Removed directory: {replica_sub_dir}")

        for file_name in file_list:
            replica_file_path = os.path.join(dir_path, file_name)
            source_file_path = os.path.join(corresponding_source_path, file_name)
            if not os.path.exists(source_file_path):
                os.remove(replica_file_path)
                log.info(f"Removed file: {replica_file_path}")

# Main function:
def run_synchronization():
    # Parse arguments:
    argument_parser = argparse.ArgumentParser(description="Folder synchronization project.")
    argument_parser.add_argument("source", type=str, help="Path to the source folder.")
    argument_parser.add_argument("replica", type=str, help="Path to the copy folder.")
    argument_parser.add_argument("sync_interval", type=int, help="Synchronization interval in seconds.")
    argument_parser.add_argument("log_output", type=str, help="Path to the log file.")
    arguments = argument_parser.parse_args()

    # Logging
    logging.basicConfig(filename=arguments.log_output, level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s - %(message)s")
    sync_logger = logging.getLogger()
    console_logger = logging.StreamHandler()
    console_logger.setLevel(logging.INFO)
    sync_logger.addHandler(console_logger)

    # Log details:
    sync_logger.info("Starting folder synchronization...")
    sync_logger.info(f"Source folder: {arguments.source}")
    sync_logger.info(f"Copy folder: {arguments.replica}")
    sync_logger.info(f"Synchronization interval: {arguments.sync_interval} seconds")
    sync_logger.info(f"Logging to: {arguments.log_output}")

    # Run synchronization from x to x interval seconds:
    while True:
        sync_logger.info("Synchronization started.")
        synchronize_directories(arguments.source, arguments.replica, sync_logger)
        sync_logger.info("Synchronization completed.")
        time.sleep(arguments.sync_interval)

if __name__ == "__main__":
    run_synchronization()
