# sudo python3 -m pip install --upgrade --force pip
# pip3 install --upgrade ibm-watson
# pip3 install ibm-cloud-sdk-core
# pylint: disable=unused-import,line-too-long,bare-except,import-error,invalid-name,missing-final-newline

"""This is a translator module"""

import ibm_watson

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def englishtofrench(word):
    """This class does english to french translation"""

    url_lt='https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/98eba734-0a37-4a92-ba67-9ca4a7766005'
    version_lt='2023-02-10'
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    lt = language_translator
    translation = lt.translate(text=word, model_id="en-fr").get_result()
    
    if word == " ":
        print("Please enter a word")
    else:
        pass

    return translation['translations'][0]['translation']

def englishtofrench(word):
    """This class does english to french translation"""

    url_lt='https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/98eba734-0a37-4a92-ba67-9ca4a7766005'
    version_lt='2023-02-10'
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    lt = language_translator
    translation = lt.translate(text=word, model_id="en-fr").get_result()
    return translation['translations'][0]['translation']
