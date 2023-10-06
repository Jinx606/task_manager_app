# Use the PyPy base image
FROM pypy:latest

# Set the working directory inside the container
WORKDIR /app

# Copy your Python script and data files into the container
COPY task_manager.py /app/
COPY task_overview.txt /app/
COPY tasks.txt /app/
COPY user.txt /app/

# Install any Python dependencies (if you have any)
RUN pip install datetime

# Set the command to run your Python script
CMD ["pypy3", "task_manager.py"]
