FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the test files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Run API tests
CMD ["sh", "-c", "pytest -v -m 'api'"]
