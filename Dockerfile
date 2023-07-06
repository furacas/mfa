# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add current directory files (/app on your machine) to container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Set the path for the database file
ENV DB_PATH=sqlite:////data/mfa_data.db

# Create a data volume for database
VOLUME /data

# Run app.py when the container launches
CMD streamlit run MFA_Client.py
