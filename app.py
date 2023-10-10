from flask import Flask, render_template

app = Flask(__name__)

# Sample data for demonstration
sample_data = {
    'title': 'Frognite Flask',
    'message': 'This is a description of what we will use flask for',
    'items': [
        {1: 'Backend Server', 'Flask can serve as the backend server for our game. It handles incoming requests from the frontend, processes them, and sends back the appropriate responses. This includes managing user authentication, game state, and interactions.': ''},
        {2: 'API Endpoints', ' You can use Flask to create RESTful API endpoints that allow the frontend to communicate with the backend. This is crucial for tasks like retrieving player data, updating game state, and handling multiplayer interactions.':''},
        {3: 'Database Integration', 'Flask can work in conjunction with a database (such as SQLite, PostgreSQL, or MySQL) to store and manage game-related data. This could include player profiles, character statistics, and game progress.':''},
        {4: 'User Authentication','Flask provides tools for implementing user authentication and authorization. This ensures that players can create accounts, log in, and securely access their profiles and game progress.':''},
        {5: 'Session Management','Flask enables us to manage user sessions, which is important for tracking logged-in users and maintaining their state across different interactions with the game.':''},
        {6: 'Error Handling and Logging','Flask provides mechanisms for handling errors and logging, which is crucial for identifying and troubleshooting issues within the backend code.':''},
        {7: 'RESTful Routing','Flask allows us to define routes that correspond to specific actions or resources in our game. This helps in organizing the backend logic and ensures that each API endpoint serves a specific purpose.':''},
        {8: 'Integration with External Services','If our game ends up requiring integration with external services (e.g., payment gateways, social media platforms), Flask can facilitate these connections.':''},
        {9: 'Websockets and Real-time Communication','While Flask itself is not designed for real-time communication, we can use extensions like Flask-SocketIO to implement real-time features in our game, such as live updates, chat, or notifications.':''},
        {10: 'Testing and Debugging','Flask has built-in support for unit testing, which can help ensure the reliability and stability of your backend code. It also provides debugging tools to identify and resolve issues during development.':''},
    ]
}

@app.route('/')
def home():
    # Render the 'index.html' template with dynamic data
    return render_template('index.html', data=sample_data)

if __name__ == '__main__':
    app.run(debug=True)
    