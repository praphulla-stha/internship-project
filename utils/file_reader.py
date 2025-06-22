import json
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def read_json_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            logger.info(f"Successfully read JSON file: {file_path}")
            return data
    except Exception as e:
        logger.error(f"Error reading {file_path}: {e}")
        return None