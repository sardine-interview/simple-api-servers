### Simple API servers

This repository contains simple hello server implementation (parse JSON and return JSON) in various programming languages.


```
$ curl -X POST -d '{"name": "John"}' http://localhost:8080/api
{"message": "Hello John!"}
```

### Fibonacci

All servers expose the same intentionally slow endpoint:

```
GET /fibonacci?n=10
```

`n` is 0-indexed and must be an integer between 0 and 50.

```
$ curl 'http://localhost:8080/fibonacci?n=10'
{"n":10,"result":55}
```

Invalid input returns HTTP 400:

```
$ curl -i 'http://localhost:8080/fibonacci?n=51'
HTTP/1.1 400 Bad Request
...
{"error":"n must be an integer between 0 and 50"}
```

Servers run on different ports: Go and Java on 8080, Node.js on 3000, and Python on 8000.

### integration test

Test code is written in Python and still in progress

```
python tests/test_echo_servers.py
```