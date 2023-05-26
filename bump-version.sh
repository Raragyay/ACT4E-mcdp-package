#!/usr/bin/env bash

# Get the latest tag from git
VERSION=`git describe --tags $(git rev-list --tags --max-count=1)`

# Remove the 'v' prefix if your tags use it (like v1.0.0)
VERSION=${VERSION#v}

# Call bumpversion with the --current-version option
bumpversion --verbose --current-version "$VERSION" patch
