# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.contact import Contact

class TestContact(unittest.TestCase):
    """Contact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Contact:
        """Test Contact
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Contact`
        """
        model = Contact()
        if include_optional:
            return Contact(
                object = 'Contact',
                address_array = [
                    unicourt.models.address.Address(
                        object = 'Address', 
                        street_address1 = '0', 
                        street_address2 = '0', 
                        city = '0', 
                        state_name = 'UNKNOWN', 
                        state_code = '01', 
                        country_name = 'UNKNOWN', 
                        country_code = '01', 
                        zip = '0', 
                        zip4 = '0123', 
                        is_visible = True, 
                        first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        latitude = -90, 
                        longitude = -180, )
                    ],
                phone_number_array = [
                    unicourt.models.phone.Phone(
                        object = 'Phone', 
                        phone_number = '0', 
                        phone_type = 'DEFAULT', 
                        is_visible = True, 
                        first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                email_array = [
                    unicourt.models.email.Email(
                        object = 'Email', 
                        email_id = '0', 
                        is_visible = True, 
                        first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return Contact(
                object = 'Contact',
                address_array = [
                    unicourt.models.address.Address(
                        object = 'Address', 
                        street_address1 = '0', 
                        street_address2 = '0', 
                        city = '0', 
                        state_name = 'UNKNOWN', 
                        state_code = '01', 
                        country_name = 'UNKNOWN', 
                        country_code = '01', 
                        zip = '0', 
                        zip4 = '0123', 
                        is_visible = True, 
                        first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        latitude = -90, 
                        longitude = -180, )
                    ],
                phone_number_array = [
                    unicourt.models.phone.Phone(
                        object = 'Phone', 
                        phone_number = '0', 
                        phone_type = 'DEFAULT', 
                        is_visible = True, 
                        first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                email_array = [
                    unicourt.models.email.Email(
                        object = 'Email', 
                        email_id = '0', 
                        is_visible = True, 
                        first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testContact(self):
        """Test Contact"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
