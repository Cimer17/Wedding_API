# Wedding API

A FastAPI-based backend service for managing wedding guest information and related functionality.

## Features

- RESTful API endpoints for managing wedding guests
- SQLAlchemy ORM for database operations
- Pydantic models for data validation
- CORS middleware enabled for cross-origin requests
- Docker support for containerization

## Project Structure

```
Wedding_API/
├── api/           # API routes and endpoints
├── crud/          # Database CRUD operations
├── data/          # Data files and resources
├── db/            # Database configuration and initialization
├── models/        # SQLAlchemy models
├── schemas/       # Pydantic schemas
├── utils/         # Utility functions
├── app.py         # Main application file
├── Dockerfile     # Docker configuration
└── requirements.txt # Project dependencies
```

## Prerequisites

- Python 3.8+
- Docker (optional)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Wedding_API
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Local Development

1. Start the FastAPI server:
```bash
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`

### Using Docker

1. Build the Docker image:
```bash
docker build -t wedding-api .
```

2. Run the container:
```bash
docker run -p 8000:8000 wedding-api
```

## API Documentation

Once the server is running, you can access:
- Swagger UI documentation: `http://localhost:8000/docs`
- ReDoc documentation: `http://localhost:8000/redoc`

## API Endpoints

- `GET /api/users` - Get all guests
- `POST /api/users` - Create a new guest
- `GET /api/users/{id}` - Get a specific guest
- `PUT /api/users/{id}` - Update a guest
- `DELETE /api/users/{id}` - Delete a guest

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
