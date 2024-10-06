# Stage 1: Build the React app
FROM node:18 AS build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json / yarn.lock
COPY package.json /app/package.json
COPY yarn.lock /app/yarn.lock
# Install dependencies
RUN yarn install

# Copy the rest of the React app source code
COPY . .

# Build the app for production
RUN yarn build

# Stage 2: Serve the app with Nginx
FROM nginx:stable-alpine

# Copy the build output to the Nginx web root
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80 for the container
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
