FROM python:3.10.2-slim
#FROM dashboardmultimedia


# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install Setuptools
#RUN pip install mysqlclient
RUN python3 --version
RUN pip list
RUN pip install opencv-python-headless
RUN pip install --no-cache-dir -r requirements.txt


# Expose port 5000 for Flask app
EXPOSE 5000

# Run the Flask app
CMD ["python3", "main.py"]
