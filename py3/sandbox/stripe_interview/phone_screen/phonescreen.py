# Part 1
import re
from typing import List


# In an HTTP request, the Accept-Language header describes the list of languages that the requester would like content to be returned in. The header takes the form of a comma-separated list of language tags. For example:

#   Accept-Language: en-US, fr-CA, fr-FR



# means that the reader would accept:

# English as spoken in the United States (most preferred)
# French as spoken in Canada
# French as spoken in France (least preferred)


# We're writing a server that needs to return content in an acceptable language for the requester, and we want to make use of this header. Our server doesn't support every possible language that might be requested (yet!), but there is a set of languages that we do support. Write a function that receives two arguments: an Accept-Language header value as a string and a set of supported languages, and returns the list of language tags that will work for the request. The language tags should be returned in descending order of preference (the same order as they appeared in the header).



# In addition to writing this function, you should use tests to demonstrate that it's correct, either via an existing testing system or one you create.


# Examples:



# parse_accept_language(
#   "en-US, fr-CA, fr-FR",  # the client's Accept-Language header, a string
#   ["fr-FR", "en-US"]      # the server's supported languages, a set of strings
# )
# returns: ["en-US", "fr-FR"]


# parse_accept_language("fr-CA, fr-FR", ["en-US", "fr-FR"])
# returns: ["fr-FR"]


# parse_accept_language("en-US", ["en-US", "fr-CA"])
# returns: ["en-US"]


# Enter your code here. Read input from STDIN. Print output to STDOUT

# Part 2

# Accept-Language headers will often also include a language tag that is not region-specific - for example, a tag of "en" means "any variant of English". Extend your function to support these language tags by letting them match all specific variants of the language.



# Examples:



# parse_accept_language("en", ["en-US", "fr-CA", "fr-FR"])
# returns: ["en-US"]

# parse_accept_language("fr", ["en-US", "fr-CA", "fr-FR"])
# returns: ["fr-CA", "fr-FR"]

# parse_accept_language("fr-FR, fr", ["en-US", "fr-CA", "fr-FR"])
# returns: ["fr-FR", "fr-CA"]


def parse_accept_language(accept_header: str, server_langs: List[str]):
    server_lang_set = set(server_langs)
    lang_qfs = []
    accept_langs = re.split(',\\s*', accept_header.strip())
    returned_langs = set()
    result = []

    for al in accept_langs:
        lang, qf = re.split(';', al)
        qf = float(re.split('=', qf)[1]) if qf else 1
        lang_qfs.append((lang, qf))

    lang_qfs.sort(key=lambda e: e[1], reverse=True)

    for lang_qf in lang_qfs:
        accept_lang_spec = lang_qf[0]
        lang_parts = re.split('\\-', lang_qf[0])
        if len(lang_parts) == 1:
            for sl in server_langs:
                if (lang_parts[0] == '*' or sl.startswith(lang_parts[0] + '-')) and sl not in returned_langs:
                    returned_langs.add(sl)
                    result.append(sl)
        elif len(lang_parts) == 2 and accept_lang_spec in server_lang_set and accept_lang_spec not in returned_langs:
            returned_langs.add(accept_lang_spec)
            result.append(accept_lang_spec)
        else:
            # log some warning
            pass

    return result

