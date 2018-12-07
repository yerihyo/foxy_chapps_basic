#!/bin/bash -eu

branch_fullname=$(git symbolic-ref -q HEAD)
branch_name=${branch_fullname##refs/heads/}
echo "$branch_name"
