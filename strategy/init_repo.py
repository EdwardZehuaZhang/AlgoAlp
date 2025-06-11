"""
Initialize git repository for AlgoAlp
"""
import subprocess
import os
import sys

def run_command(command):
    """Run a shell command and print output"""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(e.stderr)
        return False

def main():
    """Main function to initialize the git repository"""
    print("Initializing git repository for AlgoAlp...")
    
    # Check if git is installed
    if not run_command("git --version"):
        print("Git not found. Please install git and try again.")
        sys.exit(1)
    
    # Check if .git already exists
    if os.path.exists(".git"):
        print("Git repository already initialized.")
        choice = input("Do you want to re-initialize? (y/n): ").lower()
        if choice != 'y':
            print("Aborted.")
            return
    
    # Initialize git repository
    print("\nInitializing git repository...")
    if not run_command("git init"):
        print("Failed to initialize git repository.")
        return
    
    # Add all files
    print("\nAdding files to git...")
    if not run_command("git add ."):
        print("Failed to add files to git.")
        return
    
    # Initial commit
    print("\nCreating initial commit...")
    if not run_command('git commit -m "Initial commit of AlgoAlp trading strategy"'):
        print("Failed to create initial commit.")
        return
    
    # Prompt for GitHub repository
    print("\nWould you like to connect to a GitHub repository?")
    choice = input("Connect to GitHub? (y/n): ").lower()
    
    if choice == 'y':
        repo_url = input("Enter your GitHub repository URL: ")
        if repo_url:
            print(f"\nAdding remote repository: {repo_url}")
            if not run_command(f"git remote add origin {repo_url}"):
                print("Failed to add remote repository.")
                return
            
            print("\nPushing to GitHub...")
            if not run_command("git push -u origin master"):
                print("Failed to push to GitHub. You can try pushing manually later.")
                return
            
            print("\nSuccessfully pushed to GitHub!")
    
    print("\nGit repository initialized successfully!")
    print("\nNext steps:")
    print("1. Update your .env file with your Alpaca API credentials")
    print("2. Run 'python setup.py' to install dependencies")
    print("3. Start the strategy with 'python strategy.py'")

if __name__ == "__main__":
    main() 