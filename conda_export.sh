# set EXPORT_TEXT variable to the results of conda env export
EXPORT_TEXT=$(conda env export | grep -v "^prefix: ")

# replace invokeai in EXPORT_TEXT with image-ai
EXPORT_TEXT=${EXPORT_TEXT//invokeai/image-ai}

# save to environment.yml
echo "$EXPORT_TEXT" > environment.yml