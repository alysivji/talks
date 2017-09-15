# Use latest Python runtime as a parent image
FROM python:3.6.2-slim

# Meta-data
LABEL maintainer="Aly Sivji <alysivji@gmail.com>" \
      description="Docker Data Science Workflow #4: Data Science API\
      This image contains a pickled version of the predictive model\
      that can be accessed using a REST API (created in Flask).\
      Fitting and pickling was done at another point in the process"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# pip install
RUN pip --no-cache-dir install -r /app/requirements.txt

# Make port available to the world outside this container
EXPOSE 5000

# ENTRYPOINT allows us to specify the default executible. CMD sets default 
# arguments to that executable which may be overwritten when using docker run
ENTRYPOINT ["python"]
CMD ["app.py"]
