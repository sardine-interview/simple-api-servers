# Java Simple API Server

A minimal REST API server using Spring Boot framework.

## Usage

### Using Makefile (recommended)

```bash
# Install dependencies
make install

# Compile and run
make run

# Just compile
make compile

# Test the API
make test

# Clean compiled files
make clean
```

### Manual commands

```bash
# Install dependencies
mvn dependency:resolve

# Compile
mvn compile

# Run
mvn spring-boot:run
```

## API

- **POST** `/api` - Accepts JSON with `name` field, returns greeting message

### Example

```bash
curl -X POST -d '{"name": "John"}' -H "Content-Type: application/json" http://localhost:8080/api
# Returns: {"message": "Hello John!"}
```

## Dependencies

- Spring Boot 3.2.3 (web framework)
- Spring Boot Starter Web (includes embedded Tomcat and Jackson)