### Simple API servers

This repository contains simple hello server implementation (parse JSON and return JSON) in various programming languages.


```
$ curl -X POST -d '{"name": "John"}' http://localhost:8080/api
{"message": "Hello John!"}
```

### integration test

Test code is written in Python and still in progress

```
python tests/test_echo_servers.py
```