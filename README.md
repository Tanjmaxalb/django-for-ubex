# Overview

* [Installation](#installation)
* [Testing](#testing)
* [Usage](#usage)
* [Request examples using curl](#request-examples-using-curl)
    * [Create a vulnerability](#create-a-vulnerability)
    * [Print a vulnerability](#print-a-vulnerability)
* [API](#api)
    * [Softwares](#softwares)
        * [Get softwares](#get-softwares)
            * [Parameters](#parameters)
        * [Create a software](#create-a-software)
            * [Parameters](#parameters)
        * [Update a software](#update-a-software)
            * [Parameters](#parameters)
        * [Delete a software](#delete-a-software)
    * [Vulnerabilities](#vulnerabilities)
    * [Get vulnerabilities](#get-vulnerabilities)
        * [Parameters](#parameters)
    * [Create a vulnerability](#create-a-vulnerability)
        * [Parameters](#parameters)
    * [Update a vulnerability](#update-a-vulnerability)
        * [Parameters](#parameters)
    * [Delete a vulnerability](#delete-a-vulnerability)

# Installation

```bash
make build
```

# Testing

```bash
make test
```

# Usage

```bash
make run
```

Move to another tty screen

```
make migrate
make create-user-user
make print_token
```

# Request examples using curl

## Create a vulnerability
```bash
curl \
    --header "Content-Type: application/json" \
    --request POST \
    --data '{"name": "buffer overflow", "description": "description", "created_at": "2020-07-22T22:00:00Z", "updated_at": "2020-07-22T22:00:00Z"}' \
    -H "Authorization: Token $(make print_token)" \
    http://127.0.0.1:8080/api/vulnerabilities/Vulnerability
```

## Print a vulnerability

```bash
curl -H "Authorization: Token $(make print_token)" http://127.0.0.1:8080/api/vulnerabilities/Vulnerability
```

Output:
```
[{"id":1,"createdAt":"2020-07-23T04:40:58.407570+00:00","updatedAt":"2020-07-23T04:40:58.407617+00:00","created_at":"2020-07-23T04:40:58.407570Z","updated_at":"2020-07-23T04:40:58.407617Z","name":"buffer overflow","description":"description"}]
```

# API

## Softwares

### Get softwares

| | |
|-|-|
| URL | /api/softwares/Software |
| METHOD | GET |

#### Parameters

| Patameter | Description |
|-|-|
| limit | Limit the selection |
| order_by | Sort result by column |
| fields | Select all rows where the fields are equal set value |

### Create a software

| | |
|-|-|
| URL | /api/softwares/Software |
| METHOD | POST |

#### Parameters

| Patameter | Description |
|-|-|
| name | Name of the software |
| description | Description of the software |
| vulnerability | identificator of vulnerability |
| created_at | Date of the creation (YYYY-mm-ddTHH:MM:SSZ format) |
| updated_at | Date of the creation (YYYY-mm-ddTHH:MM:SSZ format) |

### Update a software

| | |
|-|-|
| URL | /api/softwares/Software/{id} |
| METHOD | PUT |

#### Parameters

| Patameter | Description |
|-|-|
| name | Name of the software |
| description | Description of the software |
| vulnerability | identificator of vulnerability |
| created_at | Date of the creation (YYYY-mm-ddTHH:MM:SSZ format) |
| updated_at | Date of the update (YYYY-mm-ddTHH:MM:SSZ format) |

### Delete a software

| | |
|-|-|
| URL | /api/softwares/Software/{id} |
| METHOD | DELETE |

## Vulnerabilities

### Get vulnerabilities

| | |
|-|-|
| URL | /api/vulnerabilities/Vulnerability |
| METHOD | GET |

#### Parameters

| Patameter | Description |
|-|-|
| limit | Limit the selection |
| order_by | Sort result by column |
| fields | Select all rows where the fields are equal set value |

### Create a vulnerability

| | |
|-|-|
| URL | /api/vulnerabilities/Vulnerability |
| METHOD | POST |

#### Parameters

| Patameter | Description |
|-|-|
| name | Name of the software |
| description | Description of the software |
| created_at | Date of the creation (YYYY-mm-ddTHH:MM:SSZ format) |
| updated_at | Date of the creation (YYYY-mm-ddTHH:MM:SSZ format) |

### Update a vulnerability

| | |
|-|-|
| URL | /api/vulnerabilities/Vulnerability/{id} |
| METHOD | PUT |

#### Parameters

| Patameter | Description |
|-|-|
| name | Name of the software |
| description | Description of the software |
| created_at | Date of the creation (YYYY-mm-ddTHH:MM:SSZ format) |
| updated_at | Date of the update (YYYY-mm-ddTHH:MM:SSZ format) |

### Delete a vulnerability

| | |
|-|-|
| URL | /api/vulnerabilities/Vulnerability/{id} |
| METHOD | DELETE |
