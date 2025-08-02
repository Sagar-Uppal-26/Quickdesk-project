import streamlit as st
import uuid
import json
import os
from typing import Dict, List

TICKET_FILE = "tickets.json"
USER_ROLE = "user"
SUPPORT_ROLE = "support"
CREDENTIALS_FILE = "users.json"

# ---------- Load & Save Functions ----------

def load_tickets() -> Dict[str, List[dict]]:
    if os.path.exists(TICKET_FILE):
        with open(TICKET_FILE, "r") as f:
            return json.load(f)
    return {}

def save_tickets(ticket_db: Dict[str, List[dict]]):
    with open(TICKET_FILE, "w") as f:
        json.dump(ticket_db, f, indent=2)

def load_users() -> Dict[str, Dict[str, str]]:
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "r") as f:
            return json.load(f)
    return {
        "user1": {"password": "userpass", "role": USER_ROLE},
        "support_agent": {"password": "supportpass", "role": SUPPORT_ROLE}
    }

def save_users(user_db: Dict[str, Dict[str, str]]):
    with open(CREDENTIALS_FILE, "w") as f:
        json.dump(user_db, f, indent=2)

# Load database on startup
ticket_db = load_tickets()
user_db = load_users()

# ---------- Core Ticket Functions ----------

def open_ticket(username: str, title: str, description: str) -> str:
    ticket = {
        "ticket_id": str(uuid.uuid4())[:8],
        "title": title,
        "status": "open",
        "comments": [{"by": username, "text": description}]
    }
    if username not in ticket_db:
        ticket_db[username] = []
    ticket_db[username].append(ticket)
    save_tickets(ticket_db)
    return ticket["ticket_id"]

def close_ticket(username: str, ticket_id: str, role: str) -> bool:
    for user, tickets in ticket_db.items():
        for ticket in tickets:
            if ticket["ticket_id"] == ticket_id:
                if role == SUPPORT_ROLE or (role == USER_ROLE and user == username):
                    ticket["status"] = "closed"
                    save_tickets(ticket_db)
                    return True
    return False

def add_comment(username: str, ticket_id: str, role: str, comment: str) -> bool:
    for user, tickets in ticket_db.items():
        for ticket in tickets:
            if ticket["ticket_id"] == ticket_id:
                if role == SUPPORT_ROLE or (role == USER_ROLE and user == username):
                    ticket["comments"].append({"by": username, "text": comment})
                    save_tickets(ticket_db)
                    return True
    return False

def get_tickets(username: str, role: str) -> Dict[str, List[dict]]:
    if role == SUPPORT_ROLE:
        return ticket_db
    return {username: ticket_db.get(username, [])}

# ---------- Ticket UI Component ----------

def ticket_display(ticket: dict, current_user: str, role: str):
    with st.expander(f"[{ticket['status'].upper()}] {ticket['title']} - ID: {ticket['ticket_id']}"):
        st.write("### Comments")
        for c in ticket["comments"]:
            author = c["by"]
            st.markdown(f"- **{author}:** {c['text']}")

        if ticket["status"] == "open":
            comment = st.text_input(f"Add comment (ID: {ticket['ticket_id']})", key=f"comment_{ticket['ticket_id']}")
            if comment and st.button("Post Comment", key=f"btn_comment_{ticket['ticket_id']}"):
                success = add_comment(current_user, ticket["ticket_id"], role, comment)
                if success:
                    st.success("Comment added.")
                    st.rerun()

            if st.button("Close Ticket", key=f"btn_close_{ticket['ticket_id']}"):
                closed = close_ticket(current_user, ticket["ticket_id"], role)
                if closed:
                    st.success("Ticket closed.")
                    st.rerun()

# ---------- Streamlit App UI ----------

st.set_page_config(page_title="Ticketing Agent", layout="centered")
st.title("🎫 Ticketing Board")

# ---------- Authentication ----------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.username = ""
    st.session_state.role = ""

if not st.session_state.authenticated:
    tabs = st.tabs(["Login", "Register"])

    with tabs[0]:
        with st.form("login_form"):
            st.subheader("🔐 Login")
            username = st.text_input("Username", key="login_user")
            password = st.text_input("Password", type="password", key="login_pass")
            submitted = st.form_submit_button("Login")
            if submitted:
                user = user_db.get(username)
                if user and user["password"] == password:
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    st.session_state.role = user["role"]
                    st.rerun()
                else:
                    st.error("Invalid username or password")

    with tabs[1]:
        with st.form("register_form"):
            st.subheader("🆕 Register as User")
            new_username = st.text_input("New Username", key="reg_user")
            new_password = st.text_input("New Password", type="password", key="reg_pass")
            confirm_password = st.text_input("Confirm Password", type="password", key="reg_pass2")
            register = st.form_submit_button("Register")
            if register:
                if new_username in user_db:
                    st.warning("Username already exists.")
                elif new_password != confirm_password:
                    st.warning("Passwords do not match.")
                elif not new_username or not new_password:
                    st.warning("Please fill in all fields.")
                else:
                    user_db[new_username] = {"password": new_password, "role": USER_ROLE}
                    save_users(user_db)
                    st.success("User registered successfully. You can now log in.")

elif st.session_state.authenticated:
    st.sidebar.success(f"Logged in as: {st.session_state.username} ({st.session_state.role})")
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.username = ""
        st.session_state.role = ""
        st.rerun()

    username = st.session_state.username
    role = st.session_state.role

    st.divider()

    if role == SUPPORT_ROLE:
        st.subheader("👤 Register New Support Agent")
        with st.form("register_support"):
            agent_username = st.text_input("Support Username", key="agent_user")
            agent_password = st.text_input("Support Password", type="password", key="agent_pass")
            confirm_password = st.text_input("Confirm Password", type="password", key="agent_pass2")
            reg = st.form_submit_button("Register Support Agent")
            if reg:
                if agent_username in user_db:
                    st.warning("Support username already exists.")
                elif agent_password != confirm_password:
                    st.warning("Passwords do not match.")
                elif not agent_username or not agent_password:
                    st.warning("Please fill in all fields.")
                else:
                    user_db[agent_username] = {"password": agent_password, "role": SUPPORT_ROLE}
                    save_users(user_db)
                    st.success("Support agent registered successfully.")

    if role == USER_ROLE:
        st.subheader("📝 Open a New Ticket")
        with st.form("new_ticket_form"):
            title = st.text_input("Ticket Title")
            description = st.text_area("Describe the issue")
            submit = st.form_submit_button("Submit Ticket")
            if submit and title and description:
                ticket_id = open_ticket(username, title, description)
                st.success(f"Ticket created with ID: {ticket_id}")
                st.rerun()

    st.subheader("📂 View Tickets")
    tickets = get_tickets(username, role)
    if not tickets:
        st.info("No tickets available.")
    else:
        for user, ticket_list in tickets.items():
            for ticket in ticket_list:
                ticket_display(ticket, username, role)
