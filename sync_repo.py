repo_url = "https://github.com/HariCharan-91/MDI-NOTV.git"
repo_dir = "/content/MDI-NOTV"

script_content = f'''
import os

REPO_URL = "{repo_url}"
REPO_DIR = "{repo_dir}"

def sync_repo():
    if not os.path.exists(REPO_DIR):
        print("Cloning the repository...")
        os.system(f"git clone {{REPO_URL}}")
    else:
        print("Repository already exists. Pulling the latest updates...")
        os.chdir(REPO_DIR)
        os.system("git pull origin main")

if __name__ == "__main__":
    sync_repo()
    print("✅ Repository synced successfully.")
'''

# Create the script file
with open("sync_repo.py", "w") as file:
    file.write(script_content)

print("sync_repo.py created successfully.")
