# IMPLEMENTED SECURITY FEATURES

## X-FRAME-OPTIONS
Using the "django.middleware.clickjacking.XFrameOptionsMiddleware" sets the X-frame-options of the webapp sites to DENY to prevent clickjacking

## SECURE_CONTENT_TYPE_NOSNIFF
Setting this to true prevents the browser from guessing the content type and forcing it to always use the type provided in the contenttype header

### CSRF TOKENS
All forms contains {% csrf_token %} to protect against CSRF attacks

### DJANGO ORM
Django ORM is used to properly parameterize queries to avoid SQL injection

### 