def err(err_code, add_msg=None):
  if err_code == 400:
    print(f"[EXTD] Oops... Bad Request (400) \nDeveloper Note: {add_msg}")
  elif err_code == 401:
    print(f"[EXTD] Oops... Authentication Fail (401) \nDeveloper Note: {add_msg}")
  elif err_code == 402:
    print(f"[EXTD] Oops... Payment Avaliable But Rejected (402) \nDeveloper Note: {add_msg}")
  elif err_code == 403:
    print(f"[EXTD] Oops... Forbidden  (403) \nDeveloper Note: {add_msg}")
  elif err_code == 404:
    print(f"[EXTD] Oops... That wasn't found... (404) \nDeveloper Note: {add_msg}")
  elif err_code == 405:
    print(f"[EXTD] Oops... Method Not Allowed (405) \nDeveloper Note: {add_msg}")
  elif err_code == 406:
    print(f"[EXTD] Oops... Not Acceptable (406) \nDeveloper Note: {add_msg}")
  elif err_code == 407:
    print(f"[EXTD] Oops... Proxy Authentication Required (407) \nDeveloper Note: {add_msg}")
  elif err_code == 408:
    print(f"[EXTD] Oops... Request Took Too Long (408) \nDeveloper Note: {add_msg}")
  elif err_code == 409:
    print(f"[EXTD] Oops... Conflict (409) \nDeveloper Note: {add_msg}")
  elif err_code == 410:
    print(f"[EXTD] Oops... Missing/Gone (410) \nDeveloper Note: {add_msg}")
  elif err_code == 411:
    print(f"[EXTD] Oops... Length Required (411) \nDeveloper Note: {add_msg}")
  elif err_code == 412:
    print(f"[EXTD] Oops... Precondition Failed (412) \nDeveloper Note: {add_msg}")
  elif err_code == 413:
    print(f"[EXTD] Oops... Request Entity Too Large (413) \nDeveloper Note: {add_msg}")
  elif err_code == 414:
    print(f"[EXTD] Oops... Request-URI Too Long (414) \nDeveloper Note: {add_msg}")
  elif err_code == 415:
    print(f"[EXTD] Oops... Unsupported Media Type (415) \nDeveloper Note: {add_msg}")
  elif err_code == 416:
    print(f"[EXTD] Oops... Requested Range Not Satisfiable (416) \nDeveloper Note: {add_msg}")
  elif err_code == 417:
    print(f"[EXTD] Oops... Expectation Failed (417) \nDeveloper Note: {add_msg}")
  elif err_code == 418:
    print(f"[EXTD] Oops... I'm a teapot!! (418) \nDeveloper Note: {add_msg}")
  elif err_code == 419:
    print(f"[EXTD] Oops... Authentication Timeout (419) \nDeveloper Note: {add_msg}")
  elif err_code == 420:
    print(f"[EXTD] Oops... Developers Are Busy (420) \nDeveloper Note: {add_msg}")
  elif err_code == 421:
    print(f"[EXTD] Oops... Misdirected Request (421) \nDeveloper Note: {add_msg}")
  elif err_code == 422:
    print(f"[EXTD] Oops... Unprocessable Entity (422) \nDeveloper Note: {add_msg}")
  elif err_code == 423:
    print(f"[EXTD] Oops... Locked (423) \nDeveloper Note: {add_msg}")
  elif err_code == 424:
    print(f"[EXTD] Oops... Failed Dependency (424) \nDeveloper Note: {add_msg}")
  elif err_code == 425:
    print(f"[EXTD] Oops... Too Early (425) \nDeveloper Note: {add_msg}")
  elif err_code == 426:
    print(f"[EXTD] Oops... Upgrade Required (426) \nDeveloper Note: {add_msg}")
  elif err_code == 428:
    print(f"[EXTD] Oops... Precondition Required (428) \nDeveloper Note: {add_msg}")
  elif err_code == 429:
    print(f"[EXTD] Oops... Too Many Requests (429) \nDeveloper Note: {add_msg}")
  elif err_code == 431:
    print(f"[EXTD] Oops... Request Header Fields Too Large (431) \nDeveloper Note: {add_msg}")
  elif err_code == 451:
    print(f"[EXTD] Oops... Unavailable For Legal Reasons (451) \nDeveloper Note: {add_msg}")
  elif err_code == None:
    print(f"[EXTD] Oops... Developers Were Lazy, No Error Code Provided (None) \nDeveloper Note: {add_msg}")
  elif err_code == 500:
    print(f"[EXTD] Oops... Internal Server Error (500) \nDeveloper Note: {add_msg}")
  elif err_code == 501:
    print(f"[EXTD] Oops... Not Implemented (501) \nDeveloper Note: {add_msg}")
  elif err_code == 502:
    print(f"[EXTD] Oops... Bad Gateway (502) \nDeveloper Note: {add_msg}")
  elif err_code == 503:
    print(f"[EXTD] Oops... Service Unavailable (503) \nDeveloper Note: {add_msg}")
  elif err_code == 504:
    print(f"[EXTD] Oops... Gateway Timeout (504) \nDeveloper Note: {add_msg}")
  elif err_code == 505:
    print(f"[EXTD] Oops... HTTP Version Not Supported (505) \nDeveloper Note: {add_msg}")
  elif err_code == 506:
    print(f"[EXTD] Oops... Variant Also Negotiates (506) \nDeveloper Note: {add_msg}")
  elif err_code == 507:
    print(f"[EXTD] Oops... Insufficient Storage (507) \nDeveloper Note: {add_msg}")
  elif err_code == 508:
    print(f"[EXTD] Oops... Loop Detected (508) \nDeveloper Note: {add_msg}")
  elif err_code == 510:
    print(f"[EXTD] Oops... Not Extended (510) \nDeveloper Note: {add_msg}")
  elif err_code == 511:
    print(f"[EXTD] Oops... Network Authentication Required (511) \nDeveloper Note: {add_msg}")
  elif err_code == 218:
    print(f"[EXTD] This is fine... (218) \nDeveloper Note: {add_msg}")
  elif err_code == 450:
    print(f"[EXTD] Oops... Microsoft Parental Controls Blocked This... (450) \nDeveloper Note: {add_msg}")  
  elif err_code == 529:
    print(f"[EXTD] Oops... This Is Overloaded (529) \nDeveloper Note: {add_msg}")
  elif err_code == 530:
    print(f"[EXTD] Oops... This Is Frozen (530) \nDeveloper Note: {add_msg}")
  elif err_code == 440:
    print(f"[EXTD] Oops... Login Timeout (440) \nDeveloper Note: {add_msg}")
  elif err_code == 110:
    print(f"[EXTD] Oops... Stale Bread Detected (110) \nDeveloper Note: {add_msg}")
  elif err_code == 42:
    print(f"[EXTD] Developers Are Still Working On This (42) \nDeveloper Note: {add_msg}")
  else:
    print(f"[EXTD] Oops... Generic Error. See project GitHub for more details. ({err_code}) \nDeveloper Note: {add_msg}")
