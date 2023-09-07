# Use an official Ubuntu as a parent image
FROM ubuntu:latest

# Update package lists and install fontconfig
RUN apt-get update && apt-get install -y fontconfig