# 🧩 Broken Link Validator

A lightweight, multi-threaded Python tool for validating and classifying large batches of URLs from Excel files.  

This project automates the process of checking whether URLs in datasets are working, redirected, blocked, or broken — ideal for **data validation**, **media monitoring**, or **web scraping quality checks**.  

## 🚀 Features
- ✅ Bulk validation of URLs from Excel files  
- ⚡ Multi-threaded processing for faster execution  
- 🧠 Automatic classification:  
  - Working (Status 200)  
  - Redirected but Working (301/302)  
  - Blocked (403 Forbidden)  
  - Not Working (timeout or error)  
- 📊 Excel export with added status column  
- 🧾 Customizable & reproducible  

**Input:** Excel file containing a URL column

**Output:** Excel file with a new column Status showing each link’s result

## 💻 Usage
```bash
pip install pandas requests openpyxl
python broken_links.py
```

Example Output:
![Broken Link Validator Output](images/broken_link_output.png)

## ERROR description

- If response.status_code == 200, then the URL is considered "Working" in your script.
- 301 Moved Permanently → The URL has changed permanently, and future requests should use the new URL.
- 302 Found (Temporary Redirect): The resource is temporarily moved to another location.
- HTTP 403 (Forbidden) → "Blocked (403 Forbidden)"

**Possible causes:**
- Website blocks automated requests (bot protection).
- Missing authentication or permission.
- IP restrictions.
- 404 Not Found -> The requested URL does not exist.
- 500 Internal Server Error -> The server encountered an error.
- 405 Method Not Allowed -> The request method is not supported by the server.
- 503 Service Unavailable -> The server is down or overloaded.