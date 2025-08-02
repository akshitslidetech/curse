"""
Utility functions for the Curse project
"""

import json
import csv
from typing import List, Dict, Any

def load_data(file_path: str) -> List[Dict[str, Any]]:
    """Load data from a JSON or CSV file"""
    if file_path.endswith('.json'):
        with open(file_path, 'r') as f:
            return json.load(f)
    elif file_path.endswith('.csv'):
        data = []
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        return data
    else:
        raise ValueError("Unsupported file format. Use .json or .csv")

def save_data(data: List[Dict[str, Any]], file_path: str) -> None:
    """Save data to a JSON or CSV file"""
    if file_path.endswith('.json'):
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
    elif file_path.endswith('.csv'):
        if data:
            fieldnames = data[0].keys()
            with open(file_path, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
    else:
        raise ValueError("Unsupported file format. Use .json or .csv")

def process_data(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Process data and return summary statistics"""
    if not data:
        return {}
    
    # Calculate basic statistics
    numeric_fields = []
    for key in data[0].keys():
        try:
            float(data[0][key])
            numeric_fields.append(key)
        except (ValueError, TypeError):
            continue
    
    stats = {}
    for field in numeric_fields:
        values = [float(item[field]) for item in data if item.get(field)]
        if values:
            stats[field] = {
                'count': len(values),
                'sum': sum(values),
                'mean': sum(values) / len(values),
                'min': min(values),
                'max': max(values)
            }
    
    return stats 