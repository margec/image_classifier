FROM public.ecr.aws/lambda/python:3.11

# Install dependencies
# COPY requirements.txt ${LAMBDA_TASK_ROOT}
# RUN pip install -r requirements.txt
RUN pip install sagemaker

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

# Command to run your Lambda function
CMD ["app.lambda_handler"]
