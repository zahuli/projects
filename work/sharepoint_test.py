import requests
import json
import os
from pathlib import Path

def load_config():
    """Load configuration from config.json file"""
    # Look for config file in current directory or parent directory
    config_paths = [
        Path("config.json"),
        Path("..") / "config.json",
        Path("../..") / "config.json"
    ]
    
    for config_path in config_paths:
        if config_path.exists():
            try:
                with open(config_path, 'r') as f:
                    config = json.load(f)
                print(f"✓ Configuration loaded from {config_path}")
                return config
            except Exception as e:
                print(f"✗ Failed to load configuration from {config_path}: {e}")
    
    print("✗ No configuration file found. Please create config.json")
    return None

def test_sharepoint_connection():
    # Load configuration
    config = load_config()
    if not config:
        return
    
    # Extract configuration values
    tenant_id = config.get("tenant_id")
    client_id = config.get("client_id")
    client_secret = config.get("client_secret")
    site_url = config.get("site_url")
    
    # Validate required configuration
    required_fields = ["tenant_id", "client_id", "client_secret", "site_url"]
    missing_fields = [field for field in required_fields if not config.get(field)]
    if missing_fields:
        print(f"✗ Missing required configuration fields: {missing_fields}")
        return
    
    # Step 1: Get access token
    print("Getting access token...")
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    token_data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "https://graph.microsoft.com/.default",
        "grant_type": "client_credentials"
    }
    token_headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    try:
        token_response = requests.post(token_url, data=token_data, headers=token_headers)
        token_response.raise_for_status()
        token_json = token_response.json()
        access_token = token_json["access_token"]
        print("✓ Access token obtained successfully")
    except Exception as e:
        print(f"✗ Failed to get access token: {e}")
        return
    
    # Set authorization header for subsequent requests
    auth_header = {"Authorization": f"Bearer {access_token}"}
    graph_base_url = "https://graph.microsoft.com/v1.0"
    
    # Step 2: Get site information
    print("\nGetting site information...")
    try:
        site_response = requests.get(f"{graph_base_url}/sites/{site_url}", headers=auth_header)
        site_response.raise_for_status()
        site_data = site_response.json()
        site_id = site_data["id"]
        print(f"✓ Site information retrieved successfully")
        print(f"  Site ID: {site_id}")
        print(f"  Site Name: {site_data['displayName']}")
    except Exception as e:
        print(f"✗ Failed to get site information: {e}")
        return
    
    # Step 3: Get drives information
    print("\nGetting drives information...")
    try:
        drives_response = requests.get(f"{graph_base_url}/sites/{site_id}/drives", headers=auth_header)
        drives_response.raise_for_status()
        drives_data = drives_response.json()
        
        if drives_data["value"]:
            drive_id = drives_data["value"][0]["id"]
            drive_name = drives_data["value"][0]["name"]
            print(f"✓ Drives information retrieved successfully")
            print(f"  Drive ID: {drive_id}")
            print(f"  Drive Name: {drive_name}")
        else:
            print("✗ No drives found")
            return
    except Exception as e:
        print(f"✗ Failed to get drives information: {e}")
        return
    
    # Step 4: Get root folder children
    print("\nGetting root folder children...")
    try:
        children_response = requests.get(
            f"{graph_base_url}/drives/{drive_id}/root/children", 
            headers=auth_header
        )
        children_response.raise_for_status()
        children_data = children_response.json()
        
        print("✓ Root folder children retrieved successfully")
        print(f"  Found {len(children_data.get('value', []))} items in root folder")
        
        # Display first few items (if any)
        items = children_data.get('value', [])
        if items:
            print("\nFirst few items:")
            for i, item in enumerate(items[:3]):
                print(f"  {i+1}. {item.get('name', 'N/A')} ({item.get('folder', {}).get('childCount', 0) if 'folder' in item else 'file'})")
            if len(items) > 3:
                print(f"  ... and {len(items) - 3} more items")
        else:
            print("  No items found in root folder")
            
    except Exception as e:
        print(f"✗ Failed to get root folder children: {e}")
        return
    
    print("\n✅ All SharePoint connection tests completed successfully!")

if __name__ == "__main__":
    test_sharepoint_connection()