# Quick Start Guide - Document RAG Chatbot

## 5-Minute Setup

### Prerequisites
- Python 3.8+
- Virtual environment activated
- Dependencies installed

### Step 1: Start Backend (Terminal 1)
```bash
cd d:\Tech stack\Document-rag
python -m uvicorn app.main:app --reload --port 8000
```

Expected output:
```
INFO:     Application startup complete
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### Step 2: Start Frontend (Terminal 2)
```bash
cd d:\Tech stack\Document-rag\frontend
streamlit run app.py
```

Expected output:
```
Local URL: http://localhost:8501
```

### Step 3: Open Browser
Navigate to `http://localhost:8501` - The UI will load automatically

---

## First Time User Workflow

### 1. Create New Chat
- Click **"➕ New Chat"** button in sidebar
- A new conversation is created automatically

### 2. Upload a Document
- Click **"Upload Document"** area
- Select a PDF, TXT, or DOCX file
- Wait for upload confirmation (✅ message)

### 3. Ask Your First Question
- Type a question about your document
- Example: "What is the main topic of this document?"
- Click **"Send"** button

### 4. View Response
- The AI will analyze your document
- Response will appear in the chat
- Both messages are automatically saved

### 5. Continue Conversation
- Ask follow-up questions
- Context is maintained throughout the conversation
- All messages are saved

---

## Key Features

### 💬 Chat Management
| Feature | How to Use |
|---------|-----------|
| New Chat | Click ➕ New Chat button |
| View History | Click conversation in sidebar |
| Rename Chat | Click ✏️ pencil icon |
| Delete Chat | Click 🗑️ trash icon |
| Clear Messages | Click 🧹 Clear Chat button |

### 📄 File Management
| Feature | How to Use |
|---------|-----------|
| Upload | Click "Upload Document" |
| View Files | See list under "Uploaded Files" |
| Remove File | Click ❌ next to filename |
| Multiple Files | Upload several per chat |

### 💾 Persistence
- All chats auto-save to `conversations/` folder
- Messages persist after app restart
- No manual saving needed

---

## Common Tasks

### How to search old conversations?
1. Look through sidebar conversation list
2. Scroll up to see older chats
3. Click any chat to resume
4. Use Ctrl+F in browser to search

### How to export a conversation?
1. Copy the entire conversation text
2. Right-click → Save As in browser
3. Or manually copy messages to text editor

### How to upload multiple files at once?
1. Upload first file (wait for confirmation)
2. Click "Upload Document" again
3. Select next file
4. Repeat for each file

### How to delete specific messages?
- Clear entire conversation: Click 🧹 Clear Chat
- Delete single message: Not supported (delete chat and start fresh)

### How to rename a conversation after creation?
1. Click ✏️ pencil icon next to conversation name
2. Enter new title
3. Click "Save"

---

## Troubleshooting

### ❌ "Error connecting to server"
**Problem:** Backend not running
**Solution:**
```bash
# Terminal 1 - Check if running
python -m uvicorn app.main:app --reload --port 8000
```

### ❌ "Upload failed"
**Problem:** File too large or invalid format
**Solution:**
- Check file size (max 50MB default)
- Supported formats: PDF, TXT, DOCX
- Check `uploads/` folder permissions

### ❌ "Chat not saving"
**Problem:** Conversations directory permission issue
**Solution:**
```bash
# Check directory exists
dir conversations
# Create if missing
mkdir conversations
```

### ❌ "Responses are empty"
**Problem:** Backend not processing correctly
**Solution:**
- Check backend logs for errors
- Ensure document uploaded successfully
- Restart both frontend and backend

### ❌ "Streamlit keeps crashing"
**Problem:** Memory or package issue
**Solution:**
```bash
# Clear Streamlit cache
streamlit cache clear

# Restart app
streamlit run app.py
```

---

## Tips & Tricks

### 🎯 Get Better Responses
- Be specific in your questions
- Ask one question at a time
- Reference specific parts of the document
- Ask follow-up questions for more context

### 📚 Organize Your Work
- Use clear conversation titles
- Group related documents in same chat
- Create new chats for different topics
- Use sidebar to quickly switch between chats

### ⚡ Work Efficiently
- Use keyboard shortcut: Type your question and press Enter
- Click "Send" button or press Enter to send
- Sidebar stays visible during chat
- Drag browser window edges to resize

### 💡 Best Practices
- Upload documents before asking questions
- Check "Active Documents" section shows your files
- Start with a general question to understand content
- Ask specific questions about details
- Review responses carefully for accuracy

---

## System Requirements

- **Memory:** Minimum 4GB RAM
- **Storage:** 500MB free space
- **Internet:** Local machine only (no external internet needed)
- **Ports:** 8000 (backend), 8501 (frontend)
- **Python:** 3.8 or higher

---

## File Structure

```
Document-rag/
├── app/                    # Backend RAG system
│   ├── main.py            # FastAPI application
│   ├── rag.py             # RAG logic
│   └── ...
├── frontend/              # Frontend application
│   ├── app.py             # Main Streamlit app
│   ├── conversation_manager.py
│   ├── config.py
│   ├── ui_components.py
│   └── README.md
├── conversations/         # Chat history (auto-created)
│   └── *.json            # Individual chats
└── uploads/              # Uploaded documents
```

---

## Next Steps

1. **Customize Configuration**
   - Edit `frontend/config.py` for API URL, file limits, etc.

2. **Integrate with Your Documents**
   - Upload your specific documents
   - Test different question types

3. **Deploy to Production**
   - Set up proper database
   - Configure authentication
   - Use cloud hosting (Azure, AWS, etc.)

4. **Extend Functionality**
   - Add more file type support
   - Implement user authentication
   - Add conversation sharing
   - Build admin dashboard

---

## Support

For issues:
1. Check console for error messages
2. Review troubleshooting section above
3. Check backend logs: Terminal 1
4. Check frontend logs: Streamlit terminal

---

**You're ready to go! Happy analyzing! 🚀**
