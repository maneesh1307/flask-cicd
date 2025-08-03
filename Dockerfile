# Use slim Python base image
FROM python:3.10-slim

LABEL maintainer="DigiLocker"
LABEL version="1.0"
ENV TZ="Asia/Kolkata"

# Set working directory inside the container
WORKDIR /app

# Copy only your main Flask app (adjust if using other files)
COPY src_code/app.py /app/

# Install pip packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir flask flask-cors gunicorn

# Expose the port Gunicorn will use
EXPOSE 5001

# Run the app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]
