# Use the official Python image based on Ubuntu 20.04
FROM python:3.8-slim-buster as base

# Prevent Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Avoid Python buffering to see logs immediately.
ENV PYTHONUNBUFFERED=1

WORKDIR /

# Create a non-privileged user for running the app.
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Install system dependencies (e.g., required for MySQL client libraries)
RUN apt-get update && apt-get install -y \
    libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the source code into the container.
COPY . .

# Download Python dependencies using pip, leveraging caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

# Switch to the non-privileged user to run the application.
USER appuser

# Expose the port that the application listens on (if needed).
# Replace with the actual port your application listens on.
# EXPOSE 8000

# Run the application. Replace with your specific command.
# For example, if you want to run a Python script:
CMD ["python", "0-select_states.py", "root", "root", "hbtn_0e_0_usa"]

