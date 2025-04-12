package main

import (
	"fmt"
	"io"
	"net/http"
)

func main() {
	http.HandleFunc("/echo", func(w http.ResponseWriter, r *http.Request) {
		body, err := io.ReadAll(r.Body)
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		w.Write(body)
	})
	fmt.Println("Server is running on port 8080")
	http.ListenAndServe(":8080", nil)
}
