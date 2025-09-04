.PHONY: install compile run clean test

install:
	mvn dependency:resolve

compile: install
	mvn compile

run: compile
	mvn exec:java -Dexec.mainClass="com.example.ApiServer"

clean:
	mvn clean

test:
	curl -X POST -d '{"name": "John"}' -H "Content-Type: application/json" http://localhost:8080/api