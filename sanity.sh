#! /bin/sh

# Collection Directory
COLLECTION_DIR="ansible_collections/kube_cloud/haproxy"

# Actual Directory
ACTUAL_DIR=$(pwd)

# Create Collection Directory
mkdir -p $COLLECTION_DIR

# Clean Fir
rm -Rf $COLLECTION_DIR/*

# Copy Collection to Dir
cp -rf meta/ plugins/ roles/ tests/ galaxy.yml LICENSE README.md $COLLECTION_DIR

# Install Requirements


# Start Sanity
cd $COLLECTION_DIR && ansible-test sanity --target-python 3.7 && cd $ACTUAL_DIR && rm -Rf $COLLECTION_DIR