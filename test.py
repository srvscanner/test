# DLP Test File - GitHub Upload Monitoring
# Purpose: Validate Microsoft Purview Endpoint DLP file upload monitoring

import datetime

application_name = "DLP GitHub Upload Test"
developer = "Test User"

def get_application_info():
    return {
        "Application": application_name,
        "Developer": developer,
        "Test_Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Purpose": "Testing Endpoint DLP monitoring for GitHub uploads"
    }


def process_data(data):
    """
    Sample function representing data processing.
    This file contains no production data.
    """
    result = f"Processing data: {data}"
    return result


if __name__ == "__main__":
    info = get_application_info()

    print("=== Application Information ===")
    for key, value in info.items():
        print(f"{key}: {value}")

    sample_input = "Test data upload to GitHub"
    print(process_data(sample_input))