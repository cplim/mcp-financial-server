# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Create a non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Install uv
RUN pip install uv

# Copy the project definition file
COPY pyproject.toml ./

# Install dependencies
RUN uv pip sync pyproject.toml

# Copy the rest of the application code and set permissions
COPY --chown=appuser:appuser . .

# Switch to the non-root user
USER appuser

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
