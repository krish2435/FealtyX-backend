#FealtyX-Backend

This FastAPI project is designed to provide an API for managing students data and integrating with the LLaMA model. The project includes endpoints for processing requests and interacting with AI model for data summarization

This README outlines the setup process, running the project locally, and instructions for installing OLLAMA and downloading the LLaMA model.


## Requirements

- Python 3.7+
- [FastAPI](https://fastapi.tiangolo.com/)
- [OLLAMA](https://github.com/jmorganca/ollama) for working with the LLaMA 3.2 model
- Additional dependencies specified in `requirements.txt`

## Setup Instructions

To set up and run the project, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-project-name.git
cd your-project-name
```

### 2. Set Up a Virtual Environment (Recommended)

**Using Python's venv module:**

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

**Using Conda:**

```bash
conda create -n your_env_name python=3.7
conda activate your_env_name
```

### 3. Install Dependencies

Navigate to the project directory and install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Install OLLAMA

To download and install OLLAMA, visit the [OLLAMA GitHub repository](https://github.com/jmorganca/ollama) and follow the installation instructions for your operating system.

### 5. Pull the LLaMA Model

Once OLLAMA is installed, download the LLaMA 3.2 model by running:

```bash
ollama pull llama3.2:1b
```

This command downloads the 1-billion parameter version of the LLaMA 3.2 model.

### 6. Run the FastAPI Application

Launch the FastAPI application with:

```bash
uvicorn main:app --reload
```

Here:
- `main` is the primary Python file containing the FastAPI instance (`app`).
- `--reload` enables auto-reload for development.

The API will be accessible at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### 7. Access API Documentation

FastAPI offers interactive API documentation at:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Project Structure

Below is a basic overview of the project layout:

```
your-project-name/
│
├── app/
│   ├── main.py           # Main application file
│   ├── routers/          # Endpoint organization (optional)
│   ├── models/           # Database models
│   ├── schemas/          # Pydantic models for request/response schemas
│   └── services/         # Business logic layer
│
├── requirements.txt      # Dependencies file
└── README.md             # Project documentation
```

This guide should help you get started with setting up and running the project locally.
