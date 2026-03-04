#!/usr/bin/python3
"""
Module for converting CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to JSON format and saves it to data.json.

    Args:
        csv_filename (str): The name of the CSV file to read.
    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        data = []
        with open(csv_filename, mode="r", encoding="utf-8") as csv_f:
            reader = csv.DictReader(csv_f)
            for row in reader:
                data.append(row)

        with open("data.json", mode="w", encoding="utf-8") as json_f:
            json.dump(data, json_f)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
