# Fleet Management API Documentation

A REST API for managing fleet operations including drivers, vehicles, packages, and routes. Built with Flask and PostgreSQL.

---

## Base URL

```
https://quanda.pathway4.click
```

---

## Tech Stack

- **Framework:** Flask 3.1.3
- **Database:** PostgreSQL (via psycopg2)
- **Python:** 3.x

---

## Database Schema

### Driver
| Column | Type | Constraints |
|---|---|---|
| `driver_id` | SERIAL | PRIMARY KEY |
| `name` | VARCHAR(250) | UNIQUE, NOT NULL |
| `license` | VARCHAR(50) | NOT NULL |

### Vehicle
| Column | Type | Constraints |
|---|---|---|
| `vehicle_id` | SERIAL | PRIMARY KEY |
| `license_plate` | VARCHAR(50) | UNIQUE, NOT NULL |
| `model` | VARCHAR(50) | NOT NULL |

### Packages
| Column | Type | Constraints |
|---|---|---|
| `packages_id` | SERIAL | PRIMARY KEY |
| `description` | VARCHAR(250) | UNIQUE, NOT NULL |
| `weight` | NUMERIC | NOT NULL |

### Routes
| Column | Type | Constraints |
|---|---|---|
| `routes_id` | SERIAL | PRIMARY KEY |
| `date` | DATE | UNIQUE, NOT NULL |
| `service_zone` | VARCHAR(250) | NOT NULL |

---

## Endpoints

### Health Check

#### `GET /`

Returns server status.

**Response**
```json
{
  "message": "Server Online"
}
```

---

## Drivers

Base path: `/driver`

### `GET /driver/`

Returns a list of all drivers.

**Response `200 OK`**
```json
[
  {
    "driver_id": 1,
    "name": "John Doe",
    "license": "DL-123456"
  }
]
```

---

### `POST /driver/`

Creates a new driver.

**Request Body**
```json
{
  "driver_id": 1,
  "name": "John Doe",
  "license": "DL-123456"
}
```

| Field | Type | Required |
|---|---|---|
| `driver_id` | integer | Yes |
| `name` | string | Yes |
| `license` | string | Yes |

**Response `201 Created`**
```json
{
  "message": "Object Created"
}
```

---

### `PUT /driver/<id>`

Updates an existing driver by ID.

**Path Parameter**
| Parameter | Type | Description |
|---|---|---|
| `id` | integer | The driver's ID |

**Request Body**
```json
{
  "driver_id": 1,
  "name": "Jane Doe",
  "license": "DL-654321"
}
```

**Response `201`**
```json
{
  "message": "Object Updated"
}
```

---

### `DELETE /driver/<id>`

Deletes a driver by ID.

**Path Parameter**
| Parameter | Type | Description |
|---|---|---|
| `id` | integer | The driver's ID |

**Response `201`**
```json
{
  "message": "Object Deleted"
}
```

---

## Vehicles

Base path: `/vehicle`

> **Note:** The `GET /vehicle/` endpoint is currently missing the `@Vehicle.route` decorator in the source code and will not respond to requests.

### `GET /vehicle/`

Returns a list of all vehicles.

**Response `200 OK`**
```json
[
  {
    "vehicle_id": 1,
    "license_plate": "ABC-1234",
    "model": "Ford Transit"
  }
]
```

---

### `POST /vehicle/`

Creates a new vehicle.

**Request Body**
```json
{
  "vehicle_id": 1,
  "license_plate": "ABC-1234",
  "model": "Ford Transit"
}
```

| Field | Type | Required |
|---|---|---|
| `vehicle_id` | integer | Yes |
| `license_plate` | string | Yes |
| `model` | string | Yes |

**Response `201 Created`**
```json
{
  "message": "Object Created"
}
```

---

### `PUT /vehicle/<id>`

Updates an existing vehicle by ID.

**Path Parameter**
| Parameter | Type | Description |
|---|---|---|
| `id` | integer | The vehicle's ID |

**Request Body**
```json
{
  "vehicle_id": 1,
  "license_plate": "XYZ-9999",
  "model": "Mercedes Sprinter"
}
```

**Response `201`**
```json
{
  "message": "Object Updated"
}
```

---

### `DELETE /vehicle/<id>`

Deletes a vehicle by ID.

**Path Parameter**
| Parameter | Type | Description |
|---|---|---|
| `id` | integer | The vehicle's ID |

**Response `201`**
```json
{
  "message": "Object Deleted"
}
```

---

## Packages

Base path: `/packages`

### `GET /packages/`

Returns a list of all packages.

**Response `200 OK`**
```json
[
  {
    "packages_id": 1,
    "description": "Fragile electronics",
    "weight": 2.5
  }
]
```

---

### `POST /packages/`

Creates a new package.

**Request Body**
```json
{
  "packages_id": 1,
  "description": "Fragile electronics",
  "weight": 2.5
}
```

| Field | Type | Required |
|---|---|---|
| `packages_id` | integer | Yes |
| `description` | string | Yes |
| `weight` | number | Yes |

**Response `201 Created`**
```json
{
  "message": "Object Created"
}
```

---

### `PUT /packages/<id>`

Updates an existing package by ID.

**Path Parameter**
| Parameter | Type | Description |
|---|---|---|
| `id` | integer | The package's ID |

**Request Body**
```json
{
  "package_id": 1,
  "description": "Updated description",
  "weight": 3.0
}
```

> **Note:** The request body uses `package_id` (singular) rather than `packages_id`.

**Response `201`**
```json
{
  "message": "Object Updated"
}
```

---

### `DELETE /packages/<id>`

Deletes a package by ID.

**Path Parameter**
| Parameter | Type | Description |
|---|---|---|
| `id` | integer | The package's ID |

**Response `201`**
```json
{
  "message": "Object Deleted"
}
```

---

## Routes

Base path: `/routes`

### `GET /routes/`

Returns a list of all routes.

**Response `200 OK`**
```json
[
  {
    "routes_id": 1,
    "date": "2026-05-13",
    "service_zone": "Downtown"
  }
]
```

---

### `POST /routes/`

Creates a new route.

**Request Body**
```json
{
  "routes_id": 1,
  "date": "2026-05-13",
  "service_zone": "Downtown"
}
```

| Field | Type | Required |
|---|---|---|
| `routes_id` | integer | Yes |
| `date` | string (YYYY-MM-DD) | Yes |
| `service_zone` | string | Yes |

**Response `201 Created`**
```json
{
  "message": "Object Created"
}
```

---

### `PUT /routes/<id>`

Updates an existing route by ID.

**Path Parameter**
| Parameter | Type | Description |
|---|---|---|
| `id` | integer | The route's ID |

**Request Body**
```json
{
  "route_id": 1,
  "date": "2026-05-14",
  "service_zone": "Uptown"
}
```

> **Note:** The request body uses `route_id` (singular) rather than `routes_id`.

**Response `201`**
```json
{
  "message": "Object Updated"
}
```

---

### `DELETE /routes/<id>`

Deletes a route by ID.

**Path Parameter**
| Parameter | Type | Description |
|---|---|---|
| `id` | integer | The route's ID |

**Response `201`**
```json
{
  "message": "Object Deleted"
}
```

---

## Error Responses

All endpoints return a `500` status code on unexpected errors.

```json
{
  "message": "An unexpected error occurred: <error details>"
}
```

---

## Environment Variables

Create a `.env` file in the project root with the following variables:

| Variable | Description | Default |
|---|---|---|
| `DB_HOST` | PostgreSQL host | — |
| `DB_PORT` | PostgreSQL port | — |
| `DB_NAME` | Database name | — |
| `DB_USER` | Database user | — |
| `DB_PASSWORD` | Database password | — |
| `DB_SSLMODE` | SSL mode | `require` |

---

## Running the API

```bash
# Install dependencies
pip install -r requirements.txt

# Start the server
python app.py
```

The server runs on `https://quanda.pathway4.click` by default.

---

## Known Issues

- `GET /vehicle/` — The `@Vehicle.route("/")` decorator is missing in `vehicle.py`, so this endpoint is not registered and will return a 404.
- `PUT /packages/<id>` — The request body key is `package_id` (not `packages_id`), which is inconsistent with the other fields.
- `PUT /routes/<id>` — The request body key is `route_id` (not `routes_id`), which is inconsistent with the other fields.
