FROM python:3.9-slim

# set the working directory inside the container
WORKDIR /app

# copy ONLY the requirements file
COPY requirements.txt .

# Docker caches this layer! As long as requirements.txt hasn't changed,
# Docker completely skips this 1-2 minute install process during a rebuild.
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy all files from the current directory to the container's working directory
COPY . .

# Define the command to start the application using Gunicorn with 4 worker processes
# - `-w 4`: Uses 4 worker processes for handling requests
# - `-b 0.0.0.0:7860`: Binds the server to port 7860 on all network interfaces
# - `app:app`: Runs the Flask app (assuming `app.py` contains the Flask instance named `app`)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:7860", "app:superkart_api"]
