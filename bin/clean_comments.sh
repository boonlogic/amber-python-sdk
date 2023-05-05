#!/usr/bin/env bash

# removes all noqa in files

if [ "$(uname)" == "Darwin" ]; then
    # Do something under Mac OS X platform 
    sed -i '' -e 's/  # noqa: E501.*$//g' boonamber/v2/*.py boonamber/v2/models/*.py
    sed -i '' -e "s/'str'/bytes/g" boonamber/v2/api/default_api.py
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    # Do something under GNU/Linux platform
    sed -i 's/  # noqa: E501.*$//g' boonamber/v2/*.py boonamber/v2/models/*.py
    sed -i "s/'str'/bytes/g" boonamber/v2/api/default_api.py
fi

rm test/test_default_api.py
rm docs/*.md