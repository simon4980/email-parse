# email-parse

Reads emails files downloaded into tmp/email-download.  Parses and stores the To, From, Date, Subject and Message-ID into a dynamodb table (email_data).

AWS Region: us-east-1

Builds docker container with docker-compose

docker-compose up

docker-compose run -e AWS_ACCESS_KEY_ID=[Key] -e AWS_SECRET_ACCESS_KEY=[Secret] app bash

docker-compose down

