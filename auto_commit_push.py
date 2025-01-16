import os
import subprocess
from datetime import datetime
import sys

def git_auto_commit_push(commit_message):
    try:
        # Step 1: Add all changes
        print("Adding changes...")
        subprocess.run(["git", "add", "."], check=True)

        # Step 2: Commit with the provided message
        print(f"Committing with message: {commit_message}")
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Step 3: Push changes to the remote repository
        print("Pushing to remote repository...")
        subprocess.run(["git", "push"], check=True)

        print("Git operations completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing: {e.cmd}")
        print(f"Error message: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Get the current time formatted as "YYYY-MM-DD HH:MM:SS"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Check if there's a command-line argument for the commit message
    if len(sys.argv) > 1:
        # Use the current time + provided argument as commit message
        commit_message = current_time + " " + " ".join(sys.argv[1:])
    else:
        # Use only the current time as the commit message
        commit_message = current_time

    # Execute the git commands with the constructed commit message
    git_auto_commit_push(commit_message)