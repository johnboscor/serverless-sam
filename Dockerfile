FROM public.ecr.aws/lambda/python:3.8

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

# Copy all relevant app files
COPY ./myapp ./myapp

# Expose port 8000 in Docker and forward to localhost:80
EXPOSE 80:8000

# Run the API when container starts
CMD ["myapp.main.handler"]

