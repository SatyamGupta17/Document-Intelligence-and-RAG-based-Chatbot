"""
UI utility functions and components for the chatbot
"""

import streamlit as st
from typing import Optional, List
from datetime import datetime


def render_chat_message(role: str, content: str, timestamp: Optional[str] = None):
    """Render a chat message with proper styling"""
    
    if role == "user":
        st.markdown(f"""
        <div class="chat-message user">
            <div class="chat-avatar user-avatar">👤</div>
            <div style="flex: 1;">
                <div style="font-weight: bold; margin-bottom: 0.5rem;">You
                {f'<span style="font-size: 0.75rem; color: #999; margin-left: 0.5rem;">{timestamp}</span>' if timestamp else ''}
                </div>
                <div>{content}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    elif role == "assistant":
        st.markdown(f"""
        <div class="chat-message assistant">
            <div class="chat-avatar assistant-avatar">🤖</div>
            <div style="flex: 1;">
                <div style="font-weight: bold; margin-bottom: 0.5rem;">Assistant
                {f'<span style="font-size: 0.75rem; color: #999; margin-left: 0.5rem;">{timestamp}</span>' if timestamp else ''}
                </div>
                <div>{content}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    elif role == "system":
        st.markdown(f"""
        <div class="chat-message system">
            <div class="chat-avatar system-avatar">ℹ️</div>
            <div style="flex: 1;">
                <div style="font-weight: bold; margin-bottom: 0.5rem;">System
                {f'<span style="font-size: 0.75rem; color: #999; margin-left: 0.5rem;">{timestamp}</span>' if timestamp else ''}
                </div>
                <div>{content}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


def render_file_badge(filename: str, size: Optional[str] = None):
    """Render a file badge"""
    size_str = f" • {size}" if size else ""
    st.markdown(f"""
    <span class="file-badge">
        📎 {filename}{size_str}
    </span>
    """, unsafe_allow_html=True)


def render_conversation_stats(stats: dict):
    """Render conversation statistics"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Conversations",
            value=stats.get("total_conversations", 0)
        )
    
    with col2:
        st.metric(
            label="Total Messages",
            value=stats.get("total_messages", 0)
        )
    
    with col3:
        st.metric(
            label="Total Files",
            value=stats.get("total_files", 0)
        )
    
    with col4:
        avg_msgs = stats.get("avg_messages_per_conversation", 0)
        st.metric(
            label="Avg Messages/Chat",
            value=f"{avg_msgs:.1f}"
        )


def format_timestamp(iso_timestamp: str) -> str:
    """Format ISO timestamp for display"""
    try:
        dt = datetime.fromisoformat(iso_timestamp)
        return dt.strftime("%b %d, %Y at %I:%M %p")
    except:
        return iso_timestamp


def get_message_preview(content: str, max_length: int = 50) -> str:
    """Get preview text from message content"""
    if len(content) > max_length:
        return content[:max_length] + "..."
    return content


def render_empty_state():
    """Render empty state for no conversations"""
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <div style="font-size: 3rem; margin-bottom: 1rem;">💬</div>
        <h2>No conversations yet</h2>
        <p style="color: #666; margin-bottom: 1.5rem;">
            Click <strong>➕ New Chat</strong> in the sidebar to get started
        </p>
    </div>
    """, unsafe_allow_html=True)


def render_welcome_screen():
    """Render welcome screen for new users"""
    st.markdown("""
    <div style="text-align: center; padding: 3rem; max-width: 600px; margin: 0 auto;">
        <div style="font-size: 4rem; margin-bottom: 1rem;">🤖</div>
        <h1>Document Intelligence Chatbot</h1>
        <p style="font-size: 1.1rem; color: #666; margin-bottom: 2rem;">
            Upload your documents and ask questions. Our RAG-powered AI will analyze 
            and provide intelligent answers based on your content.
        </p>
        
        <div style="background: #f0f0f0; padding: 1.5rem; border-radius: 0.5rem; 
                    text-align: left; margin-bottom: 1.5rem;">
            <h3>✨ Features</h3>
            <ul>
                <li>📄 Upload PDF, TXT, and DOCX files</li>
                <li>🔍 Intelligent document analysis</li>
                <li>💬 Chat-like conversation interface</li>
                <li>📚 Chat history & persistence</li>
                <li>🔗 Context-aware responses</li>
            </ul>
        </div>
        
        <p style="color: #999; font-size: 0.9rem;">
            👈 Start by creating a new chat in the sidebar
        </p>
    </div>
    """, unsafe_allow_html=True)


def render_error_message(title: str, message: str):
    """Render error message"""
    st.error(f"**{title}**: {message}")


def render_success_message(title: str, message: str):
    """Render success message"""
    st.success(f"**{title}**: {message}")


def render_info_message(title: str, message: str):
    """Render info message"""
    st.info(f"**{title}**: {message}")


def render_warning_message(title: str, message: str):
    """Render warning message"""
    st.warning(f"**{title}**: {message}")


def create_two_column_layout(ratio: tuple = (1, 2)):
    """Create a two-column layout with custom ratio"""
    return st.columns(ratio)


def create_three_column_layout(ratio: tuple = (1, 1, 1)):
    """Create a three-column layout with custom ratio"""
    return st.columns(ratio)


def render_loading_spinner(text: str = "Loading..."):
    """Render a loading spinner"""
    with st.spinner(text):
        pass


def render_code_block(code: str, language: str = "python"):
    """Render a code block"""
    st.code(code, language=language)


def render_table(data: dict):
    """Render a table from data"""
    st.dataframe(data, use_container_width=True)


def render_metric_row(metrics: dict):
    """Render a row of metrics"""
    cols = st.columns(len(metrics))
    
    for col, (label, value) in zip(cols, metrics.items()):
        with col:
            st.metric(label=label, value=value)


def create_button_row(buttons: dict, key_prefix: str = ""):
    """Create a row of buttons"""
    cols = st.columns(len(buttons))
    
    results = {}
    for col, (label, key) in zip(cols, buttons.items()):
        with col:
            results[key] = st.button(label, key=f"{key_prefix}_{key}")
    
    return results


def render_file_manager_ui(files: List[dict], on_delete_callback=None):
    """Render file manager UI"""
    if not files:
        st.info("No files uploaded yet")
        return
    
    for idx, file_info in enumerate(files):
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            st.markdown(f"📎 **{file_info.get('name', 'Unknown')}**")
        
        with col2:
            if file_info.get('uploaded_at'):
                st.caption(format_timestamp(file_info['uploaded_at']))
        
        with col3:
            if st.button("🗑️", key=f"delete_file_{idx}"):
                if on_delete_callback:
                    on_delete_callback(file_info)


# CSS Styles
CUSTOM_CSS = """
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
</style>
"""


def apply_custom_css():
    """Apply custom CSS to the app"""
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
