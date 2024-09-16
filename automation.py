import schedule
import time
import subprocess

def run_all_scans():
    print("Running all security scans...")
    subprocess.run(['python3', 'scans/nmap_scan.py'])
    subprocess.run(['python3', 'scans/nikto_scan.py'])
    subprocess.run(['python3', 'scans/dependency_check.py'])

def job():
    run_all_scans()

# Schedule the job to run daily
schedule.every().day.at("02:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
