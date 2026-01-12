FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Copy project files
COPY pyproject.toml poetry.lock* ./
COPY highbar ./highbar
COPY README.md ./

# Configure Poetry to not create virtual environment in container
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-interaction --no-ansi --no-dev

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Create data directories
RUN mkdir -p /app/data /app/results /app/scores

# Expose port for potential web services
EXPOSE 8000

# Set entrypoint
ENTRYPOINT ["highbar"]
CMD ["--help"]
