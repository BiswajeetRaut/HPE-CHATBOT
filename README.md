# HPE-CHATBOT

An interactive chatbot platform for HPE Primera and Alletra products, providing users with real-time responses and assistance for their queries and doubts.

## Features

- User Authentication: Users can register and log in using their credentials. Firebase authentication is used to handle user authentication and secure user data.

- Sidebar: The sidebar displays a list of existing chat conversations. It allows users to view and manage their chats.

- Chat Window: The chat window is where users can interact with the chatbot and view chat messages. It supports real-time synchronization of messages and scrolling to the latest message.

- Chat Management: Users can create new chat conversations and delete existing ones. The chat management options are accessible through the chat window.

- Real-time Updates: The application leverages Firebase Firestore to synchronize chat messages in real-time. When a new message is sent or received, it is immediately updated and displayed in the chat window.

- AI Integration: The chatbot's responses are powered by an external API for natural language processing and AI capabilities. It provides intelligent and context-aware responses to user queries.

## Prerequisites

Before running the application, ensure that you have the following prerequisites installed on your machine:

- Node.js: Make sure you have Node.js installed. You can download it from the official website: https://nodejs.org/

- npm: npm (Node Package Manager) is bundled with Node.js. It is used to install project dependencies.

## Installation

1. Clone the repository:

git clone (https://github.com/BiswajeetRaut/HPE-CHATBOT.git)

2. Navigate to the project directory:

cd frontend

3. Install dependencies:

npm install or yarn install
  
4. Configure Firebase credentials:

   - Create a Firebase project on the Firebase console (https://console.firebase.google.com/) if you haven't already.

   - Obtain the Firebase configuration credentials (apiKey, authDomain, projectId, etc.) for your project.

   - Open the `firebase.js` file located in the `src/` directory.

   - Replace the placeholder values with your Firebase configuration credentials.

5. Start the development server:

npm run dev or yarn run dev

6. Access the application:

   - Open your preferred web browser.

   - Enter the following URL: `http://localhost:3000`

   - The Chat Application should now be running and accessible in your browser.

7. Now go to server directory:

   cd server
   
8. Install dependencies:

   npm / yarn install
   
9. Run the server:

   npm run dev

## File Structure

The codebase is structured as follows:

- `src/`: Contains the source code for the application.

  - `components/`: Holds the React components used in the application.

    - `Chat.jsx`: Renders the main chat window and handles chat-related functionalities.

    - `Chatwindow.jsx`: Renders the chat messages and handles sending and receiving messages.

    - `Sidebar.jsx`: Renders the sidebar with a list of chats and chat management options.

  - `features/`: Contains Redux features and slices for managing user state.

    - `user/`: Manages user authentication and user data.

      - `userSlice.js`: Defines Redux actions, reducers, and selectors for user state.

  - `firebase.js`: Handles Firebase configuration and exports the Firebase instance.

  - `App.js`: The root component of the application.

  - `index.js`: Renders the App component and mounts it to the DOM.

## Usage

Here is a step-by-step guide on how to use the Chat Application:

1. LogIn: On the landing page, you can register a new account or log in with your Google Account.

2. Sidebar: After logging in, you will be redirected to the main dashboard. The sidebar displays a list of your chat conversations.

3. Open a chat: Click on a chat conversation in the sidebar to open the chat window for that particular chat.

4. Interact with the chatbot: In the chat window, you can type messages in the input field at the bottom. Press the "Send" button or hit Enter to send your message. The chatbot will respond with an AI-generated reply.

5. Real-time updates: All chat messages are synchronized in real-time. Whenever a new message is sent or received, it will automatically appear in the chat window, and the window will scroll to the latest message.

6. Create a new chat: To create a new chat conversation, click on the "New Chat" button in the welcome section of the chat window. Follow the prompts to enter a name for the new chat.

7. Delete a chat: If you wish to delete a chat, click on the "View Chats" button in the welcome section of the chat window. This will open the sidebar, where you can select and delete individual chat conversations.
  
## Technologies

The Chat Application was developed using the following technologies and resources:

- React (https://reactjs.org/): A JavaScript library for building user interfaces.

- Redux (https://redux.js.org/): A predictable state container for JavaScript applications.

- Firebase (https://firebase.google.com/): A cloud-based platform for building web and mobile applications. It provides authentication, real-time database, and hosting services.

- External API (Our ChatBot API): An API that powers the AI capabilities and natural language processing of the chatbot.
  
## Figma Design

The design for the Chat Application can be found in the following Figma project: [HPE CTY Chatbot](https://www.figma.com/file/F1Ze5XJ4xLxYv260ZkO9rF/HPE-CTY-Chatbot?type=design&node-id=0-1&t=Ar2rxjIVGQGiLAPj-0)


## Contributors

This project was developed by:

- [Biswajeet Raut](https://github.com/BiswajeetRaut)

- [Soham Bhattacharjee](https://github.com/thunderfreak)






