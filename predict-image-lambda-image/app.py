import json
import base64
import sagemaker
from sagemaker.serializers import IdentitySerializer
from sagemaker.predictor import Predictor

# Fill this in with the name of your deployed model
ENDPOINT = 'image-classification-2024-11-01-02-47-23-556' ## TODO: fill in

def lambda_handler(event, context):
    print("Hit container lambda_handler...")
    # Decode the image data    
    image_data = event['image_data']
    image = base64.b64decode(image_data) ## TODO: fill in
    print("base64 decoded image data!")

    # Instantiate a Predictor
    predictor = Predictor(ENDPOINT) ## TODO: fill in
    print("Instantiated Predictor!")

    # For this model the IdentitySerializer needs to be "image/png"
    predictor.serializer = IdentitySerializer("image/png")
    print("Set predictor serializer!")

    # Make a prediction:
    inferences = predictor.predict(image) ## TODO: fill in
    print("Got inferences!")
    print(inferences)

    # We return the data back to the Step Function    
    event["inferences"] = inferences.decode('utf-8')

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
