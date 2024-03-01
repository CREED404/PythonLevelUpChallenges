def sort_words(string: str):
    return " ".join(sorted(string.split(), key=lambda x: x.lower()))

# Observations
#
# `str.casefold` builds over `str.lower` to be locale independent
