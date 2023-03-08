# First stage: Build the application
FROM python:3.10.10-slim-buster

# Install dependencies
RUN apt-get update && apt-get install -y build-essential

# Copy application files
COPY app.py /app/

# Install application dependencies
WORKDIR /app
RUN pip install fastapi uvicorn

# Add .local/bin to PATH
ENV PATH=/root/.local/bin:$PATH

# Expose the application port
EXPOSE 8000

# Start the application using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]