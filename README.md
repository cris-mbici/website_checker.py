# Website Checker

## Things I learnt

[Watch the demo](https://github.com/cris-mbici/website_checker.py/raw/main/web_checker_demo.mp4)
This project taught me several key programming concepts and practical skills:

### 1. **Working with CSV Files**
- Learned how to **read data from a CSV file** using the `csv` module.
- Understood the importance of **iterating over file contents row by row**.

### 2. **Making HTTP Requests**
- Used the `requests` library to **send GET requests** to websites.
- Learned about **timeouts** to prevent the script from waiting indefinitely.

### 3. **Understanding HTTP Response Codes**
- Explored common HTTP status codes like `200`, `404`, `403`, and `429`.
- Understood how websites can be **online, blocked, not found, or rate-limited**.

### 4. **Error Handling**
- Implemented `try-except` blocks to handle network errors gracefully.
- Avoided crashes when a website is unreachable.
- The `try-except` block has been a major hurdle for me but I've grasped it after this project.

---
## How It Works
- The script **reads website URLs from a CSV file** (`test_sites.csv`).
- It **checks if each website is online or offline** by making a HTTP request.
- It **interprets response codes** and prints the appropriate message.
- If an error occurs (e.g., no internet, site down), it **handles it without crashing**.
- The script **prompts the user before starting**, ensuring intentional execution.

---
This project helped me take a big step from basic Python scripts to **real-world automation**!

