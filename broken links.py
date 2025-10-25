#!/usr/bin/env python
# coding: utf-8

# **Broken Link Validator**
# 
# **Description:** Checks the validity of URLs in Excel files and classifies them as Working, Redirected, Blocked, or Not working.

# In[29]:


#!pip install requests


# In[30]:


import os  
import pandas as pd  
import requests
from concurrent.futures import ThreadPoolExecutor


# In[31]:


os.chdir(r"C:/Users/mmaha/projects/broken links")


# In[32]:


#os.getcwd()
print(os.listdir())


# In[33]:


df = pd.read_excel("data/check url status.xls")


# In[34]:


df.tail()


# In[35]:


# Function to check URL status
def check_url(URL):
    try:
        response = requests.get(URL, allow_redirects=True, timeout=10)
        if response.status_code == 200:
            return "Working"
        elif response.status_code in [301, 302]:  
            return "Redirected but Working"
        elif response.status_code == 403:  
            return "Blocked (403 Forbidden)"
        else:
            return f"Not Working ({response.status_code})"
    except requests.RequestException as e:
        return f"Not Working ({str(e)})"

# Apply ThreadPoolExecutor for faster execution
with ThreadPoolExecutor(max_workers=10) as executor:
    df['Status'] = list(executor.map(check_url, df['URL']))

# Export to Excel
df.to_excel("data/url_status.xlsx", index=False)

# Print the DataFrame
df


# **ERROR description**
# 
# If response.status_code == 200, then the URL is considered "Working" in your script.
# 
# 301 Moved Permanently → The URL has changed permanently, and future requests should use the new URL.
# 
# 302 Found (Temporary Redirect): The resource is temporarily moved to another location.
# 
# HTTP 403 (Forbidden) → "Blocked (403 Forbidden)"
# - Possible causes:
# - Website blocks automated requests (bot protection).
# - Missing authentication or permission.
# - IP restrictions.
# 
# 404 Not Found -> The requested URL does not exist.
#   
# 500 Internal Server Error -> The server encountered an error.
# 
# 405 Method Not Allowed -> The request method is not supported by the server.
# 
# 503 Service Unavailable -> The server is down or overloaded.
# 
