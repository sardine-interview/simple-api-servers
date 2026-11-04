package com.example;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
public class ApiController {

    public static class HelloRequest {
        public String name;
    }

    public static class HelloResponse {
        public String message;

        public HelloResponse(String message) {
            this.message = message;
        }
    }

    public static class FibonacciResponse {
        public int n;
        public long result;

        public FibonacciResponse(int n, long result) {
            this.n = n;
            this.result = result;
        }
    }

    public static class ErrorResponse {
        public String error;

        public ErrorResponse(String error) {
            this.error = error;
        }
    }

    @PostMapping("/api")
    public HelloResponse hello(@RequestBody HelloRequest request) {
        return new HelloResponse("Hello " + request.name + "!");
    }

    @GetMapping("/fibonacci")
    public ResponseEntity<?> fibonacci(@RequestParam(required = false) String n) {
        Integer number = null;
        try {
            number = n == null ? null : Integer.parseInt(n);
        } catch (NumberFormatException ignored) {
            // handled by the validation below
        }

        if (number == null || number < 0 || number > 50) {
            return ResponseEntity.badRequest()
                    .body(new ErrorResponse("n must be an integer between 0 and 50"));
        }

        return ResponseEntity.ok(new FibonacciResponse(number, computeFibonacci(number)));
    }

// This is slow on purpose, don't change it
    private long computeFibonacci(int n) {
        if (n < 2) {
            return n;
        }
        return computeFibonacci(n - 1) + computeFibonacci(n - 2);
    }
}
