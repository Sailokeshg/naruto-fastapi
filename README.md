
## Setting Up Development Environment

### Install Python > 3.7

```shell
sudo apt-get install python3.8
```

### Check version

```shell
python --version
```

### Install PIP

```shell
sudo apt install python3-pip
```

### Install  the requirements

```shell
pip install -r requirements.txt
```

### Run the uvicorn server

To run the server , move the index to `app` directory .

```shell
uvicorn main:app --reload
```
If the above run command didn't work , proceed with this

```shell
python3 -m uvicorn main:app --reload
```

### To access the API's and documentation

Go to any of the following addresses in the browser

  -  http://127.0.0.1:8000/docs
  -  http://127.0.0.1:8000/redoc

This app is deployed on Deta and api's can be accessed at https://q5rwi9.deta.dev/docs
