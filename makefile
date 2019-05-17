build: test
	go build audiotowav.go

test:
	go test ./...

sanitize:
	go fmt ./...
	go vet ./...

clean:
	rm -f audiotowav
