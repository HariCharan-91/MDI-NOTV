import os
import requests
from tqdm import tqdm

# Define directories
HUMAN_PARSING_DIR = "ckpt\humanparsing"
OPENPOSE_CKPTS_DIR = "ckpt\openpose\ckpts"

# Create folders if they don't exist
os.makedirs(HUMAN_PARSING_DIR, exist_ok=True)
os.makedirs(OPENPOSE_CKPTS_DIR, exist_ok=True)

# List of files to download (URL -> Save As)
files = {
    "https://huggingface.co/yisol/IDM-VTON/resolve/main/humanparsing/parsing_atr.onnx": os.path.join(HUMAN_PARSING_DIR, "parsing_atr.onnx"),
    "https://huggingface.co/yisol/IDM-VTON/resolve/main/humanparsing/parsing_lip.onnx": os.path.join(HUMAN_PARSING_DIR, "parsing_lip.onnx"),
    "https://huggingface.co/yisol/IDM-VTON/resolve/main/openpose/ckpts/body_pose_model.pth": os.path.join(OPENPOSE_CKPTS_DIR, "body_pose_model.pth"),
}

# Function to download and replace files
def download_file(url, save_path):
    """Downloads a file from a URL and replaces it if it exists."""
    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        file_size = int(response.headers.get("content-length", 0))
        desc = f"Downloading {os.path.basename(save_path)}"
        
        with open(save_path, "wb") as file, tqdm(
            desc=desc,
            total=file_size,
            unit="B",
            unit_scale=True,
            unit_divisor=1024
        ) as bar:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
                bar.update(len(chunk))
        
        print(f"✅ Saved: {save_path}")
    else:
        print(f"❌ Failed to download {url} (Status Code: {response.status_code})")

# Download and replace files
def download_models():
    """Downloads all necessary models and replaces them if they exist."""
    for url, path in files.items():
        download_file(url, path)

if __name__ == "__main__":
    download_models()
    print("\n✅ All files downloaded successfully and saved in the correct folders.")
