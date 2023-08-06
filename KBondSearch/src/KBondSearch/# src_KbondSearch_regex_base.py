# src/KbondSearch/regex_base.py

import re 

# extracts 22.10.02 or 23.1.13
dt_ext = re.compile(r"[\d]{1,2}.[\d]{1,2}.[\d]{1,2}")

# extracts 22-1, or 23-12
ty_ext = re.compile(r"[\d]{2}-[\d]{1,2}")

# extracts 

# extracts abbreviations of ty and msb
abbr_ext = re.compile(
	r"([국당]|[국전]|[통당]|[통딱]|[구통]|)"
)