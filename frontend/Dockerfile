# Pull official base image.
FROM node:14.21.3-buster-slim

# Set working directory.
WORKDIR /usr/src/app

# Install dependencies.
COPY package.json .
COPY package-lock.json .
RUN npm clean-install

# Copy app.
COPY . .

# Start app.
ENTRYPOINT ["npm", "start"]
