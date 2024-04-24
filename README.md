# AuthSys

![GitHub stars](https://img.shields.io/github/stars/IceBytes/AuthSys?style=social)
![GitHub followers](https://img.shields.io/github/followers/IceBytes?style=social)

## Introduction
AuthSys is a Python library for Memberships system.

## Installation
You can install AuthSys using pip:
```bash
pip install AuthSys
```

## Usage

### Initialization
```python
from AuthSys import AuthSys

auth = AuthSys()
```

### Login
```python
# Logging in with a key and access token
response = auth.login(key="your_key", access_token="your_access_token")
print(response)
```

### Registration
```python
# Registering a new user
response = auth.register(time="registration_time")
print(response)
```

### Removing a user
```python
# Removing a user using their key and authentication secret
response = auth.remove(key="user_key", secret_auth="user_secret_auth")
print(response)
```

### Editing user information
```python
# Editing user information
response = auth.edit(key="user_key", auth="user_auth", time="new_time")
print(response)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
```