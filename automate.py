import subprocess
import sys

def run_command(command, description):
    print(f"--- Running: {description} ---")
    # This runs the command and waits for it to finish
    result = subprocess.run(command, shell=True)
    
    if result.returncode != 0:
        print(f"❌ {description} FAILED")
        return False
    
    print(f"✅ {description} PASSED\n")
    return True

def main():
    # 1. Run the Linter (Flake8)
    lint_passed = run_command("flake8 calc.py", "Linting Check")
    
    # 2. Run the Math Script
    math_passed = run_command("python calc.py", "Math Logic Check")
    
    # If anything failed, exit with code 1 to turn the GitHub Action RED
    if not lint_passed or not math_passed:
        sys.exit(1)
    
    print("All checks passed successfully!")
    sys.exit(0)

if __name__ == "__main__":
    main()
