#!/bin/bash

skyramp tester generate rest --api-schema openapi/contacts-openapi.yaml \
  --alias hubspot --address https://api.hubapi.com --port 443 \
  --path /crm/v3/objects/contacts \
  --sample-request files/sample-contact-create-request.json \
  --language python

