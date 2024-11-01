import json

THRESHOLD = .93

def lambda_handler(event, context):
    
    # Grab the inferences from the event
    body = json.loads(event['body'])
    print(body)
    inferences = json.loads(body['inferences']) ## TODO: fill in
    print(inferences)
    
    # Check if any values in our inferences are above THRESHOLD
    bike_prob = float(inferences[0])
    print(f"Bicycle probability: {bike_prob}")
    motorcycle_prob = float(inferences[1])
    print(f"Motorcycle probability: {motorcycle_prob}")
    meets_threshold = False ## TODO: fill in
    if bike_prob >= THRESHOLD or motorcycle_prob >= THRESHOLD:
        meets_threshold = True
        print(f"One probability has met our confidence threshold {THRESHOLD}")
    else:
        print(f"No probability has met our confidence threshold {THRESHOLD}")
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': { 'inferences': inferences, 'threshold': THRESHOLD, 'meets_threshold': meets_threshold }
    }
