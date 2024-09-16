import subprocess
from pathlib import Path

if __name__ == '__main__':
    dashboard_path = Path(__file__).parent / 'test_dashboard2.py'
    subprocess.run(f'streamlit run {dashboard_path}', shell=True)
