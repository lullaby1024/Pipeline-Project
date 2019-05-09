import boto3

def detect_labels(bucket="recipecialist", key="test.jpg", region="us-east-1"):

    rekognition = boto3.client("rekognition", region)
    response = rekognition.detect_labels(
        Image={
            "S3Object": {
                "Bucket": bucket,
				"Name": key,
            }
        },
		# MaxLabels=max_labels,
		# MinConfidence=min_confidence,
	)
    labs = []
    confid = []

    for label in response['Labels']:
        labs.append(label['Name'])
        confid.append(label['Confidence'])

    # for label in response['Labels']:
    #     print("{Name} - {Confidence}%".format(**label))

    # return response['Labels']
    return dict(zip(labs, confid))


