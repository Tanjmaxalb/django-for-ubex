## Installation

```bash
make build
```

## Testing

```bash
make test
```

## Usage

```bash
make run
```

Move to another tty screen

```
make migrate
make create-user-user
make print_token
```

### Requests

#### Create a vulnerability
```bash
curl \
    --header "Content-Type: application/json" \
    --request POST \
    --data '{"name": "buffer overflow", "description": "description", "created_at": "2020-07-22T22:00:00Z", "updated_at": "2020-07-22T22:00:00Z"}' \
    -H "Authorization: Token $(make print_token)" \
    http://127.0.0.1:8080/api/vulnerabilities/Vulnerability
```

#### Print a vulnerability

```bash
curl -H "Authorization: Token $(make print_token)" http://127.0.0.1:8080/api/vulnerabilities/Vulnerability
```

Output:
```
[{"id":1,"createdAt":"2020-07-23T04:40:58.407570+00:00","updatedAt":"2020-07-23T04:40:58.407617+00:00","created_at":"2020-07-23T04:40:58.407570Z","updated_at":"2020-07-23T04:40:58.407617Z","name":"buffer overflow","description":"description"}]
```
