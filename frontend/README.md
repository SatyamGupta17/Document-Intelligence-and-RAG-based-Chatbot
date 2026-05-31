# Document Intelligence Chatbot - ChatGPT-like UI Guide

## 🎯 Overview

The updated frontend provides a modern, ChatGPT-inspired interface for the Document RAG Chatbot with the following features:

- ✅ **ChatGPT-like UI Design** - Familiar conversation interface
- ✅ **Chat History Storage** - Persistent conversation management
- ✅ **Multiple Conversations** - Manage multiple chat sessions
- ✅ **File Management** - Upload and organize documents
- ✅ **RAG-based Analysis** - Intelligent document analysis for everyone
- ✅ **Search & Export** - Find and export conversations

---

## 🚀 Features

### 1. **Sidebar Navigation**
- **New Chat Button** - Start a fresh conversation anytime
- **File Management** - Upload, view, and manage documents
- **Conversation History** - Browse all previous chats
- **Quick Actions** - Rename, edit, or delete conversations

### 2. **Main Chat Area**
- **Message Display** - User and assistant messages with clear avatars
- **Conversation Title** - Auto-generated or manually editable
- **Active Documents** - See which files are being analyzed
- **Input Field** - Type questions naturally
- **Clear Chat** - Start fresh within a conversation

### 3. **File Management**
- **Multi-format Support** - PDF, TXT, DOCX files
- **Upload Progress** - Visual feedback during upload
- **File Listing** - View all uploaded documents
- **Quick Delete** - Remove files with one click
- **Conversation-scoped Files** - Each chat can have its own documents

### 4. **Chat History**
- **Auto-save** - Conversations saved automatically
- **Persistent Storage** - History survives app restarts
- **Quick Search** - Find past conversations
- **Metadata** - Timestamps and conversation stats
- **Export Options** - Save conversations as JSON or TXT

---

## 📋 Quick Start

### Starting the Application

1. **Start the FastAPI backend:**
```bash
cd d:\Tech stack\Document-rag
python -m uvicorn app.main:app --reload
```

2. **Start the Streamlit frontend (in another terminal):**
```bash
cd d:\Tech stack\Document-rag\frontend
streamlit run app.py
```

3. **Open in browser:**
   - Streamlit will open at `http://localhost:8501`

---

## 💬 Using the Chat Interface

### Create a New Chat
1. Click **"➕ New Chat"** in the sidebar
2. A new conversation will be created automatically
3. Start typing your questions

### Upload Documents
1. Click **"Upload Document"** in the File Management section
2. Select a PDF, TXT, or DOCX file
3. Wait for the upload confirmation
4. The file will appear in the "Uploaded Files" list
5. Ask questions about the document

### Ask Questions
1. Type your question in the input field
2. Click **"Send"** or press Enter
3. The assistant will analyze the documents using RAG and respond
4. Both user and assistant messages are automatically saved

### Manage Conversations
- **View History** - Click on any conversation in the sidebar
- **Rename** - Click the pencil (✏️) icon
- **Delete** - Click the trash (🗑️) icon
- **Clear Chat** - Remove all messages from current conversation

---

## 📁 File Structure

```
frontend/
├── app.py                      # Main Streamlit application
├── conversation_manager.py     # Conversation management utilities
└── ../conversations/           # Chat history storage (auto-created)
    ├── abc12345.json          # Individual conversation files
    └── def67890.json
```

---

## 💾 Conversation Storage

Conversations are stored as JSON files in the `conversations/` directory:

```json
{
  "id": "abc12345",
  "title": "Understanding Cloud Architecture",
  "created_at": "2024-05-31T10:30:00.000000",
  "updated_at": "2024-05-31T10:45:00.000000",
  "messages": [
    {
      "role": "user",
      "content": "What is cloud computing?",
      "timestamp": "2024-05-31T10:30:00.000000"
    },
    {
      "role": "assistant",
      "content": "Cloud computing is...",
      "timestamp": "2024-05-31T10:30:05.000000"
    }
  ],
  "files": [
    {
      "name": "cloud_guide.pdf",
      "uploaded_at": "2024-05-31T10:30:00.000000"
    }
  ],
  "metadata": {
    "message_count": 2,
    "file_count": 1
  }
}
```

---

## 🎨 UI Components

### User Message
- **Background**: Light gray (#f0f0f0)
- **Border**: Blue accent (#0084ff)
- **Avatar**: 👤 Blue circle

### Assistant Message
- **Background**: White (#ffffff)
- **Border**: Green accent (#11a37d)
- **Avatar**: 🤖 Green circle

### System Alerts
- **Background**: Yellow (#fef3c7)
- **Border**: Orange accent (#f59e0b)
- **Avatar**: ⚠️ Orange circle

---

## 🔧 Advanced Usage

### Using the Conversation Manager Programmatically

```python
from frontend.conversation_manager import ConversationManager

# Create manager
manager = ConversationManager()

# Create new conversation
conv_id = manager.create_conversation(title="My Research")

# Add messages
manager.add_message(conv_id, "user", "What is machine learning?")
manager.add_message(conv_id, "assistant", "Machine learning is...")

# Add files
manager.add_file(conv_id, "ml_guide.pdf")

# Get statistics
stats = manager.get_statistics()
print(stats)
# Output: {'total_conversations': 5, 'total_messages': 23, ...}

# Search conversations
results = manager.search_conversations("machine learning")

# Export conversation
json_export = manager.export_conversation(conv_id, format="json")
txt_export = manager.export_conversation(conv_id, format="txt")

# Delete conversation
manager.delete_conversation(conv_id)
```

---

## 🔌 API Integration

The frontend communicates with the FastAPI backend via two main endpoints:

### Upload Endpoint
```
POST /upload
- Uploads a document file
- Returns: {"message": "File processed successfully"}
```

### Chat Endpoint
```
POST /chat?query={question}
- Sends a query to the RAG system
- Returns: {"answer": "Generated response"}
```

---

## ⚙️ Configuration

### Customize API URL
Edit `app.py` line 60:
```python
API_BASE_URL = "http://127.0.0.1:8000"  # Change if backend is on different host
```

### Customize Storage Location
Edit `app.py` line 62:
```python
CONVERSATIONS_DIR = "conversations"  # Change storage directory
```

### Customize Supported File Types
Edit `app.py` line 97:
```python
type=["pdf", "txt", "docx"]  # Add or remove file types
```

---

## 🐛 Troubleshooting

### Issue: "Error connecting to server"
**Solution:** Make sure the FastAPI backend is running:
```bash
python -m uvicorn app.main:app --reload
```

### Issue: Files not uploading
**Solution:** Check that the `uploads/` directory exists and has write permissions

### Issue: Chat history not saving
**Solution:** Ensure the `conversations/` directory is writable. Check file permissions.

### Issue: Conversations lost after restart
**Solution:** Check if `conversations/` directory is being deleted. Files should persist automatically.

---

## 📊 Example Workflow

1. **Click "➕ New Chat"** → Creates new conversation
2. **Upload "annual_report.pdf"** → File added to conversation
3. **Ask "What were the key achievements?"** → RAG analyzes document
4. **Review response** → Automatically saved to chat history
5. **Ask follow-up questions** → Full context maintained
6. **Click conversation name** → See it in sidebar history
7. **Click "✏️"** → Rename to "2024 Annual Report Analysis"
8. **Start new chat** → Previous chat remains in history
9. **Click saved chat** → Resume conversation anytime

---

## 🎓 Best Practices

- **Organize by Topic** - Use clear conversation titles for easy finding
- **Group Related Files** - Upload related documents to the same conversation
- **Ask Follow-ups** - Build on previous questions for better context
- **Export Important Chats** - Save key conversations as backups
- **Regular Cleanup** - Delete old conversations you no longer need

---

## 🚀 Future Enhancements

- [ ] Conversation sharing/collaboration
- [ ] Advanced search with filters
- [ ] Conversation templates
- [ ] Bulk file uploads
- [ ] Message reactions/feedback
- [ ] Voice input support
- [ ] Dark mode theme
- [ ] API key management for multi-user

---

## 📞 Support

For issues or feature requests, please check:
1. Backend logs for errors
2. Browser console for JavaScript errors
3. Conversation storage directory permissions

---

**Happy analyzing! 🚀**
