from utils.utils import new_function
from data.loader import load_data
from services.services import run_service

def main():
    new_function()
    load_data()
    run_service()

if __name__ == "__main__":
    main()
