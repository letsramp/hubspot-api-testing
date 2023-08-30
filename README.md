# HubSpot API Testing with Skyramp

This repository contains Skyramp configurations for mocking [HubSpot APIs](https://developers.hubspot.com/docs/api/overview). To learn more about what Skyramp does, how it works, and how it improves the software testing experience, refer to the [Skyramp documentation](https://www.skyramp.dev/docs/).

## Overview

The `mocks/` directory contains generated Skyramp configurations to mock HubSpot APIs. This enables you to test applications that are dependent on HubSpot without actually needing the live HubSpot service. More information on generating mocks can be found below. Integration with OpenAI helps us produce realistic static mock responses (rather than being pseudo-random or limited pre-defined values). For example, a property like names will get realistic sounding names (such as `Jane Doe`).

The `openapi/` directory contains a few sample OpenAPI files shared by HubSpot. These files are required in the Skyramp mock configuration generation. They allow the Skyramp CLI tool to understand the structure of the HubSpot API requests/responses so mock values can be accurate.

## Generating the Mocks

There are three OpenAPI files in the `openapi/` directory. Skyramp mock configurations were generated for each of them using the `mocker` component of the Skyramp TestKit. For more information on `mocker`, refer to the [Mocker documentation](https://www.skyramp.dev/docs/testkit/mocker/).

For each of the three referenced OpenAPI files below, the `skyramp mocker` command that follows was used to generate the mock descriptions. For specific information on what these parameters refer to and what they are used for, refer to the [documentation for generating a mock](https://www.skyramp.dev/docs/testkit/mocker/#2-generate-a-mock).

### Site Search
https://api.hubspot.com/api-catalog-public/v1/apis/cms/v3/site-search   
```
skyramp mocker generate --alias cms-site-search --port 80 --protocol openapi --openai --api-schema openapi/cms-sites-search-openapi.yaml
```

### Contacts
https://api.hubspot.com/api-catalog-public/v1/apis/crm/v3/objects/contacts   
```
skyramp mocker generate --alias cms-contacts-service --port 80 --protocol openapi --openai --api-schema openapi/contacts-openapi.yaml
```

### Associations
https://api.hubspot.com/api-catalog-public/v1/apis/crm/v4/associations   
```
skyramp mocker generate --alias cms-association-service --port 80 --protocol openapi --openai --api-schema openapi/associations-openapi.yaml
```
