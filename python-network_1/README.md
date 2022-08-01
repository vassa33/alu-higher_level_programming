# PYTHON -Network #1
## Mandatory Tasks
### 0-hbtn_status.py
* Script fetches https://intranet.hbtn.io/status
* Usage: `./0-hbtn_status.py`
* Output:
```
Body response:
    - type: <class 'bytes'>
    - content: b'OK'
    - utf8 content: OK
```

### 1-hbtn_header.py
* Script takes URL, sends a request to URL, and display value of `X-Request-Id` variable from header of response
* Usage: `./1-hbtn_header.py URL`

### 2-post_email.py
* Sends a `POST` request to the URL passed into script with email passed as parameter, prints body of response
* Usage: `./2-post_email.py URL email`

### 3-error_code.py
* Print error code in `utf-8`
* Usage: `./3-error_code.py URL`

### 4-hbtn_status.py
* Use package requests to fetch https://intranet.hbtn.io/status
* Usage: `4-hbtn_status.py`
* Output:
```
Body response:
    - type: <class 'str'>
    - content: OK
```

### 5-hbtn_header.py
* Sends request to given URL and display value of `X-Request-Id` in header
* Usage: `./5-hbtn_header.py URL`

### 6-post_email.py
* Sends a POST request to passed URL with email as parameter and displays body of response
* Usage: `./6-post_email.py URL email`

### 7-error_code.py
* Send request to given URL and display body of response
* Usage: `./7-error_code.py URL`

### 8-json_api.py
* Takes a letter and post request to `http://0.0.0.0:5000/search_user`
* Usage: `./8-json_api.py letter`
* Output: `[id] name`
  * `Not a valid JSON` if JSON is invalid
  * `No result` if JSON is empty

### 10-my_github.py
* Script takes Github credentials (username and password) and uses the [Github API](https://developer.github.com/v3/users/#get-the-authenticated-user) to display id
* Usage: `./10-my_github.py username password`
* Output: User's id or None


## Advanced Tasks
### 100-github_commits.py
* Takes two arguments to send a request to the Github API to get 10 commits
* Usage: `./100-github_commits repository_name owner_name`
