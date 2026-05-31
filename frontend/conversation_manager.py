"""
Chat history and conversation management utilities
"""

import json
import os
from datetime import datetime
from pathlib import Path
import uuid
from typing import Dict, List, Optional


class ConversationManager:
    """Manages chat conversations and history"""
    
    def __init__(self, storage_dir: str = "conversations"):
        self.storage_dir = storage_dir
        os.makedirs(storage_dir, exist_ok=True)
    
    def create_conversation(self, title: str = None) -> str:
        """Create a new conversation"""
        conv_id = str(uuid.uuid4())[:8]
        
        conversation = {
            "id": conv_id,
            "title": title or "New Conversation",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "messages": [],
            "files": [],
            "metadata": {
                "message_count": 0,
                "file_count": 0
            }
        }
        
        self._save_conversation(conv_id, conversation)
        return conv_id
    
    def add_message(self, conv_id: str, role: str, content: str) -> None:
        """Add a message to conversation"""
        conversation = self.get_conversation(conv_id)
        if conversation:
            conversation["messages"].append({
                "role": role,
                "content": content,
                "timestamp": datetime.now().isoformat()
            })
            conversation["updated_at"] = datetime.now().isoformat()
            conversation["metadata"]["message_count"] = len(conversation["messages"])
            self._save_conversation(conv_id, conversation)
    
    def add_file(self, conv_id: str, filename: str) -> None:
        """Add a file to conversation"""
        conversation = self.get_conversation(conv_id)
        if conversation:
            file_info = {
                "name": filename,
                "uploaded_at": datetime.now().isoformat()
            }
            # Avoid duplicates
            if file_info not in conversation["files"]:
                conversation["files"].append(file_info)
                conversation["updated_at"] = datetime.now().isoformat()
                conversation["metadata"]["file_count"] = len(conversation["files"])
                self._save_conversation(conv_id, conversation)
    
    def remove_file(self, conv_id: str, filename: str) -> None:
        """Remove a file from conversation"""
        conversation = self.get_conversation(conv_id)
        if conversation:
            conversation["files"] = [
                f for f in conversation["files"] 
                if f.get("name") != filename
            ]
            conversation["updated_at"] = datetime.now().isoformat()
            conversation["metadata"]["file_count"] = len(conversation["files"])
            self._save_conversation(conv_id, conversation)
    
    def get_conversation(self, conv_id: str) -> Optional[Dict]:
        """Get a conversation by ID"""
        filepath = os.path.join(self.storage_dir, f"{conv_id}.json")
        
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                return json.load(f)
        return None
    
    def get_all_conversations(self) -> Dict[str, Dict]:
        """Get all conversations"""
        conversations = {}
        
        for filename in os.listdir(self.storage_dir):
            if filename.endswith(".json"):
                conv_id = filename.replace(".json", "")
                conversations[conv_id] = self.get_conversation(conv_id)
        
        # Sort by updated_at (newest first)
        return dict(sorted(
            conversations.items(),
            key=lambda x: x[1].get("updated_at", ""),
            reverse=True
        ))
    
    def update_title(self, conv_id: str, new_title: str) -> None:
        """Update conversation title"""
        conversation = self.get_conversation(conv_id)
        if conversation:
            conversation["title"] = new_title
            conversation["updated_at"] = datetime.now().isoformat()
            self._save_conversation(conv_id, conversation)
    
    def delete_conversation(self, conv_id: str) -> None:
        """Delete a conversation"""
        filepath = os.path.join(self.storage_dir, f"{conv_id}.json")
        
        if os.path.exists(filepath):
            os.remove(filepath)
    
    def clear_messages(self, conv_id: str) -> None:
        """Clear all messages in a conversation"""
        conversation = self.get_conversation(conv_id)
        if conversation:
            conversation["messages"] = []
            conversation["updated_at"] = datetime.now().isoformat()
            conversation["metadata"]["message_count"] = 0
            self._save_conversation(conv_id, conversation)
    
    def export_conversation(self, conv_id: str, export_format: str = "json") -> str:
        """Export conversation to file"""
        conversation = self.get_conversation(conv_id)
        if not conversation:
            return ""
        
        if export_format == "json":
            return json.dumps(conversation, indent=2)
        elif export_format == "txt":
            lines = [f"Conversation: {conversation.get('title', 'Untitled')}"]
            lines.append(f"Created: {conversation.get('created_at', '')}")
            lines.append(f"Files: {len(conversation.get('files', []))}")
            lines.append("-" * 50)
            
            for msg in conversation.get("messages", []):
                role = msg.get("role", "").upper()
                content = msg.get("content", "")
                lines.append(f"\n{role}:")
                lines.append(content)
            
            return "\n".join(lines)
        
        return ""
    
    def search_conversations(self, keyword: str) -> Dict[str, Dict]:
        """Search conversations by keyword"""
        results = {}
        keyword_lower = keyword.lower()
        
        for conv_id, conversation in self.get_all_conversations().items():
            # Search in title
            if keyword_lower in conversation.get("title", "").lower():
                results[conv_id] = conversation
                continue
            
            # Search in messages
            for message in conversation.get("messages", []):
                if keyword_lower in message.get("content", "").lower():
                    results[conv_id] = conversation
                    break
        
        return results
    
    def get_statistics(self) -> Dict:
        """Get statistics about all conversations"""
        conversations = self.get_all_conversations()
        
        total_messages = 0
        total_files = 0
        
        for conversation in conversations.values():
            total_messages += len(conversation.get("messages", []))
            total_files += len(conversation.get("files", []))
        
        return {
            "total_conversations": len(conversations),
            "total_messages": total_messages,
            "total_files": total_files,
            "avg_messages_per_conversation": (
                total_messages / len(conversations) if conversations else 0
            )
        }
    
    def _save_conversation(self, conv_id: str, conversation: Dict) -> None:
        """Save conversation to disk"""
        filepath = os.path.join(self.storage_dir, f"{conv_id}.json")
        
        with open(filepath, "w") as f:
            json.dump(conversation, f, indent=2)


# Singleton instance
_manager = None

def get_conversation_manager(storage_dir: str = "conversations") -> ConversationManager:
    """Get or create conversation manager instance"""
    global _manager
    if _manager is None:
        _manager = ConversationManager(storage_dir)
    return _manager
