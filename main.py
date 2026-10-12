import os
from datetime import datetime

def main():
    print("Daily funny cartoon automation")
    print("Date:", datetime.now().strftime("%Y-%m-%d"))
    print("YouTube refresh token:",
          "available" if os.getenv("YOUTUBE_REFRESH_TOKEN") else "missing")

if __name__ == "__main__":
    main()
