package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"strconv"
)

type HelloRequest struct {
	Name string `json:"name"`
}

type HelloResponse struct {
	Message string `json:"message"`
}

type FibonacciResponse struct {
	N      int   `json:"n"`
	Result int64 `json:"result"`
}

type ErrorResponse struct {
	Error string `json:"error"`
}

// This is slow on purpose, don't change it
func fibonacci(n int) int64 {
	if n < 2 {
		return int64(n)
	}
	return fibonacci(n-1) + fibonacci(n-2)
}

func writeJSON(w http.ResponseWriter, status int, payload any) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	json.NewEncoder(w).Encode(payload)
}

func main() {
	http.HandleFunc("/api", func(w http.ResponseWriter, r *http.Request) {
		body, err := io.ReadAll(r.Body)
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		var request HelloRequest
		err = json.Unmarshal(body, &request)
		if err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		}
		response := HelloResponse{Message: fmt.Sprintf("Hello %s!", request.Name)}
		json.NewEncoder(w).Encode(response)
	})

	http.HandleFunc("GET /fibonacci", func(w http.ResponseWriter, r *http.Request) {
		n, err := strconv.Atoi(r.URL.Query().Get("n"))
		if err != nil || n < 0 || n > 50 {
			writeJSON(w, http.StatusBadRequest, ErrorResponse{Error: "n must be an integer between 0 and 50"})
			return
		}
		writeJSON(w, http.StatusOK, FibonacciResponse{N: n, Result: fibonacci(n)})
	})

	fmt.Println("Server is running on port 8080")
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		fmt.Println("Error starting server:", err)
	}
}
