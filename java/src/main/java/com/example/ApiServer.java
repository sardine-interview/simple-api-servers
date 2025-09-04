package com.example;

import io.javalin.Javalin;

public class ApiServer {
    
    public static class HelloRequest {
        public String name;
    }
    
    public static class HelloResponse {
        public String message;
        
        public HelloResponse(String message) {
            this.message = message;
        }
    }

    public static void main(String[] args) {
        Javalin app = Javalin.create()
            .post("/api", ctx -> {
                HelloRequest request = ctx.bodyAsClass(HelloRequest.class);
                HelloResponse response = new HelloResponse("Hello " + request.name + "!");
                ctx.json(response);
            })
            .start(8080);
            
        System.out.println("Server is running on port 8080");
    }
}