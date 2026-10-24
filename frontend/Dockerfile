FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# copy ONLY the requirements file
COPY requirements.txt .

# Docker caches this layer! As long as requirements.txt hasn't changed,
# Docker completely skips this 1-2 minute install process during a rebuild.
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy all files from the current directory to the container's working directory
COPY . .

# install Python dependencies listed in requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Define the command to run the Streamlit app on port 8501 and make it accessible externally
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableXsrfProtection=false"]
