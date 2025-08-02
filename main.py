#!/usr/bin/env python3
"""
Curse Project - Main Application
"""

import sys
import os
from datetime import datetime

def main():
    """Main function for the Curse project"""
    print("Welcome to Curse Project!")
    print(f"Current time: {datetime.now()}")
    print("This is a sample Python application.")
    
    # Example functionality
    data = [1, 2, 3, 4, 5]
    print(f"Sample data: {data}")
    print(f"Sum of data: {sum(data)}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 