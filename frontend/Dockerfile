# Use the official Node.js image as a base
FROM node:20

# Set the working directory to /app
WORKDIR /app

# Copy the package*.json files to the working directory
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the code to the working directory
COPY . .

# Expose the port that the app will run on
EXPOSE 3000

# Run the command to start the app
CMD ["npm", "start"]
