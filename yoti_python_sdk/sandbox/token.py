from yoti_python_sdk.sandbox.attribute import SandboxAttribute
from yoti_python_sdk import config
from cryptography.fernet import base64


class YotiTokenRequest(object):
    def __init__(self, remember_me_id, sandbox_attributes=None):

        if sandbox_attributes is None:
            sandbox_attributes = []

        self.remember_me_id = remember_me_id
        self.sandbox_attributes = sandbox_attributes

    def __dict__(self):
        return {
            "remember_me_id": self.remember_me_id,
            "profile_attributes": self.sandbox_attributes,
        }

    @staticmethod
    def builder():
        return YotiTokenRequestBuilder()


class YotiTokenRequestBuilder(object):
    def __init__(self):
        self.remember_me_id = None
        self.attributes = []

    def with_remember_me_id(self, remember_me_id):
        self.remember_me_id = remember_me_id
        return self

    def with_attribute(self, sandbox_attribute):
        self.attributes.append(sandbox_attribute)
        return self

    def with_given_names(self, value, anchors=None):
        return self.__create_attribute(config.ATTRIBUTE_GIVEN_NAMES, value, anchors)

    def with_family_name(self, value, anchors=None):
        return self.__create_attribute(config.ATTRIBUTE_FAMILY_NAME, value, anchors)

    def with_full_name(self, value, anchors=None):
        return self.__create_attribute(config.ATTRIBUTE_FULL_NAME, value, anchors)

    def with_date_of_birth(self, value, anchors=None):
        return self.__create_attribute(config.ATTRIBUTE_DATE_OF_BIRTH, value, anchors)

    def with_age_over(self, value, anchors=None):
        return self.__create_attribute(config.ATTRIBUTE_AGE_OVER, value, anchors)

    def with_age_under(self, value, anchors=None):
        return self.__create_attribute(config.ATTRIBUTE_AGE_UNDER, value, anchors)

    def with_gender(self, value, anchors=None):
        return self.__create_attribute(config.ATTRIBUTE_GENDER, value, anchors)

    def with_phone_number(self, value, anchors=None):
        return self.__create_attribute(config.ATTRIBUTE_PHONE_NUMBER, value, anchors)

    def with_nationality(self, value, anchors=None):
        return self.__create_attribute(config.ATTRIBUTE_NATIONALITY, value, anchors)

    def with_postal_address(self, value, anchors=None):
        return self.__create_attribute(config.ATTRIBUTE_POSTAL_ADDRESS, value, anchors)

    def with_structured_postal_address(self, value, anchors=None):
        return self.__create_attribute(
            config.ATTRIBUTE_STRUCTURED_POSTAL_ADDRESS, value, anchors
        )

    def with_selfie(self, value, anchors=None):
        base64_selfie = base64.b64decode(value).decode("utf-8")
        return self.with_base64_selfie(base64_selfie, anchors)

    def with_base64_selfie(self, value, anchors=None):
        return self.__create_attribute(config.ATTRIBUTE_SELFIE, value, anchors)

    def with_email_address(self, value, anchors=None):
        return self.__create_attribute(config.ATTRIBUTE_EMAIL_ADDRESS, value, anchors)

    def with_document_details(self, value, anchors=None):
        return self.__create_attribute(
            config.ATTRIBUTE_DOCUMENT_DETAILS, value, anchors
        )

    def build(self):
        return YotiTokenRequest(self.remember_me_id, self.attributes)

    @staticmethod
    def __create_attribute(self, name, value, anchors=None):
        return SandboxAttribute(name, value, anchors)
