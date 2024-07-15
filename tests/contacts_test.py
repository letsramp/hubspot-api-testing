import skyramp

# Initialize Endpoint(s)
contacts_endpoint = skyramp.RestEndpoint(
    name="hubspot",
    port=443,
    rest_path="/crm/v3/objects/contacts"
)
contacts_contactId_endpoint = skyramp.RestEndpoint(
    name="hubspot",
    port=443,
    rest_path="/crm/v3/objects/contacts/{contactId}"
)

# Create JSON Payload Constants
contacts_request_data = r'''{
  "properties": {
    "email": "bcooper@biglytics.net",
    "phone": "(877) 929-0687",
    "company": "Biglytics",
    "website": "biglytics.net",
    "lastname": "Cooper",
    "firstname": "Bryan"
  },
  "associations": []
}
'''
contacts_contactId_request_data = r'''{
  "associations": [],
  "properties": {
    "company": "Biglytics",
    "email": "bcooper@biglytics.net",
    "firstname": "Bryan",
    "lastname": "Cooper",
    "phone": "(877) 929-0687",
    "website": "biglytics.net"
  }
}'''

# Define Requests
contacts_GET_request = skyramp.Request(
    name="contacts_GET",
    method_name="GET",
    endpoint_descriptor=contacts_endpoint,
    vars_={"after":"","archived":False,"associations":[""],"limit":10,"properties":[""],"propertiesWithHistory":[""]},
    params=[
        skyramp.RestParam(name="limit", in_="query", value="vars.limit"),
        skyramp.RestParam(name="after", in_="query", value="vars.after"),
        skyramp.RestParam(name="properties", in_="query", value="vars.properties"),
        skyramp.RestParam(name="propertiesWithHistory", in_="query", value="vars.propertiesWithHistory"),
        skyramp.RestParam(name="associations", in_="query", value="vars.associations"),
        skyramp.RestParam(name="archived", in_="query", value="vars.archived")
    ]
)
contacts_POST_request = skyramp.Request(
    name="contacts_POST",
    method_name="POST",
    endpoint_descriptor=contacts_endpoint,
    vars_={},
    blob=contacts_request_data
)
contacts_contactId_GET_request = skyramp.Request(
    name="contacts_contactId_GET",
    method_name="GET",
    endpoint_descriptor=contacts_contactId_endpoint,
    vars_={"archived":False,"associations":[""],"contactId":"","properties":[""],"propertiesWithHistory":[""]},
    params=[
        skyramp.RestParam(name="contactId", in_="path", value="vars.contactId"),
        skyramp.RestParam(name="properties", in_="query", value="vars.properties"),
        skyramp.RestParam(name="propertiesWithHistory", in_="query", value="vars.propertiesWithHistory"),
        skyramp.RestParam(name="associations", in_="query", value="vars.associations"),
        skyramp.RestParam(name="archived", in_="query", value="vars.archived"),
    ]
)
contacts_contactId_DELETE_request = skyramp.Request(
    name="contacts_contactId_DELETE",
    method_name="DELETE",
    endpoint_descriptor=contacts_contactId_endpoint,
    vars_={"contactId":""},
    params=[
        skyramp.RestParam(name="contactId", in_="path", value="vars.contactId"),
    ]
)
contacts_contactId_PATCH_request = skyramp.Request(
    name="contacts_contactId_PATCH",
    method_name="PATCH",
    endpoint_descriptor=contacts_contactId_endpoint,
    vars_={"contactId":""},
    params=[
        skyramp.RestParam(name="contactId", in_="path", value="vars.contactId"),
    ],
    blob=contacts_contactId_request_data
)

# Define Scenarios
def add_contacts_functional_scenario():
    scenario = skyramp.Scenario(
        "contacts_functional_scenario",
        ignore=False
    )
		#   # Endpoint /crm/v3/objects/contacts and Method POST
		#   scenario.add_request_v1(
		#       request=contacts_POST_request,
		#       step_name="contacts_functional_scenario-0",
		#       description="Endpoint /crm/v3/objects/contacts and Method POST"
		#   )
		#   # Assert of scenario step contacts_functional_scenario-0 - Endpoint /crm/v3/objects/contacts and Method POST
		#   scenario.add_assert_v1(
		#       assert_value="requests.contacts_POST.code",
		# assert_expected_value="201", 
		#       assert_step_name="contacts_functional_scenario-1",
		#       description="Assert of scenario step contacts_functional_scenario-0 - Endpoint /crm/v3/objects/contacts and Method POST"
		#   )
    # Endpoint /crm/v3/objects/contacts and Method GET
    scenario.add_request_v1(
        request=contacts_GET_request,
        step_name="contacts_functional_scenario-2",
        vars_override={"after":"","archived":False,"associations":[""],"limit":10,"properties":[""],"propertiesWithHistory":[""]},
        description="Endpoint /crm/v3/objects/contacts and Method GET"
    )
    # Assert of scenario step contacts_functional_scenario-2 - Endpoint /crm/v3/objects/contacts and Method GET
    scenario.add_assert_v1(
        assert_value="requests.contacts_GET.code",
        assert_expected_value="200", 
        assert_step_name="contacts_functional_scenario-3",
        description="Assert of scenario step contacts_functional_scenario-2 - Endpoint /crm/v3/objects/contacts and Method GET"
    )
    # Endpoint /crm/v3/objects/contacts/{contactId} and Method GET
    scenario.add_request_v1(
        request=contacts_contactId_GET_request,
        step_name="contacts_functional_scenario-4",
        vars_override={"archived":False,"associations":[""],"properties":[""],"propertiesWithHistory":[""]},
        description="Endpoint /crm/v3/objects/contacts/{contactId} and Method GET",
        max_retries=5,
        interval="1s",
        until="code == 200"
    )
    scenario.add_assert_v1(
        assert_value="requests.contacts_contactId_GET.code",
        assert_expected_value="200", 
        assert_step_name="contacts_functional_scenario-5",
        description="Assert of scenario step contacts_functional_scenario-4 - Endpoint /crm/v3/objects/contacts/{contactId} and Method GET"
    )
		#   # Endpoint /crm/v3/objects/contacts/{contactId} and Method PATCH
		#   scenario.add_request_v1(
		#       request=contacts_contactId_PATCH_request,
		#       step_name="contacts_functional_scenario-6",
		#       description="Endpoint /crm/v3/objects/contacts/{contactId} and Method PATCH"
		#   )
		#   # Assert of scenario step contacts_functional_scenario-6 - Endpoint /crm/v3/objects/contacts/{contactId} and Method PATCH
		#   scenario.add_assert_v1(
		#       assert_value="requests.contacts_contactId_PATCH.code",
		# assert_expected_value="200", 
		#       assert_step_name="contacts_functional_scenario-7",
		#       description="Assert of scenario step contacts_functional_scenario-6 - Endpoint /crm/v3/objects/contacts/{contactId} and Method PATCH"
		#   )
		#   # Endpoint /crm/v3/objects/contacts/{contactId} and Method DELETE
		#   scenario.add_request_v1(
		#       request=contacts_contactId_DELETE_request,
		#       step_name="contacts_functional_scenario-8",
		#       description="Endpoint /crm/v3/objects/contacts/{contactId} and Method DELETE"
		#   )
		#   # Assert of scenario step contacts_functional_scenario-8 - Endpoint /crm/v3/objects/contacts/{contactId} and Method DELETE
		#   scenario.add_assert_v1(
		#       assert_value="requests.contacts_contactId_DELETE.code",
		# assert_expected_value="204", 
		#       assert_step_name="contacts_functional_scenario-9",
		#       description="Assert of scenario step contacts_functional_scenario-8 - Endpoint /crm/v3/objects/contacts/{contactId} and Method DELETE"
		#   )
    return scenario

def add_contacts_negative_get_scenario_0():
    scenario = skyramp.Scenario(
        "contacts_negative_get_scenario_0",
        ignore=True,
        vars_={"after": None,"archived": None,"associations": None,"limit": None,"properties": None,"propertiesWithHistory": None}
    )
    # Negative case of setting optional associations to [0123456789]
    scenario.add_request_v1(
        request=contacts_GET_request,
        step_name="contacts_negative_get_scenario-0",
        vars_override={"after":"vars.after","archived":"vars.archived","associations":["0123456789"],"limit":"vars.limit","properties":"vars.properties","propertiesWithHistory":"vars.propertiesWithHistory"},
        description="Negative case of setting optional associations to [0123456789]"
    )
    # Assert of scenario step contacts_negative_get_scenario-0 - Negative case of setting optional associations to [0123456789]
    scenario.add_assert_v1(
        assert_value="requests.contacts_GET.code",
		assert_expected_value="400", 
        assert_step_name="contacts_negative_get_scenario-1",
        description="Assert of scenario step contacts_negative_get_scenario-0 - Negative case of setting optional associations to [0123456789]"
    )
    return scenario

def add_contacts_negative_get_scenario_1():
    scenario = skyramp.Scenario(
        "contacts_negative_get_scenario_1",
        ignore=True,
        vars_={"after": None,"archived": None,"associations": None,"limit": None,"properties": None,"propertiesWithHistory": None}
    )
    # Negative case of setting optional archived to true
    scenario.add_request_v1(
        request=contacts_GET_request,
        step_name="contacts_negative_get_scenario-2",
        vars_override={"after":"vars.after","archived":True,"associations":"vars.associations","limit":"vars.limit","properties":"vars.properties","propertiesWithHistory":"vars.propertiesWithHistory"},
        description="Negative case of setting optional archived to true"
    )
    # Assert of scenario step contacts_negative_get_scenario-2 - Negative case of setting optional archived to true
    scenario.add_assert_v1(
        assert_value="requests.contacts_GET.code",
		assert_expected_value="400", 
        assert_step_name="contacts_negative_get_scenario-3",
        description="Assert of scenario step contacts_negative_get_scenario-2 - Negative case of setting optional archived to true"
    )
    return scenario

def add_contacts_negative_get_scenario_2():
    scenario = skyramp.Scenario(
        "contacts_negative_get_scenario_2",
        ignore=True,
        vars_={"after": None,"archived": None,"associations": None,"limit": None,"properties": None,"propertiesWithHistory": None}
    )
    # Negative case of setting optional limit to -10
    scenario.add_request_v1(
        request=contacts_GET_request,
        step_name="contacts_negative_get_scenario-4",
        vars_override={"after":"vars.after","archived":"vars.archived","associations":"vars.associations","limit":-10,"properties":"vars.properties","propertiesWithHistory":"vars.propertiesWithHistory"},
        description="Negative case of setting optional limit to -10"
    )
    # Assert of scenario step contacts_negative_get_scenario-4 - Negative case of setting optional limit to -10
    scenario.add_assert_v1(
        assert_value="requests.contacts_GET.code",
		assert_expected_value="400", 
        assert_step_name="contacts_negative_get_scenario-5",
        description="Assert of scenario step contacts_negative_get_scenario-4 - Negative case of setting optional limit to -10"
    )
    return scenario

def add_contacts_negative_get_scenario_3():
    scenario = skyramp.Scenario(
        "contacts_negative_get_scenario_3",
        ignore=True,
        vars_={"after": None,"archived": None,"associations": None,"limit": None,"properties": None,"propertiesWithHistory": None}
    )
    # Negative case of setting optional after to 0123456789
    scenario.add_request_v1(
        request=contacts_GET_request,
        step_name="contacts_negative_get_scenario-6",
        vars_override={"after":"0123456789","archived":"vars.archived","associations":"vars.associations","limit":"vars.limit","properties":"vars.properties","propertiesWithHistory":"vars.propertiesWithHistory"},
        description="Negative case of setting optional after to 0123456789"
    )
    # Assert of scenario step contacts_negative_get_scenario-6 - Negative case of setting optional after to 0123456789
    scenario.add_assert_v1(
        assert_value="requests.contacts_GET.code",
		assert_expected_value="400", 
        assert_step_name="contacts_negative_get_scenario-7",
        description="Assert of scenario step contacts_negative_get_scenario-6 - Negative case of setting optional after to 0123456789"
    )
    return scenario

def add_contacts_negative_get_scenario_4():
    scenario = skyramp.Scenario(
        "contacts_negative_get_scenario_4",
        ignore=True,
        vars_={"after": None,"archived": None,"associations": None,"limit": None,"properties": None,"propertiesWithHistory": None}
    )
    # Negative case of setting optional properties to [0123456789]
    scenario.add_request_v1(
        request=contacts_GET_request,
        step_name="contacts_negative_get_scenario-8",
        vars_override={"after":"vars.after","archived":"vars.archived","associations":"vars.associations","limit":"vars.limit","properties":["0123456789"],"propertiesWithHistory":"vars.propertiesWithHistory"},
        description="Negative case of setting optional properties to [0123456789]"
    )
    # Assert of scenario step contacts_negative_get_scenario-8 - Negative case of setting optional properties to [0123456789]
    scenario.add_assert_v1(
        assert_value="requests.contacts_GET.code",
		assert_expected_value="400", 
        assert_step_name="contacts_negative_get_scenario-9",
        description="Assert of scenario step contacts_negative_get_scenario-8 - Negative case of setting optional properties to [0123456789]"
    )
    return scenario

def add_contacts_negative_get_scenario_5():
    scenario = skyramp.Scenario(
        "contacts_negative_get_scenario_5",
        ignore=True,
        vars_={"after": None,"archived": None,"associations": None,"limit": None,"properties": None,"propertiesWithHistory": None}
    )
    # Negative case of setting optional propertiesWithHistory to [0123456789]
    scenario.add_request_v1(
        request=contacts_GET_request,
        step_name="contacts_negative_get_scenario-10",
        vars_override={"after":"vars.after","archived":"vars.archived","associations":"vars.associations","limit":"vars.limit","properties":"vars.properties","propertiesWithHistory":["0123456789"]},
        description="Negative case of setting optional propertiesWithHistory to [0123456789]"
    )
    # Assert of scenario step contacts_negative_get_scenario-10 - Negative case of setting optional propertiesWithHistory to [0123456789]
    scenario.add_assert_v1(
        assert_value="requests.contacts_GET.code",
		assert_expected_value="400", 
        assert_step_name="contacts_negative_get_scenario-11",
        description="Assert of scenario step contacts_negative_get_scenario-10 - Negative case of setting optional propertiesWithHistory to [0123456789]"
    )
    return scenario

def add_contacts_negative_post_scenario_0():
    scenario = skyramp.Scenario(
        "contacts_negative_post_scenario_0",
        ignore=True
    )
    # Negative case of setting associations to []
    scenario.add_request_v1(
        request=contacts_POST_request,
        step_name="contacts_negative_post_scenario-0",
        description="Negative case of setting associations to []", 
        blob_override={"associations":[]}
    )
    # Assert of scenario step contacts_negative_post_scenario-0 - Negative case of setting associations to []
    scenario.add_assert_v1(
        assert_value="requests.contacts_POST.code",
		assert_expected_value="400", 
        assert_step_name="contacts_negative_post_scenario-1",
        description="Assert of scenario step contacts_negative_post_scenario-0 - Negative case of setting associations to []"
    )
    return scenario

def add_contacts_negative_post_scenario_1():
    scenario = skyramp.Scenario(
        "contacts_negative_post_scenario_1",
        ignore=True
    )
    # Negative case of setting associations to nil
    scenario.add_request_v1(
        request=contacts_POST_request,
        step_name="contacts_negative_post_scenario-2",
        description="Negative case of setting associations to nil", 
        blob_override={"associations": None}
    )
    # Assert of scenario step contacts_negative_post_scenario-2 - Negative case of setting associations to nil
    scenario.add_assert_v1(
        assert_value="requests.contacts_POST.code",
		assert_expected_value="400", 
        assert_step_name="contacts_negative_post_scenario-3",
        description="Assert of scenario step contacts_negative_post_scenario-2 - Negative case of setting associations to nil"
    )
    return scenario

def add_contacts_negative_post_scenario_2():
    scenario = skyramp.Scenario(
        "contacts_negative_post_scenario_2",
        ignore=True
    )
    # Negative case of setting properties.company to 0123456789
    scenario.add_request_v1(
        request=contacts_POST_request,
        step_name="contacts_negative_post_scenario-4",
        description="Negative case of setting properties.company to 0123456789", 
        blob_override={"properties.company":"0123456789"}
    )
    # Assert of scenario step contacts_negative_post_scenario-4 - Negative case of setting properties.company to 0123456789
    scenario.add_assert_v1(
        assert_value="requests.contacts_POST.code",
		assert_expected_value="400", 
        assert_step_name="contacts_negative_post_scenario-5",
        description="Assert of scenario step contacts_negative_post_scenario-4 - Negative case of setting properties.company to 0123456789"
    )
    return scenario

def add_contacts_negative_post_scenario_3():
    scenario = skyramp.Scenario(
        "contacts_negative_post_scenario_3",
        ignore=True
    )
    # Negative case of setting properties.company to nil
    scenario.add_request_v1(
        request=contacts_POST_request,
        step_name="contacts_negative_post_scenario-6",
        description="Negative case of setting properties.company to nil", 
        blob_override={"properties.company": None}
    )
    # Assert of scenario step contacts_negative_post_scenario-6 - Negative case of setting properties.company to nil
    scenario.add_assert_v1(
        assert_value="requests.contacts_POST.code",
		assert_expected_value="400", 
        assert_step_name="contacts_negative_post_scenario-7",
        description="Assert of scenario step contacts_negative_post_scenario-6 - Negative case of setting properties.company to nil"
    )
    return scenario

def add_contacts_negative_post_scenario_4():
    scenario = skyramp.Scenario(
        "contacts_negative_post_scenario_4",
        ignore=True
    )
    # Negative case of setting properties.email to 0123456789
    scenario.add_request_v1(
        request=contacts_POST_request,
        step_name="contacts_negative_post_scenario-8",
        description="Negative case of setting properties.email to 0123456789", 
        blob_override={"properties.email":"0123456789"}
    )
    # Assert of scenario step contacts_negative_post_scenario-8 - Negative case of setting properties.email to 0123456789
    scenario.add_assert_v1(
        assert_value="requests.contacts_POST.code",
		assert_expected_value="400", 
        assert_step_name="contacts_negative_post_scenario-9",
        description="Assert of scenario step contacts_negative_post_scenario-8 - Negative case of setting properties.email to 0123456789"
    )
    return scenario

def add_contacts_negative_post_scenario_5():
    scenario = skyramp.Scenario(
        "contacts_negative_post_scenario_5",
        ignore=True
    )
    # Negative case of setting properties.email to nil
    scenario.add_request_v1(
        request=contacts_POST_request,
        step_name="contacts_negative_post_scenario-10",
        description="Negative case of setting properties.email to nil", 
        blob_override={"properties.email": None}
    )
    # Assert of scenario step contacts_negative_post_scenario-10 - Negative case of setting properties.email to nil
    scenario.add_assert_v1(
        assert_value="requests.contacts_POST.code",
		assert_expected_value="400", 
        assert_step_name="contacts_negative_post_scenario-11",
        description="Assert of scenario step contacts_negative_post_scenario-10 - Negative case of setting properties.email to nil"
    )
    return scenario

def add_contacts_negative_post_scenario_6():
    scenario = skyramp.Scenario(
        "contacts_negative_post_scenario_6",
        ignore=True
    )
    # Negative case of setting properties.firstname to 0123456789
    scenario.add_request_v1(
        request=contacts_POST_request,
        step_name="contacts_negative_post_scenario-12",
        description="Negative case of setting properties.firstname to 0123456789", 
        blob_override={"properties.firstname":"0123456789"}
    )
    # Assert of scenario step contacts_negative_post_scenario-12 - Negative case of setting properties.firstname to 0123456789
    scenario.add_assert_v1(
        assert_value="requests.contacts_POST.code",
		assert_expected_value="400", 
        assert_step_name="contacts_negative_post_scenario-13",
        description="Assert of scenario step contacts_negative_post_scenario-12 - Negative case of setting properties.firstname to 0123456789"
    )
    return scenario

def add_contacts_negative_post_scenario_7():
    scenario = skyramp.Scenario(
        "contacts_negative_post_scenario_7",
        ignore=True
    )
    # Negative case of setting properties.firstname to nil
    scenario.add_request_v1(
        request=contacts_POST_request,
        step_name="contacts_negative_post_scenario-14",
        description="Negative case of setting properties.firstname to nil", 
        blob_override={"properties.firstname": None}
    )
    # Assert of scenario step contacts_negative_post_scenario-14 - Negative case of setting properties.firstname to nil
    scenario.add_assert_v1(
        assert_value="requests.contacts_POST.code",
		assert_expected_value="400", 
        assert_step_name="contacts_negative_post_scenario-15",
        description="Assert of scenario step contacts_negative_post_scenario-14 - Negative case of setting properties.firstname to nil"
    )
    return scenario

def add_contacts_negative_post_scenario_8():
    scenario = skyramp.Scenario(
        "contacts_negative_post_scenario_8",
        ignore=True
    )
    # Negative case of setting properties.lastname to 0123456789
    scenario.add_request_v1(
        request=contacts_POST_request,
        step_name="contacts_negative_post_scenario-16",
        description="Negative case of setting properties.lastname to 0123456789", 
        blob_override={"properties.lastname":"0123456789"}
    )
    # Assert of scenario step contacts_negative_post_scenario-16 - Negative case of setting properties.lastname to 0123456789
    scenario.add_assert_v1(
        assert_value="requests.contacts_POST.code",
		assert_expected_value="400", 
        assert_step_name="contacts_negative_post_scenario-17",
        description="Assert of scenario step contacts_negative_post_scenario-16 - Negative case of setting properties.lastname to 0123456789"
    )
    return scenario

def add_contacts_negative_post_scenario_9():
    scenario = skyramp.Scenario(
        "contacts_negative_post_scenario_9",
        ignore=True
    )
    # Negative case of setting properties.lastname to nil
    scenario.add_request_v1(
        request=contacts_POST_request,
        step_name="contacts_negative_post_scenario-18",
        description="Negative case of setting properties.lastname to nil", 
        blob_override={"properties.lastname": None}
    )
    # Assert of scenario step contacts_negative_post_scenario-18 - Negative case of setting properties.lastname to nil
    scenario.add_assert_v1(
        assert_value="requests.contacts_POST.code",
		assert_expected_value="400", 
        assert_step_name="contacts_negative_post_scenario-19",
        description="Assert of scenario step contacts_negative_post_scenario-18 - Negative case of setting properties.lastname to nil"
    )
    return scenario

def add_contacts_negative_post_scenario_10():
    scenario = skyramp.Scenario(
        "contacts_negative_post_scenario_10",
        ignore=True
    )
    # Negative case of setting properties.phone to 0123456789
    scenario.add_request_v1(
        request=contacts_POST_request,
        step_name="contacts_negative_post_scenario-20",
        description="Negative case of setting properties.phone to 0123456789", 
        blob_override={"properties.phone":"0123456789"}
    )
    # Assert of scenario step contacts_negative_post_scenario-20 - Negative case of setting properties.phone to 0123456789
    scenario.add_assert_v1(
        assert_value="requests.contacts_POST.code",
		assert_expected_value="400", 
        assert_step_name="contacts_negative_post_scenario-21",
        description="Assert of scenario step contacts_negative_post_scenario-20 - Negative case of setting properties.phone to 0123456789"
    )
    return scenario

def add_contacts_negative_post_scenario_11():
    scenario = skyramp.Scenario(
        "contacts_negative_post_scenario_11",
        ignore=True
    )
    # Negative case of setting properties.phone to nil
    scenario.add_request_v1(
        request=contacts_POST_request,
        step_name="contacts_negative_post_scenario-22",
        description="Negative case of setting properties.phone to nil", 
        blob_override={"properties.phone": None}
    )
    # Assert of scenario step contacts_negative_post_scenario-22 - Negative case of setting properties.phone to nil
    scenario.add_assert_v1(
        assert_value="requests.contacts_POST.code",
		assert_expected_value="400", 
        assert_step_name="contacts_negative_post_scenario-23",
        description="Assert of scenario step contacts_negative_post_scenario-22 - Negative case of setting properties.phone to nil"
    )
    return scenario

def add_contacts_negative_post_scenario_12():
    scenario = skyramp.Scenario(
        "contacts_negative_post_scenario_12",
        ignore=True
    )
    # Negative case of setting properties.website to 0123456789
    scenario.add_request_v1(
        request=contacts_POST_request,
        step_name="contacts_negative_post_scenario-24",
        description="Negative case of setting properties.website to 0123456789", 
        blob_override={"properties.website":"0123456789"}
    )
    # Assert of scenario step contacts_negative_post_scenario-24 - Negative case of setting properties.website to 0123456789
    scenario.add_assert_v1(
        assert_value="requests.contacts_POST.code",
		assert_expected_value="400", 
        assert_step_name="contacts_negative_post_scenario-25",
        description="Assert of scenario step contacts_negative_post_scenario-24 - Negative case of setting properties.website to 0123456789"
    )
    return scenario

def add_contacts_negative_post_scenario_13():
    scenario = skyramp.Scenario(
        "contacts_negative_post_scenario_13",
        ignore=True
    )
    # Negative case of setting properties.website to nil
    scenario.add_request_v1(
        request=contacts_POST_request,
        step_name="contacts_negative_post_scenario-26",
        description="Negative case of setting properties.website to nil", 
        blob_override={"properties.website": None}
    )
    # Assert of scenario step contacts_negative_post_scenario-26 - Negative case of setting properties.website to nil
    scenario.add_assert_v1(
        assert_value="requests.contacts_POST.code",
		assert_expected_value="400", 
        assert_step_name="contacts_negative_post_scenario-27",
        description="Assert of scenario step contacts_negative_post_scenario-26 - Negative case of setting properties.website to nil"
    )
    return scenario

def add_contacts_contactId_negative_get_scenario_0():
    scenario = skyramp.Scenario(
        "contacts_contactId_negative_get_scenario_0",
        ignore=True,
        vars_={"archived": None,"associations": None,"contactId":"default_value","properties": None,"propertiesWithHistory": None}
    )
    # Negative case of setting optional propertiesWithHistory to [0123456789]
    scenario.add_request_v1(
        request=contacts_contactId_GET_request,
        step_name="contacts_contactId_negative_get_scenario-0",
        vars_override={"archived":"vars.archived","associations":"vars.associations","contactId":"vars.contactId","properties":"vars.properties","propertiesWithHistory":["0123456789"]},
        description="Negative case of setting optional propertiesWithHistory to [0123456789]"
    )
    # Assert of scenario step contacts_contactId_negative_get_scenario-0 - Negative case of setting optional propertiesWithHistory to [0123456789]
    scenario.add_assert_v1(
        assert_value="requests.contacts_contactId_GET.code",
        assert_expected_value="400", 
        assert_step_name="contacts_contactId_negative_get_scenario-1",
        description="Assert of scenario step contacts_contactId_negative_get_scenario-0 - Negative case of setting optional propertiesWithHistory to [0123456789]"
    )
    return scenario

def add_contacts_contactId_negative_get_scenario_1():
    scenario = skyramp.Scenario(
        "contacts_contactId_negative_get_scenario_1",
        ignore=True,
        vars_={"archived": None,"associations": None,"contactId":"default_value","properties": None,"propertiesWithHistory": None}
    )
    # Negative case of setting optional associations to [0123456789]
    scenario.add_request_v1(
        request=contacts_contactId_GET_request,
        step_name="contacts_contactId_negative_get_scenario-2",
        vars_override={"archived":"vars.archived","associations":["0123456789"],"contactId":"vars.contactId","properties":"vars.properties","propertiesWithHistory":"vars.propertiesWithHistory"},
        description="Negative case of setting optional associations to [0123456789]"
    )
    # Assert of scenario step contacts_contactId_negative_get_scenario-2 - Negative case of setting optional associations to [0123456789]
    scenario.add_assert_v1(
        assert_value="requests.contacts_contactId_GET.code",
		assert_expected_value="400", 
        assert_step_name="contacts_contactId_negative_get_scenario-3",
        description="Assert of scenario step contacts_contactId_negative_get_scenario-2 - Negative case of setting optional associations to [0123456789]"
    )
    return scenario

def add_contacts_contactId_negative_get_scenario_2():
    scenario = skyramp.Scenario(
        "contacts_contactId_negative_get_scenario_2",
        ignore=True,
        vars_={"archived": None,"associations": None,"contactId":"default_value","properties": None,"propertiesWithHistory": None}
    )
    # Negative case of setting optional archived to true
    scenario.add_request_v1(
        request=contacts_contactId_GET_request,
        step_name="contacts_contactId_negative_get_scenario-4",
        vars_override={"archived":True,"associations":"vars.associations","contactId":"vars.contactId","properties":"vars.properties","propertiesWithHistory":"vars.propertiesWithHistory"},
        description="Negative case of setting optional archived to true"
    )
    # Assert of scenario step contacts_contactId_negative_get_scenario-4 - Negative case of setting optional archived to true
    scenario.add_assert_v1(
        assert_value="requests.contacts_contactId_GET.code",
		assert_expected_value="400", 
        assert_step_name="contacts_contactId_negative_get_scenario-5",
        description="Assert of scenario step contacts_contactId_negative_get_scenario-4 - Negative case of setting optional archived to true"
    )
    return scenario

def add_contacts_contactId_negative_get_scenario_3():
    scenario = skyramp.Scenario(
        "contacts_contactId_negative_get_scenario_3",
        ignore=True,
        vars_={"archived": None,"associations": None,"contactId":"default_value","properties": None,"propertiesWithHistory": None}
    )
    # Negative case of setting optional properties to [0123456789]
    scenario.add_request_v1(
        request=contacts_contactId_GET_request,
        step_name="contacts_contactId_negative_get_scenario-6",
        vars_override={"archived":"vars.archived","associations":"vars.associations","contactId":"vars.contactId","properties":["0123456789"],"propertiesWithHistory":"vars.propertiesWithHistory"},
        description="Negative case of setting optional properties to [0123456789]"
    )
    # Assert of scenario step contacts_contactId_negative_get_scenario-6 - Negative case of setting optional properties to [0123456789]
    scenario.add_assert_v1(
        assert_value="requests.contacts_contactId_GET.code",
		assert_expected_value="400", 
        assert_step_name="contacts_contactId_negative_get_scenario-7",
        description="Assert of scenario step contacts_contactId_negative_get_scenario-6 - Negative case of setting optional properties to [0123456789]"
    )
    return scenario

def get_test_scenarios():
    scenario = skyramp.Scenario(
        "contacts_full_scenario"
    )
    contacts_functional_scenario = add_contacts_functional_scenario()
    scenario.add_scenario_v1(
        contacts_functional_scenario,
        step_name="contacts_full_scenario-0" ,
        description="functional scenario of /crm/v3/objects/contacts" 
    )
    # contacts_negative_get_scenario_0 = add_contacts_negative_get_scenario_0()
    # scenario.add_scenario_v1(
    #     contacts_negative_get_scenario_0,
    #     step_name="contacts_full_scenario-2" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" ,
    #     vars_override={"after": None,"archived": None,"associations": None,"limit": None,"properties": None,"propertiesWithHistory": None}
    # )
    # contacts_negative_get_scenario_1 = add_contacts_negative_get_scenario_1()
    # scenario.add_scenario_v1(
    #     contacts_negative_get_scenario_1,
    #     step_name="contacts_full_scenario-4" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" ,
    #     vars_override={"after": None,"archived": None,"associations": None,"limit": None,"properties": None,"propertiesWithHistory": None}
    # )
    # contacts_negative_get_scenario_2 = add_contacts_negative_get_scenario_2()
    # scenario.add_scenario_v1(
    #     contacts_negative_get_scenario_2,
    #     step_name="contacts_full_scenario-6" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" ,
    #     vars_override={"after": None,"archived": None,"associations": None,"limit": None,"properties": None,"propertiesWithHistory": None}
    # )
    # contacts_negative_get_scenario_3 = add_contacts_negative_get_scenario_3()
    # scenario.add_scenario_v1(
    #     contacts_negative_get_scenario_3,
    #     step_name="contacts_full_scenario-8" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" ,
    #     vars_override={"after": None,"archived": None,"associations": None,"limit": None,"properties": None,"propertiesWithHistory": None}
    # )
    # contacts_negative_get_scenario_4 = add_contacts_negative_get_scenario_4()
    # scenario.add_scenario_v1(
    #     contacts_negative_get_scenario_4,
    #     step_name="contacts_full_scenario-10" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" ,
    #     vars_override={"after": None,"archived": None,"associations": None,"limit": None,"properties": None,"propertiesWithHistory": None}
    # )
    # contacts_negative_get_scenario_5 = add_contacts_negative_get_scenario_5()
    # scenario.add_scenario_v1(
    #     contacts_negative_get_scenario_5,
    #     step_name="contacts_full_scenario-12" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" ,
    #     vars_override={"after": None,"archived": None,"associations": None,"limit": None,"properties": None,"propertiesWithHistory": None}
    # )
    # contacts_negative_post_scenario_0 = add_contacts_negative_post_scenario_0()
    # scenario.add_scenario_v1(
    #     contacts_negative_post_scenario_0,
    #     step_name="contacts_full_scenario-14" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" 
    # )
    # contacts_negative_post_scenario_1 = add_contacts_negative_post_scenario_1()
    # scenario.add_scenario_v1(
    #     contacts_negative_post_scenario_1,
    #     step_name="contacts_full_scenario-16" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" 
    # )
    # contacts_negative_post_scenario_2 = add_contacts_negative_post_scenario_2()
    # scenario.add_scenario_v1(
    #     contacts_negative_post_scenario_2,
    #     step_name="contacts_full_scenario-18" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" 
    # )
    # contacts_negative_post_scenario_3 = add_contacts_negative_post_scenario_3()
    # scenario.add_scenario_v1(
    #     contacts_negative_post_scenario_3,
    #     step_name="contacts_full_scenario-20" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" 
    # )
    # contacts_negative_post_scenario_4 = add_contacts_negative_post_scenario_4()
    # scenario.add_scenario_v1(
    #     contacts_negative_post_scenario_4,
    #     step_name="contacts_full_scenario-22" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" 
    # )
    # contacts_negative_post_scenario_5 = add_contacts_negative_post_scenario_5()
    # scenario.add_scenario_v1(
    #     contacts_negative_post_scenario_5,
    #     step_name="contacts_full_scenario-24" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" 
    # )
    # contacts_negative_post_scenario_6 = add_contacts_negative_post_scenario_6()
    # scenario.add_scenario_v1(
    #     contacts_negative_post_scenario_6,
    #     step_name="contacts_full_scenario-26" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" 
    # )
    # contacts_negative_post_scenario_7 = add_contacts_negative_post_scenario_7()
    # scenario.add_scenario_v1(
    #     contacts_negative_post_scenario_7,
    #     step_name="contacts_full_scenario-28" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" 
    # )
    # contacts_negative_post_scenario_8 = add_contacts_negative_post_scenario_8()
    # scenario.add_scenario_v1(
    #     contacts_negative_post_scenario_8,
    #     step_name="contacts_full_scenario-30" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" 
    # )
    # contacts_negative_post_scenario_9 = add_contacts_negative_post_scenario_9()
    # scenario.add_scenario_v1(
    #     contacts_negative_post_scenario_9,
    #     step_name="contacts_full_scenario-32" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" 
    # )
    # contacts_negative_post_scenario_10 = add_contacts_negative_post_scenario_10()
    # scenario.add_scenario_v1(
    #     contacts_negative_post_scenario_10,
    #     step_name="contacts_full_scenario-34" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" 
    # )
    # contacts_negative_post_scenario_11 = add_contacts_negative_post_scenario_11()
    # scenario.add_scenario_v1(
    #     contacts_negative_post_scenario_11,
    #     step_name="contacts_full_scenario-36" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" 
    # )
    # contacts_negative_post_scenario_12 = add_contacts_negative_post_scenario_12()
    # scenario.add_scenario_v1(
    #     contacts_negative_post_scenario_12,
    #     step_name="contacts_full_scenario-38" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" 
    # )
    # contacts_negative_post_scenario_13 = add_contacts_negative_post_scenario_13()
    # scenario.add_scenario_v1(
    #     contacts_negative_post_scenario_13,
    #     step_name="contacts_full_scenario-40" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" 
    # )
    # contacts_contactId_negative_get_scenario_0 = add_contacts_contactId_negative_get_scenario_0()
    # scenario.add_scenario_v1(
    #     contacts_contactId_negative_get_scenario_0,
    #     step_name="contacts_full_scenario-42" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" ,
    #     vars_override={"archived": None,"associations": None,"contactId":"default_value","properties": None,"propertiesWithHistory": None}
    # )
    # contacts_contactId_negative_get_scenario_1 = add_contacts_contactId_negative_get_scenario_1()
    # scenario.add_scenario_v1(
    #     contacts_contactId_negative_get_scenario_1,
    #     step_name="contacts_full_scenario-44" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" ,
    #     vars_override={"archived": None,"associations": None,"contactId":"default_value","properties": None,"propertiesWithHistory": None}
    # )
    # contacts_contactId_negative_get_scenario_2 = add_contacts_contactId_negative_get_scenario_2()
    # scenario.add_scenario_v1(
    #     contacts_contactId_negative_get_scenario_2,
    #     step_name="contacts_full_scenario-46" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" ,
    #     vars_override={"archived": None,"associations": None,"contactId":"default_value","properties": None,"propertiesWithHistory": None}
    # )
    # contacts_contactId_negative_get_scenario_3 = add_contacts_contactId_negative_get_scenario_3()
    # scenario.add_scenario_v1(
    #     contacts_contactId_negative_get_scenario_3,
    #     step_name="contacts_full_scenario-48" ,
    #     description="Negative Scenario of /crm/v3/objects/contacts" ,
    #     vars_override={"archived": None,"associations": None,"contactId":"default_value","properties": None,"propertiesWithHistory": None}
    # )
    return scenario

def execute_tests(
    address="localhost:35142",
    override_code_path=None,
    global_vars={},
    endpoint_address="https://api.hubapi.com",
    **kwargs
):
    docker_client = skyramp.DockerClient()
    scenarios = get_test_scenarios()

    global_headers = {
        "content-type": "application/json",
        "Authorization": "Bearer <token>"
    }
    docker_client.set_global_rest_headers(global_headers)

    status = docker_client.tester_start_v1(
        scenario=scenarios,
        test_name="contacts test",
        address=address,
        blocked=True,
        global_vars=global_vars,
        override_code_path=override_code_path,
        endpoint_address=endpoint_address ,
        skip_verify=kwargs.get("skip_verify", False),
        blobs=kwargs.get("blobs", {}),
        loadtest_config=skyramp.LoadTestConfig.from_kwargs(**kwargs),
        is_formatting_enabled=True
    )
    return status

if __name__ == "__main__":
    args = skyramp.parse_args()
    execute_tests(**args)
