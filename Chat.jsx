import { useState } from "react";
import axios from "axios";
import "./Chat.css";

function Chat() {

  const [query, setQuery] = useState("");

  const [messages, setMessages] =
    useState([]);

  const sendMessage = async () => {

    if (!query.trim()) return;

    const currentQuery = query;

    // Add user message
    setMessages(prev => [
      ...prev,
      {
        sender: "user",
        text: currentQuery
      }
    ]);

    setQuery("");

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          query: currentQuery
        }
      );

      let aiText = "";

      if (
        response.data.status ===
        "SOLVED"
      ) {

        aiText =

`🤖 AI Help Desk Assistant

I analyzed your issue and found a solution.

Issue:
${currentQuery}

Root Cause:
${response.data.cause}

Recommended Action:
${response.data.solution}

Confidence:
${response.data.confidence || 95}%

Status:
${response.data.status}`;

      } else {

        aiText =

`⚠️ Issue requires human assistance

Issue:
${currentQuery}

Ticket Created:
#${response.data.ticket_id}

Status:
OPEN

Our support team will contact you shortly.`;
      }

      setMessages(prev => [
        ...prev,
        {
          sender: "ai",
          text: aiText
        }
      ]);

    } catch (error) {

      console.error(error);

      setMessages(prev => [
        ...prev,
        {
          sender: "ai",
          text:
            "❌ Unable to contact the server."
        }
      ]);
    }
  };

  const handleKeyPress = (e) => {

    if (e.key === "Enter") {

      sendMessage();
    }
  };

  return (

    <div className="chat-container">

      <div className="chat-header">

        AI Help Desk Assistant

      </div>

      <div className="chat-messages">

        {messages.map(
          (msg, index) => (

            <div

              key={index}

              className={
                msg.sender === "user"
                  ? "user-message"
                  : "ai-message"
              }
            >

              {msg.text}

            </div>
          )
        )}

      </div>

      <div className="chat-input">

        <input

          type="text"

          value={query}

          placeholder=
            "Describe your issue..."

          onChange={(e) =>
            setQuery(
              e.target.value
            )
          }

          onKeyDown={
            handleKeyPress
          }
        />

        <button
          onClick={sendMessage}
        >
          Send
        </button>

      </div>

    </div>
  );
}

export default Chat;