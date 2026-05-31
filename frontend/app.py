
import streamlit as st
import requests
import json
import os
from datetime import datetime
from pathlib import Path
import uuid

# Page configuration
st.set_page_config(
    page_title="Document Intelligence Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for ChatGPT-like styling
st.markdown("""
<style>
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        gap: 1rem;
    }
    .chat-message.user {
        background-color: #f0f0f0;
        border-left: 4px solid #0084ff;
    }
    .chat-message.assistant {
        background-color: #ffffff;
        border-left: 4px solid #11a37d;
    }
    .chat-message.system {
        background-color: #fef3c7;
        border-left: 4px solid #f59e0b;
    }
    .chat-avatar {
        width: 2rem;
        height: 2rem;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        color: white;
    }
    .user-avatar {
        background-color: #0084ff;
    }
    .assistant-avatar {
        background-color: #11a37d;
    }
    .system-avatar {
        background-color: #f59e0b;
    }
    .file-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        background-color: #e5f3ff;
        border: 1px solid #0084ff;
        border-radius: 1rem;
        font-size: 0.75rem;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    .file-status {
        font-size: 0.85rem;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "conversations" not in st.session_state:
    st.session_state.conversations = {}

if "current_conversation" not in st.session_state:
    st.session_state.current_conversation = None

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# API endpoint
API_BASE_URL = "http://127.0.0.1:8000"
CONVERSATIONS_DIR = "conversations"
os.makedirs(CONVERSATIONS_DIR, exist_ok=True)

# Load conversations from disk
def load_conversations():
    conversations = {}
    for file in os.listdir(CONVERSATIONS_DIR):
        if file.endswith(".json"):
            with open(os.path.join(CONVERSATIONS_DIR, file), "r") as f:
                conv_id = file.replace(".json", "")
                conversations[conv_id] = json.load(f)
    return conversations

# Save conversation to disk
def save_conversation(conv_id, conversation):
    with open(os.path.join(CONVERSATIONS_DIR, f"{conv_id}.json"), "w") as f:
        json.dump(conversation, f, indent=2)

# Create new conversation
def create_new_conversation():
    conv_id = str(uuid.uuid4())[:8]
    st.session_state.conversations[conv_id] = {
        "id": conv_id,
        "title": "New Conversation",
        "created_at": datetime.now().isoformat(),
        "messages": [],
        "files": []
    }
    st.session_state.current_conversation = conv_id
    st.session_state.chat_history = []
    st.session_state.uploaded_files = []  # Clear files for new chat
    st.session_state.upload_processed = None  # Reset upload tracker
    save_conversation(conv_id, st.session_state.conversations[conv_id])
    st.rerun()

# Rename conversation
def rename_conversation(conv_id, new_title):
    st.session_state.conversations[conv_id]["title"] = new_title
    save_conversation(conv_id, st.session_state.conversations[conv_id])

# Delete conversation
def delete_conversation(conv_id):
    if conv_id in st.session_state.conversations:
        del st.session_state.conversations[conv_id]
        os.remove(os.path.join(CONVERSATIONS_DIR, f"{conv_id}.json"))
        if st.session_state.current_conversation == conv_id:
            st.session_state.current_conversation = None
            st.session_state.chat_history = []
        st.rerun()

# Load conversation
def load_conversation(conv_id):
    st.session_state.current_conversation = conv_id
    conversation = st.session_state.conversations.get(conv_id, {})
    st.session_state.chat_history = conversation.get("messages", [])
    
    # Load files and remove duplicates
    files = conversation.get("files", [])
    unique_files = list({f["name"]: f for f in files}.values())
    st.session_state.uploaded_files = unique_files
    st.session_state.upload_processed = None  # Reset upload tracker
    
    # Update conversation to clean up duplicates if any
    if len(unique_files) != len(files):
        conversation["files"] = unique_files
        save_conversation(conv_id, conversation)

# SIDEBAR - Load conversations BEFORE sidebar to avoid rerun issues
if "upload_processed" not in st.session_state:
    st.session_state.upload_processed = None

# Load conversations from disk
st.session_state.conversations = load_conversations()

# SIDEBAR
with st.sidebar:
    st.title("📚 Document RAG Chat")
    
    # New conversation button
    if st.button("➕ New Chat", use_container_width=True, key="new_chat_btn"):
        create_new_conversation()
    
    st.divider()
    
    # File management section
    st.subheader("📄 File Management")
    
    uploaded_file = st.file_uploader(
        "Upload Document",
        type=["pdf", "txt", "docx"],
        key="file_uploader"
    )
    
    if uploaded_file:
        # Only process if this is a new file (not already processed)
        file_id = f"{uploaded_file.name}_{uploaded_file.size}"
        
        if st.session_state.upload_processed != file_id:
            with st.spinner(f"Uploading {uploaded_file.name}..."):
                try:
                    files = {"file": uploaded_file}
                    response = requests.post(f"{API_BASE_URL}/upload", files=files)
                    
                    if response.status_code == 200:
                        st.success(f"✅ {uploaded_file.name} uploaded!")
                        
                        # Add to current conversation (check for duplicates)
                        if st.session_state.current_conversation:
                            conv = st.session_state.conversations[st.session_state.current_conversation]
                            
                            # Check if file already exists
                            file_exists = any(f["name"] == uploaded_file.name for f in st.session_state.uploaded_files)
                            
                            if not file_exists:
                                file_info = {
                                    "name": uploaded_file.name,
                                    "uploaded_at": datetime.now().isoformat()
                                }
                                conv["files"].append(file_info)
                                save_conversation(st.session_state.current_conversation, conv)
                                st.session_state.uploaded_files.append(file_info)
                                st.session_state.upload_processed = file_id
                            else:
                                st.warning(f"📎 {uploaded_file.name} already uploaded")
                                st.session_state.upload_processed = file_id
                    else:
                        st.error("❌ Upload failed")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    # Display uploaded files
    if st.session_state.uploaded_files:
        st.markdown("**Uploaded Files:**")
        # Remove duplicates for display
        seen_files = set()
        unique_files = []
        for f in st.session_state.uploaded_files:
            if f["name"] not in seen_files:
                seen_files.add(f["name"])
                unique_files.append(f)
        
        for idx, file_info in enumerate(unique_files):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f"📎 {file_info['name']}")
            with col2:
                if st.button("❌", key=f"del_file_sidebar_{idx}"):
                    st.session_state.uploaded_files = [
                        f for f in st.session_state.uploaded_files 
                        if f["name"] != file_info["name"]
                    ]
                    if st.session_state.current_conversation:
                        conv = st.session_state.conversations[st.session_state.current_conversation]
                        conv["files"] = st.session_state.uploaded_files
                        save_conversation(st.session_state.current_conversation, conv)
                    st.rerun()
    
    st.divider()
    
    # Conversations history
    st.subheader("💬 Chat History")
    
    if st.session_state.conversations:
        for conv_id, conversation in sorted(
            st.session_state.conversations.items(),
            key=lambda x: x[1].get("created_at", ""),
            reverse=True
        ):
            col1, col2, col3 = st.columns([3, 1, 1])
            
            with col1:
                if st.button(
                    f"💬 {conversation.get('title', 'Untitled')}",
                    key=f"conv_btn_{conv_id}",
                    use_container_width=True
                ):
                    load_conversation(conv_id)
                    st.rerun()
            
            with col2:
                if st.button("✏️", key=f"rename_btn_{conv_id}"):
                    st.session_state[f"editing_{conv_id}"] = True
                    st.rerun()
            
            with col3:
                if st.button("🗑️", key=f"delete_btn_{conv_id}"):
                    delete_conversation(conv_id)
            
            # Edit title
            if st.session_state.get(f"editing_{conv_id}"):
                new_title = st.text_input(
                    "New title",
                    conversation.get("title", ""),
                    key=f"title_input_{conv_id}"
                )
                col_save, col_cancel = st.columns(2)
                with col_save:
                    if st.button("Save", key=f"save_btn_{conv_id}", use_container_width=True):
                        rename_conversation(conv_id, new_title)
                        st.session_state[f"editing_{conv_id}"] = False
                        st.rerun()
                with col_cancel:
                    if st.button("Cancel", key=f"cancel_btn_{conv_id}", use_container_width=True):
                        st.session_state[f"editing_{conv_id}"] = False
                        st.rerun()
    else:
        st.info("No conversations yet. Create one to get started!")

# MAIN CHAT AREA
if not st.session_state.current_conversation:
    st.title("🤖 Document Intelligence Chatbot")
    st.info("👈 Create a new chat from the sidebar to get started!")
else:
    # Display conversation title
    conversation = st.session_state.conversations[st.session_state.current_conversation]
    st.title(f"💬 {conversation.get('title', 'Chat')}")
    
    # Display uploaded files
    if st.session_state.uploaded_files:
        st.markdown("**📚 Active Documents:**")
        # Remove duplicates for display
        unique_files = list({f["name"]: f for f in st.session_state.uploaded_files}.values())
        files_str = " • ".join([f["name"] for f in unique_files])
        st.markdown(files_str)
    
    # Chat display area
    st.markdown("---")
    chat_container = st.container()
    
    with chat_container:
        for message in st.session_state.chat_history:
            role = message.get("role", "user")
            content = message.get("content", "")
            
            if role == "user":
                st.markdown(f"""
                <div class="chat-message user">
                    <div class="chat-avatar user-avatar">👤</div>
                    <div style="flex: 1;">
                        <div style="font-weight: bold; margin-bottom: 0.5rem;">You</div>
                        <div>{content}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="chat-message assistant">
                    <div class="chat-avatar assistant-avatar">🤖</div>
                    <div style="flex: 1;">
                        <div style="font-weight: bold; margin-bottom: 0.5rem;">Assistant</div>
                        <div>{content}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Chat input area
    col1, col2 = st.columns([5, 1])
    
    with col1:
        question = st.text_input(
            "Ask a question about your documents...",
            placeholder="Type your message here...",
            key="chat_input"
        )
    
    with col2:
        send_button = st.button("Send", use_container_width=True, key="send_btn")
    
    # Handle message sending
    if send_button and question:
        # Add user message to history
        st.session_state.chat_history.append({
            "role": "user",
            "content": question
        })
        
        # Get response from API
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    f"{API_BASE_URL}/chat",
                    params={"query": question}
                )
                
                if response.status_code == 200:
                    answer = response.json().get("answer", "No response")
                else:
                    answer = f"Error: {response.status_code}"
                
            except Exception as e:
                answer = f"Error connecting to server: {str(e)}"
        
        # Add assistant message to history
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": answer
        })
        
        # Save to conversation
        conversation["messages"] = st.session_state.chat_history
        
        # Auto-generate title from first question
        if len(st.session_state.chat_history) == 2:
            title = question[:50]
            if len(question) > 50:
                title += "..."
            conversation["title"] = title
        
        save_conversation(st.session_state.current_conversation, conversation)
        st.rerun()
    
    # Clear conversation button
    if st.button("🧹 Clear Chat", use_container_width=True, key="clear_chat_btn"):
        st.session_state.chat_history = []
        conversation["messages"] = []
        save_conversation(st.session_state.current_conversation, conversation)
        st.rerun()