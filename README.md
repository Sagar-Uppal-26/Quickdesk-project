# 🎫 Streamlit Ticketing System

A lightweight, role-based support ticketing application built with Python and Streamlit. Users can register, open and manage their own support tickets, while support agents have a global view and can manage tickets across all users.

#### Checkout the deployed version here: https://ticketingsystem.streamlit.app/

## ✨ Features

* 🔐 **User & Support Agent Authentication**

  * Users and support agents can register and log in.
  * Users can open, comment, and close only their own tickets.
  * Support agents can view, comment on, and close all tickets.
  * Support agents can register other support agents.

* 🧲 **Ticket Management**

  * Create new tickets with a title and description.
  * Add comments to tickets.
  * Close tickets when resolved.
  * View the full history of comments on each ticket.

* 📁 **Persistent Storage**

  * Tickets and user credentials are saved locally in JSON files:

    * `tickets.json` — all ticket data
    * `users.json` — user credentials and roles

## 📂 Folder Structure

```
.
├── tickets.json           # Auto-generated ticket storage
├── users.json             # Auto-generated user credentials storage
├── app.py                 # Main Streamlit application
├── README.md              # You're here!
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/streamlit-ticketing-system.git
cd streamlit-ticketing-system
```

### 2. Create and Activate a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install streamlit
```

### 4. Run the App

```bash
streamlit run app.py
```

This will launch a browser window with the full ticketing system UI.

## 🧪 Usage Guide

### 👤 Register or Login

* On first launch, you can:

  * Register as a **User** using the **Register** tab.
  * Login as `support_agent` with default password `supportpass` (can be changed or removed).

### 📝 Users Can:

* Register via the **Register** tab
* Log in to their account
* Open new tickets with a title and description
* Comment on their own open tickets
* Close their own tickets
* View ticket history

### 🛠️ Support Agents Can:

* Log in using predefined or registered credentials
* View all users’ tickets
* Comment on any open ticket
* Close any ticket
* Register new support agents

## 🗂️ Data Persistence

No database required — data is stored locally in:

* `tickets.json` — structured as:

```json
{
  "user1": [
    {
      "ticket_id": "abc123",
      "title": "Issue Title",
      "status": "open",
      "comments": [
        {"by": "user1", "text": "Initial message"},
        {"by": "support_agent", "text": "We are looking into it"}
      ]
    }
  ]
}
```

* `users.json` — stores user credentials and roles:

```json
{
  "user1": {"password": "userpass", "role": "user"},
  "support_agent": {"password": "supportpass", "role": "support"}
}
```

## 🔒 Notes on Security

This is a prototype and **not suitable for production without**:

* Secure password hashing
* Proper user session handling
* CSRF protection and HTTPS deployment

## 🛠️ Built With

* [Python 3.8+](https://www.python.org/)
* [Streamlit](https://streamlit.io/)

## 📌 Future Enhancements

* Admin dashboard and ticket filtering
* Email notifications
* Attachments (e.g., screenshots)
* Database backend (SQLite / PostgreSQL)
* JWT-based authentication

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

Built with ❤️ using Streamlit by Sagar Uppal.
