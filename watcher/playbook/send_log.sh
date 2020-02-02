#!/bin/bash

URL="{{ post_url }}"
TEXT=$*

data=`cat << EOF
{
    "text": "$TEXT"
}
EOF`

/usr/bin/curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d "$data" $URL

