package com.example;

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

    @PostMapping("/api")
    public HelloResponse hello(@RequestBody HelloRequest request) {
        return new HelloResponse("Hello " + request.name + "!");
    }
}